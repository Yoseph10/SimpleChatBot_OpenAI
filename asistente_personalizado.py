import os
import openai
import sys


API_KEY_FILE = "clave_api.txt"
PRODUCTOS_FILE = "mis_productos.csv"  # ¡Crea este archivo con tus propios productos!
REGLAS_FILE = "mis_reglas.txt"        # ¡Crea este archivo con tus propias reglas!

try:
    with open(API_KEY_FILE) as archivo:
        openai.api_key = archivo.readline().strip()
    if not openai.api_key:
        raise ValueError(f"El archivo '{API_KEY_FILE}' está vacío o la clave no es válida.")
except FileNotFoundError:
    print(f"Error: El archivo '{API_KEY_FILE}' no se encontró. Asegúrate de que esté en el mismo directorio.")
    sys.exit(1)
except ValueError as e:
    print(f"Error en la clave API: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Ocurrió un error inesperado al cargar la clave API: {e}")
    sys.exit(1)

# --- Carga de productos ---
try:
    with open(PRODUCTOS_FILE, 'r', encoding='utf-8') as archivo:
        productos_data = archivo.read()
    if not productos_data.strip():
        print(f"Advertencia: El archivo '{PRODUCTOS_FILE}' está vacío. Tu asistente podría no tener información de productos.")
except FileNotFoundError:
    print(f"Error: El archivo '{PRODUCTOS_FILE}' no se encontró. ¡Crea este archivo con tu lista de productos!")
    sys.exit(1)
except Exception as e:
    print(f"Ocurrió un error inesperado al cargar los productos: {e}")
    sys.exit(1)

# --- Carga de reglas ---
try:
    with open(REGLAS_FILE, 'r', encoding='utf-8') as archivo:
        reglas_data = archivo.read()
    if not reglas_data.strip():
        print(f"Advertencia: El archivo '{REGLAS_FILE}' está vacío. Tu asistente podría no seguir las reglas esperadas.")
except FileNotFoundError:
    print(f"Error: El archivo '{REGLAS_FILE}' no se encontró. ¡Crea este archivo con tus reglas personalizadas!")
    sys.exit(1)
except Exception as e:
    print(f"Ocurrió un error inesperado al cargar las reglas: {e}")
    sys.exit(1)

# --- MEMORIA Y CONTEXTO DEL CHAT ---
contexto = []

contexto.append({'role':'system', 'content':f"""
    ¡Eres un asistente personalizado! Sigue estas reglas y usa la siguiente información:

    --- REGLAS DE COMPORTAMIENTO ---
    {reglas_data}

    --- DATOS DE PRODUCTOS/SERVICIOS ---
    {productos_data}

    Asegúrate de mantener un tono amigable y conversacional.
"""})


def enviar_mensajes(messages, model="gpt-4.1", temperature=0.2):
    """
    Envía una lista de mensajes al modelo de OpenAI y devuelve la respuesta.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        print(f"Error de la API de OpenAI: {e}")
        return "Lo siento, hubo un problema al procesar tu solicitud con la API. Por favor, verifica tu clave o inténtalo de nuevo más tarde."
    except openai.RateLimitError:
        print("Error de límite de tasa: Has enviado demasiadas solicitudes. Espera un momento e inténtalo de nuevo.")
        return "Lo siento, estamos recibiendo muchas solicitudes en este momento. Por favor, espera un momento y vuelve a intentarlo."
    except openai.APITimeoutError:
        print("Error de tiempo de espera de la API: La solicitud tardó demasiado.")
        return "Lo siento, la operación tardó demasiado. Por favor, inténtalo de nuevo."
    except openai.APIConnectionError as e:
        print(f"Error de conexión a la API: {e}")
        return "Lo siento, no pude conectarme a la API de OpenAI. Por favor, verifica tu conexión a internet."
    except Exception as e:
        print(f"Ocurrió un error inesperado en enviar_mensajes: {e}")
        return "Lo siento, algo salió mal. Por favor, inténtalo de nuevo."

def recargar_mensajes(charla):
    """
    Agrega el mensaje del usuario al contexto, envía todo el contexto al modelo,
    y luego agrega la respuesta del modelo al contexto.
    """
    contexto.append({'role':'user', 'content':f"{charla}"})
    print("\n--- Pensando... ---")
    response = enviar_mensajes(contexto)
    contexto.append({'role':'assistant','content':f"{response}"})
    print("\n--- Asistente: ---")
    print(response)
    print("--------------------\n")

# --- FUNCIÓN PRINCIPAL DEL CHATBOT ---

def main():
    print("¡Bienvenido a tu asistente personalizado!")
    print("Escribe 'exit' en cualquier momento para salir.")

    while True:
        mensaje = input("Coloca tu mensaje: ")

        if mensaje.lower() == 'exit':
            print("¡Gracias por usar el asistente! ¡Hasta pronto!")
            break

        if not mensaje.strip(): # Evitar enviar mensajes vacíos
            print("Por favor, ingresa algo.")
            continue

        recargar_mensajes(mensaje)

if __name__=='__main__':
    main()

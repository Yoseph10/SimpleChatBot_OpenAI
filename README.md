# 🤖 Asistente Personalizado con OpenAI (ChatGPT-4)

Este proyecto implementa un **asistente conversacional inteligente** usando la API de OpenAI (ChatGPT-4), configurado para interactuar de manera amigable con los usuarios y ofrecer respuestas contextualizadas sobre productos, siguiendo un conjunto de reglas definidas.  
Ideal para quienes quieren construir asistentes a medida para atención al cliente, ventas o soporte técnico.

---

## 🧠 ¿Qué hace este asistente?

**Simula un chatbot entrenado con:**

- 🛒 Una lista de productos o servicios (`mis_productos.csv`)
- 📏 Reglas de negocio y comportamiento (`mis_reglas.txt`)
- 🤖 Un modelo de lenguaje de OpenAI (GPT-4)

El asistente integra esta información y se comporta como un experto que responde preguntas de los usuarios, manteniendo el historial de conversación para conservar coherencia.

---

## ⚙️ Fases de Funcionamiento

1. **Carga de configuración:** Se leen reglas y productos desde archivos locales.
2. **Construcción de contexto:** Se simula una "memoria" de conversación para mantener el hilo de la charla.
3. **Interacción con OpenAI:** Se envía todo el contexto acumulado para generar una respuesta relevante.
4. **Visualización:** Se imprime la respuesta y se actualiza el contexto.
5. **Repetición:** Se mantiene la conversación de manera fluida.

---

## 📂 Estructura del Repositorio

```bash
asistente-personalizado/
│
├── asistente_personalizado.py    # Script principal
├── clave_api.txt                 # Archivo con tu API key de OpenAI (NO lo compartas públicamente)
├── mis_productos.csv             # Archivo CSV con tu catálogo de productos
├── mis_reglas.txt                # Reglas y estilo de comunicación
└── README.md                     # Este archivo

---

## 📂 Ejemplo de cómo funciona el ChatBot

<img width="1877" height="965" alt="image" src="https://github.com/user-attachments/assets/2373e4d1-34b2-43fe-8993-10ce8fdca0cd" />


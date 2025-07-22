import streamlit as st
import joblib

# Cargar modelo
model = joblib.load("spam_detector.pkl")

# Título de la app
st.title("🕵️‍♀️ Detector de correos spam o maliciosos")

# Entrada del usuario
mensaje = st.text_area("✉️ Escribe el contenido del correo o mensaje sospechoso:")

if st.button("🔍 Analizar"):
    pred = model.predict([mensaje])[0]
    resultado = "🚫 SPAM o malicioso" if pred else "✅ Confiable"
    st.markdown(f"### Resultado: {resultado}")

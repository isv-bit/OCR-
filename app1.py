import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title="OCR App",
    page_icon="📷",
    layout="wide"
)

# =========================
# ESTILO VISUAL
# =========================
st.markdown("""
<style>

/* Fondo general animado */
.main {
    background: linear-gradient(135deg, #00c6ff, #0072ff, #ff4b1f, #ff9068);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Título */
h1 {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: 900;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
}

/* Texto general */
p, label, span {
    color: white !important;
    font-weight: 500;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141e30, #243b55);
}

/* Botones */
.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    font-weight: bold;
    border-radius: 0px;
    height: 50px;
}

.stButton>button:hover {
    transform: scale(1.03);
    filter: brightness(1.2);
}

/* Caja de resultado */
div.stText {
    background: rgba(0,0,0,0.3);
    padding: 15px;
    border-radius: 0px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.title("📷 Reconocimiento Óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

# =========================
# PROCESAMIENTO
# =========================
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(img_rgb)

    st.markdown("### 🧠 Texto detectado:")
    st.write(text)

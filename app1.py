import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="OCR App",
    page_icon="📷",
    layout="wide"
)

# =========================
# ESTILO NUEVO (FONDO + LETRAS)
# =========================
st.markdown("""
<style>

/* Fondo general oscuro elegante */
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0b1220);
}

/* Título */
h1 {
    text-align: center;
    color: #00e5ff;
    font-size: 44px;
    font-weight: 900;
    text-shadow: 0px 0px 15px rgba(0,229,255,0.4);
}

/* Texto general */
p, label, span, div {
    color: #e2e8f0 !important;
    font-weight: 500;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220, #111827);
}

/* Botón cámara */
.stButton>button {
    background: linear-gradient(90deg, #00e5ff, #7c3aed);
    color: white;
    font-weight: bold;
    border-radius: 0px;
    height: 50px;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.03);
    filter: brightness(1.2);
}

/* Caja de resultado */
div.stText, .stMarkdown {
    color: #f8fafc !important;
}

/* radio buttons */
.stRadio label {
    color: #cbd5e1 !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# APP
# =========================
st.title("📷 Reconocimiento Óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(img_rgb)

    st.markdown("### 🧠 Texto detectado:")
    st.write(text)

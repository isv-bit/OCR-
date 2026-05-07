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
# ESTILO VISUAL
# =========================
st.markdown("""
<style>

/* Fondo vivo tipo neón */
.main {
    background: linear-gradient(135deg, #ff00cc, #3333ff, #00ffcc, #ffcc00);
    background-size: 400% 400%;
    animation: gradientMove 8s ease infinite;
}

/* Animación */
@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Título */
h1 {
    text-align: center;
    color: #ffffff;
    font-size: 44px;
    font-weight: 900;
    text-shadow: 0px 0px 20px rgba(0,0,0,0.6);
}

/* Texto general */
p, label, span, div {
    color: #ffffff !important;
    font-weight: 500;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a0033, #000814);
}

/* Botones */
.stButton>button {
    background: linear-gradient(90deg, #ff00cc, #00ffcc);
    color: white;
    font-weight: bold;
    border-radius: 0px;
    height: 50px;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.05);
    filter: brightness(1.2);
}

/* Resultado */
.stMarkdown, .stText {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.title("📷 Reconocimiento Óptico de Caracteres")

# Cámara
img_file_buffer = st.camera_input("Toma una Foto")

# Sidebar
with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

# =========================
# PROCESAMIENTO DE IMAGEN
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

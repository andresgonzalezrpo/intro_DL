import streamlit as st
from PIL import Image
import io

st.title(" Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('hub.jfif')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('El tacto es fundamental para tu interfaz')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )

st.subheader("📸 Capturar Foto")

foto = st.camera_input("Toma una foto con tu cámara")

if foto is not None:
    image_foto = Image.open(foto)

    st.success("Foto capturada correctamente ✅")
    st.image(image_foto, caption="Vista previa de la foto", use_column_width=True)

    # Descargar la imagen
    buffer = io.BytesIO()
    image_foto.save(buffer, format="JPEG")

    st.download_button(
        label="Descargar foto",
        data=buffer.getvalue(),
        file_name="foto.jpg",
        mime="image/jpeg"
    )

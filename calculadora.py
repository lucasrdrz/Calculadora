import streamlit as st

st.title("Calculadora de Dilución")

# Entradas del usuario
volumen_total = st.number_input("Tamaño del envase a utilizar para la dilución (ml)", min_value=1, value=100)
proporcion_input = st.text_input("Relación de dilución del producto (ej. 1:10)", value="1:10")

if st.button("Calcular"):
    try:
        parte_producto, parte_total = map(int, proporcion_input.split(":"))
        cantidad_producto = volumen_total * parte_producto / parte_total
        cantidad_agua = volumen_total - cantidad_producto

        st.markdown(f"**Volumen del contenedor:** {volumen_total} ml")
        st.markdown(f"**Cantidad de producto:** {cantidad_producto:.2f} ml")
        st.markdown(f"**Cantidad de agua:** {cantidad_agua:.2f} ml")
    except:
        st.error("Por favor ingrese una proporción válida en el formato 1:10")

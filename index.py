import streamlit as st
import time

def main():
    st.title("Esse é meu título")
    st.write("Esse é meu primeiro Hello World em Streamlit")

    st.header("Input de texto no header")
    input_text = st.text_input("Digite um texto aqui neste input: ")
    if input_text:
        st.write("Você digitou: ", input_text)

    st.header("Seleção")
    selected_option = st.selectbox("Selecione uma opção: ", ["opção 1", "opção 2", "opção 3", "opção 4"])
    if selected_option:
        st.write("O usuário selecionou a opção: ", selected_option)


    st.header("Slider")
    slider_view = st.slider ("Escolha um valor: ", 0, 100, 50)
    st.write("O valor escolhido é ", slider_view)

    checkbox_boolean = st.checkbox ("Marque para ativar!")
    st.write("Checkbox", checkbox_boolean)
    
    if st.button("Clique aqui: "):
         st.write("Você clicou no botão!")

    st.header("Loading...")
    with st.spinner("Aguarde..."):
        time.sleep(3)
    st.success("Carregado!")

    st.header("Upload de arquivo")
    uploaded_file = st.file_uploader("Escolha um arquivo para subir: ", type=["pdf", "png", "jpeg"])

    if uploaded_file:
        st.write("Nome do arquivo: ", uploaded_file.name)

    st.header("Grafico")
    data = {'x': [1,2,3,4,5], 'y': [10,20,30,40,50]}
    st.line_chart(data)         

main() 
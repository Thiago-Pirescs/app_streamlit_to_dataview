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


main() 
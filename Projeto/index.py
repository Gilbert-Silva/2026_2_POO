from templates.manterclienteui import ManterClienteUI
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterprodutoui import ManterProdutoUI
import streamlit as st

class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Categorias", "Produtos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Categorias": ManterCategoriaUI.main()
        if op == "Produtos": ManterProdutoUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()
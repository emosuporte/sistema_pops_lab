import streamlit as st
import os
import fitz  # PyMuPDF
from PIL import Image


def listar_pdfs(caminho_pasta):
    return [arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.endswith('.pdf')]


def main():
    st.title('Sistema de Visualização de POPs')

    menu = ["Listar POPs", "Visualizar POP"]
    escolha = st.sidebar.selectbox("Escolha uma opção", menu)

    caminho_pasta = r'D:\NoteDell\Meus Projetos\DEV2023\PROJETO PYTHON 2023\CRIAR SITE COM STREAMLIT\GESTOR POP LAB\POPS'

    if escolha == "Listar POPs":
        st.subheader("Lista de POPs disponíveis")
        pops = listar_pdfs(caminho_pasta)
        for pop in pops:
            st.write(pop)

    elif escolha == "Visualizar POP":
        st.subheader("Visualizar POP específico")
        pops = listar_pdfs(caminho_pasta)
        pop_selecionado = st.selectbox("Escolha um POP", pops)
        if pop_selecionado:
            caminho_completo = os.path.join(caminho_pasta, pop_selecionado)

            # Abre o PDF com o PyMuPDF
            pdf = fitz.open(caminho_completo)

            # Itera sobre cada página
            for page_num in range(len(pdf)):
                # Pega a página
                page = pdf.load_page(page_num)

                # Renderiza a página para uma imagem com maior resolução
                mat = fitz.Matrix(2.0, 2.0)  # Ajusta a escala (2.0 vezes em cada dimensão neste exemplo)
                image = page.get_pixmap(matrix=mat)

                # Converte o Pixmap em uma imagem PIL
                image = Image.frombytes("RGB", [image.width, image.height], image.samples)

                # Exibe a imagem no Streamlit
                st.image(image, caption=f"Página {page_num + 1}", use_column_width=True)

            # Opção de download
            with open(caminho_completo, 'rb') as f:
                st.download_button(label="Download POP", data=f, file_name=pop_selecionado, mime='application/pdf')


if __name__ == "__main__":
    main()

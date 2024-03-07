import pandas as pd
import streamlit as st
from PIL import Image

# <a href="https://br.freepik.com/vetores-gratis/texto-neon-de-clinica-e-dente-brilhante-com-coroa_4550664.htm#query
# =dentist%20logo&position=12&from_view=search&track=robertav1_2_sidr">Imagem de katemangostar</a> no Freepik

st.image(Image.open('imagens/logo2.jpg'))
st.title('Diário de obra 📆')

tab1, tab2 = st.tabs(["🗃 Livro", "📈 Produtividade"])

tab1.subheader('📍 Selecionar data')

tab1.date_input('data', label_visibility="hidden")

tab1.subheader('Registros do dia 📑')
tab1.text_area('Livro', label_visibility="hidden", height=350)

tab1.button('Salvar')


tab2.subheader('Status da obra')
tabela = pd.DataFrame(data=None, columns=['procedimento', 'resposável', 'status (%)'])
tab2.table(tabela)

tab2.subheader('Registrar produtividade')
tab2.selectbox('Selecionar o procedimento', ('Piso', 'Parede', 'Teto'))
tab2.multiselect('Selecionar os funcionarios', ['Piao1', 'Piao2', 'Piao3'])
tab2.number_input('Quanto foi feito')
tab2.date_input('Quando foi feito')
tab2.text_area('Observacoes', height=150)

tab2.button('Atualizar')


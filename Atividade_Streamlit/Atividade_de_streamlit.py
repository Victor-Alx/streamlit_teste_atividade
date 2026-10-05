import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")

st.subheader("Victor")

nome = "Victor"

idade = 17

st.write("Olá,",nome," sua idade é ",idade)

df = pd.DataFrame({
   'Matérias': ["Português", "Matemática", "Python", "Frame"],
   'Notas': [5, 9, 7, 10]
})

df

st.subheader("Caixa de seleção (Professora isso aqui é só meme)")

itens_precos = {
    "Arroz (5Kg)":25.90,
    "Feijão Preto (1Kg)": 1.00,
    "Leite de Femboy (1L)":69.00,
    "Café Yasuo (500g)": 120000.00,
    "Açúcar Escobar (1Kg)": 200.00,
    "Óleo de Pica (Apenas usável no Kayllan)":67.00,
    "Pão Cacetinho":7.50
}

def calcular_preco(itens_precos):
    total = sum(itens_precos[item] for item in itens_selecionados)
    return total

itens_selecionados = st.multiselect(
    "Selecione alguns dos itens:",
    options = list(itens_precos.keys())
)

if itens_selecionados:
    st.subheader("Itens Selecionados:")
    for item in itens_selecionados:
        st.write(f"- {item}: R$ {itens_precos[item]}")
        
    total_compra = calcular_preco(itens_precos)
    
    st.divider()
    st.metric(label="Total da Compra", value=f"R$ {total_compra}")
else:
    st.info("Nenhum item selecionado...")
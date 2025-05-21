import streamlit as st
import requests

st.set_page_config(page_title="Busca de Endereço por CEP", layout="centered")
st.title("📍 Consulta por CEP")

# Campo de entrada
cep_input = st.text_input("Digite o CEP (somente números):", max_chars=8)

if cep_input:
    if len(cep_input) != 8 or not cep_input.isdigit():
        st.error("❌ CEP inválido. Digite exatamente 8 números.")
    else:
        with st.spinner("🔍 Buscando informações..."):
            url = f"https://viacep.com.br/ws/{cep_input}/json/"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if "erro" in data:
                    st.error("🚫 CEP não encontrado.")
                else:
                    st.success("✅ Endereço encontrado!")
                    st.markdown(f"""
                    <div style="border: 1px solid #ccc; border-radius: 10px; padding: 20px; background-color: #f2f2f2;">
                        <h4>{data['logradouro'] or 'Rua não informada'}</h4>
                        <p><strong>Bairro:</strong> {data['bairro'] or 'Não informado'}</p>
                        <p><strong>Cidade:</strong> {data['localidade']}</p>
                        <p><strong>Estado:</strong> {data['uf']}</p>
                        <p><strong>CEP:</strong> {data['cep']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.error("Erro ao acessar a API. Tente novamente mais tarde.")

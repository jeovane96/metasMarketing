import streamlit as st
import controllers.suprimentos.cadastrarContratosCon.listarContratos as listarContratos
import pandas as pd

def ListContratos():
    customerList = []

    for item in listarContratos.selecionarContratos():
        customerList.append(
            [
            item.id, 
            item.cd_empresa,    
            item.nu_contrato,         
            item.vl_orcamento,        
            item.vl_primeira_proposta,      
            item.user_insert,  
            item.dt_insert    
            ]
        )

    df = pd.DataFrame(
        customerList,
        columns=['ID', 'Cód. Empresa', 'Contrato', 'Orçamento', 'Primeira Proposta', 'Usuário', 'Data de Cadastro']
    )

    table_html = df.to_html(index=False, classes="table", border=1)

    st.markdown("""
        <style>
            .table-container {
                max-height: 600px;  /* Ajuste a altura conforme necessário */
                overflow-y: auto;  /* Habilita a rolagem vertical */
                margin-top: 20px;
            }
            .table {
                width: 100%;
                text-align: center;
                border-collapse: collapse;
            }
            .table th {
                background-color: black;
                color: white;
                padding: 10px;
                text-align: center;  /* CENTRALIZA OS CABEÇALHOS */
                position: sticky;
                top: 0;
                z-index: 1;  /* Garante que o cabeçalho ficará acima do conteúdo */
                font-size: 14px; /* Ajuste conforme necessário */
            }
            .table td {
                border: 1px solid grow;
                padding: 8px;
                text-align: center; /* CENTRALIZA O CONTEÚDO */
                font-size: 12px; /* Ajuste conforme necessário */

            }
            .table tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .table tr:nth-child(odd) {
                background-color: #ffffff;
            }
            .table tr:hover {
                background-color: #ddd;
            }
        </style>
    """, unsafe_allow_html=True)

    # Envolver a tabela com a div para permitir a rolagem
    st.markdown(f"<div class='table-container'>{table_html}</div>", unsafe_allow_html=True)
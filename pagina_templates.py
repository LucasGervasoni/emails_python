import streamlit as st
from utilidades import *

# TEMPLATES
def pag_templates():
    st.markdown('# Templates')
    st.divider()
    
    for arquivo in PASTA_TEMPLATES.glob('*.txt'):
        nome_arquivo = arquivo.stem.replace('_', ' ').upper()
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_arquivo, key=f'{nome_arquivo}', on_click=_usar_template, args=(nome_arquivo,), use_container_width=True)
        col2.button('EDITAR', key=f'editar_{nome_arquivo}', on_click=_editar_arquivo, args=(nome_arquivo,), use_container_width=True)
        col3.button('REMOVER', key=f'remover_{nome_arquivo}', on_click=_remover_template, args=(nome_arquivo,), use_container_width=True)
    
    st.divider()
    st.button('Adicionar Novo Template', on_click=mudar_pagina, args=('adicionar novo template',))

def pag_adicionar_novo_template(nome_template='', text_template=''):
    nome_template = st.text_input('Nome do Template:', value=nome_template)
    text_template = st.text_area('Escreva o texto do template:', value=text_template, height=600)
    st.button('Salvar', on_click=_salvar_template, args=(nome_template, text_template))
    
def _usar_template(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(PASTA_TEMPLATES / nome_arquivo, 'r') as f:
        texto_arquivo = f.read()
    st.session_state.corpo_atual = texto_arquivo
    mudar_pagina('home')

def _salvar_template(nome, texto):
    PASTA_TEMPLATES.mkdir(exist_ok=True)
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(PASTA_TEMPLATES / nome_arquivo, 'w') as f:
        f.write(texto)
    mudar_pagina('templates')

def _remover_template(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    (PASTA_TEMPLATES / nome_arquivo).unlink()
 
def _editar_arquivo(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(PASTA_TEMPLATES / nome_arquivo, 'r') as f:
        texto_arquivo = f.read()
    st.session_state.nome_template_editar = nome
    st.session_state.texto_template_editar = texto_arquivo
    mudar_pagina('editar_template')
   
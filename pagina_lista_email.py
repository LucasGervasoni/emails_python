import streamlit as st
from utilidades import *

# LISTA DE EMAILS    
def pag_lista_de_emails():
    st.markdown('# Lista de Emails')
    st.divider()
    
    for arquivo in PASTA_LISTA_EMAILS.glob('*.txt'):
        nome_lista = arquivo.stem.replace('_', ' ').upper()
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_lista, key=f'{nome_lista}', on_click=_usar_lista, args=(nome_lista,), use_container_width=True)
        col2.button('EDITAR', key=f'editar_{nome_lista}', on_click=_editar_lista, args=(nome_lista,), use_container_width=True)
        col3.button('REMOVER', key=f'remover_{nome_lista}', on_click=_remover_lista, args=(nome_lista,), use_container_width=True)
    
    st.divider()
    st.button('Adicionar Lista', on_click=mudar_pagina, args=('adicionar nova lista',))
    
def pag_adicionar_nova_lista(nome_template='', text_template=''):
    nome_lista = st.text_input('Nome da Lista:', value=nome_template)
    emails_lista = st.text_area('Escreva os emails separados por vírgula:', value=text_template, height=600)
    st.button('Salvar', on_click=_salvar_lista, args=(nome_lista, emails_lista))
    
def _usar_lista(nome):
    nome_lista = nome.replace(' ', '_').lower() + '.txt'
    with open(PASTA_LISTA_EMAILS / nome_lista, 'r') as f:
        emails_lista = f.read()
    st.session_state.destinatarios_atual = emails_lista
    mudar_pagina('home')

def _salvar_lista(nome, texto):
    PASTA_LISTA_EMAILS.mkdir(exist_ok=True)
    nome_lista = nome.replace(' ', '_').lower() + '.txt'
    with open(PASTA_LISTA_EMAILS / nome_lista, 'w') as f:
        f.write(texto)
    mudar_pagina('lista de emails')

def _remover_lista(nome):
    nome_lista = nome.replace(' ', '_').lower() + '.txt'
    (PASTA_LISTA_EMAILS / nome_lista).unlink()

def _editar_lista(nome):
    nome_lista = nome.replace(' ', '_').lower() + '.txt'
    with open(PASTA_LISTA_EMAILS / nome_lista, 'r') as f:
        emails_lista = f.read()
    st.session_state.nome_lista_editar = nome
    st.session_state.texto_lista_editar = emails_lista
    mudar_pagina('editar_lista')

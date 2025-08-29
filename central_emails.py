import streamlit as st
from utilidades import *
from pagina_configuracoes import pag_configuracoes, ler_email_usuario, ler_chave
from pagina_lista_email import pag_lista_de_emails, pag_adicionar_nova_lista
from pagina_templates import pag_templates, pag_adicionar_novo_template
 
# HOME
def home():
    destonatario_atual = st.session_state.destinatarios_atual
    titulo_atual = st.session_state.titulo_atual
    corpo_atual = st.session_state.corpo_atual
    
    st.markdown('# Enviar email')
    destinatarios = st.text_input('Destinatários do email:', value=destonatario_atual)
    titulo = st.text_input('Título do email:', value=titulo_atual)
    corpo = st.text_area('Corpo do email:', height=400, value=corpo_atual)
    
    col1, col2, col3 = st.columns(3)
    col1.button('Enviar Email', on_click=_enviar_email, args=(destinatarios, titulo, corpo), use_container_width=True)
    col3.button('Limpar', on_click=_limpar, use_container_width=True)
    
    st.session_state.destinatarios_atual = destinatarios
    st.session_state.titulo_atual = titulo
    st.session_state.corpo_atual = corpo

def _limpar():
    st.session_state.destinatarios_atual = ''
    st.session_state.titulo_atual = ''
    st.session_state.corpo_atual = ''

def _enviar_email(destinatarios, titulo, corpo):
    destinatarios = destinatarios.replace(' ', '').split(',')
    email = ler_email_usuario()
    chave = ler_chave()
    if email == '':
        st.error('Adicione email na página de configurações')
    elif chave == '':
        st.error('Adicione chave de email na página de configurações')
    else:
        enviar_email(email,destinatarios=destinatarios, titulo=titulo, corpo=corpo, senha_app=chave)
    

def main():
    inicializacao()
    st.sidebar.button('Enviar email', on_click=mudar_pagina, args=('home',), use_container_width=True)
    st.sidebar.button('Templates', on_click=mudar_pagina, args=('templates',), use_container_width=True)
    st.sidebar.button('Lista de Emails', on_click=mudar_pagina, args=('lista de emails',), use_container_width=True)
    st.sidebar.button('Configurações', on_click=mudar_pagina, args=('configurações',), use_container_width=True)


    if st.session_state.pagina_central_email == 'home':
        home()
    elif st.session_state.pagina_central_email == 'templates':
        pag_templates()
    elif st.session_state.pagina_central_email == 'adicionar novo template':
        pag_adicionar_novo_template()
    elif st.session_state.pagina_central_email == 'editar_template':
        nome_template_editar = st.session_state.nome_template_editar
        texto_template_editar = st.session_state.texto_template_editar
        pag_adicionar_novo_template(nome_template_editar, texto_template_editar)
    elif st.session_state.pagina_central_email == 'lista de emails':
        pag_lista_de_emails()
    elif st.session_state.pagina_central_email == 'adicionar nova lista':
        pag_adicionar_nova_lista()
    elif st.session_state.pagina_central_email == 'editar_lista':
        nome_lista_editar = st.session_state.nome_lista_editar
        texto_lista_editar = st.session_state.texto_lista_editar
        pag_adicionar_nova_lista(nome_lista_editar, texto_lista_editar)
    elif st.session_state.pagina_central_email == 'configurações':
        pag_configuracoes()

main()
# Aprendendo a Enviar e Receber E-mails com Python

Este repositório foi criado com o objetivo de demonstrar como interagir com e-mails utilizando Python.

* **Receber e ler e-mails** de uma caixa de entrada usando a biblioteca `imbox`.
* **Enviar e-mails** através de um servidor SMTP com a biblioteca nativa `smtplib`.


## 🛠️ Tecnologias e Bibliotecas

* **Python**
* **imbox**: Para leitura de e-mails de servidores IMAP de forma simplificada.
* **smtplib**: Biblioteca padrão do Python para envio de e-mails via SMTP.

## ⚙️ Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    A única biblioteca externa que precisamos instalar é a `imbox`.
    ```bash
    pip install imbox
    ```

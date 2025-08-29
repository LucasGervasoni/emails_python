from imbox import Imbox
import json
from datetime import datetime

CREDENTIALS_PATH = 'credentials.json'

with open(CREDENTIALS_PATH, 'r') as file:
    credentials_data = json.load(file)
    
host = 'imap.gmail.com'
email = credentials_data['email']
password = credentials_data['google_password']

with Imbox(host, username=email, password=password) as imbox:
    print("Conexão estabelecida com sucesso!")
    messages = imbox.messages(unread=True)
    
    if not messages:
        print("Nenhum e-mail não lido encontrado.")
        quit()
    
    print(f"Total de e-mails não lidos: {len(messages)}")
    
    #listar emails recebidos
    # for uid, message in messages:
    #     print(f"De: {message.sent_from}\n Assunto: {message.subject}\n")
    
    #ler o conteudo de um email especifico
    # message = imbox.messages(subject="Teste email")[0]
    # body = message[1].body['plain']
    # print(body)
    
    #filtrar emails por data
    # start_date = datetime(2023, 1, 1)
    # messages = imbox.messages(date__gt=start_date)
    # print(f"E-mails recebidos após {start_date.date()}: {len(messages)}")
    
    #excluir emails com base em critérios
    # start_date = datetime(2023, 1, 1)
    # messages = imbox.messages(date__gt=start_date)
    # for msg in massages:
    #   msg.delete()
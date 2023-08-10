from flask import Flask
from whois import whois

import re

# iniciar o aplicativo Flask
app = Flask(__name__)
app.debug = False

def validMAil(email):
    # Validamos o email comparando ele com um regex.
    return (re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def validDomain(dominio):
    try:
        # Fazemos um Whoi no dominio para ver se ele esta registrado ou não.
        return whois(dominio)
    except Exception:
        return False


@app.route('/<email>')
def testMail(*args, **kwargs):

    # Se na request não tem o parametro e-mail retorna uma mensagem
    if not (email := kwargs.get('email')):
        return 'Não foi enviado um email na request.'
    # Se o e-mail não e valido retorna uma mensagem para o usuario
    if not validMAil(email=email):
        return f'El email {email} não é valido.'    

    txt = email.find("@") 
    dom = email[txt+1:] # obtemos o dominio do email.

    if not (dominio := validDomain(dom)):       
        return f'O dominio {dom} não existe ou não é valido.'    
    return f'O dominio: {dominio.domain_name} existe e esta corretamente registrado.'
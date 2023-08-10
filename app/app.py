from flask import Flask
from whois import whois

import re

app = Flask(__name__)
app.debug = False

def validMAil(email):
    return (re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def validDomain(dominio):
    try:
        return whois(dominio)
    except Exception:
        return False


@app.route('/<email>')
def testMail(*args, **kwargs):

    if not (email := kwargs.get('email')):
        return 'Não foi enviado um email na request.'

    if not validMAil(email=email):
        return f'El email {email} não é valido.'    

    txt = email.find("@")
    dom = email[txt+1:]
    if not (dominio := validDomain(dom)):       
        return f'O dominio {dom} não existe ou não é valido.'
    
    return f'O dominio: {dominio.domain_name} existe e esta corretamente registrado.'
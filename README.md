# Teste Técnico Alfaero


## Instruções para instalação: 

* git clone https://github.com/mitdua/test_alfaero.git
* cd /app
* docker build . --tag test-alfaero
* docker run -p 5000:5000 test-alfaero

## Intruções para uso:



```
curl 127.0.0.1:5000/ing.macdo@gmail.com
O dominio: ['GMAIL.COM', 'gmail.com'] existe e esta corretamente registrado
```
Neste caso detecta que o dominio gmail.com existe  esta correctamente registrado.


```
curl 127.0.0.1:5000/ing.macdogmail.com
El email ing.macdogmail.com não é valido.
```
Neste caso o email enviado no é valido.

```
curl 127.0.0.1:5000/ing.macdo@xfrgmail.com
O dominio xfrgmail.com não existe ou não é valido.
```
Neste caso o dominio enviado no é valido.
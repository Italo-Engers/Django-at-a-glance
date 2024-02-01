# O que é o projeto
O projeto consiste de códigos gerados a partir do seguinte tutorial:
https://docs.djangoproject.com/en/5.0/intro/overview/

Feito com o framework Django e códigos em python e html. Todos os comandos são baseados em Linux.

## Para executar o projeto localmente com ambiente virtual:
  python -m venv .environment
##  Para ativar o ambiente virtual
  source .environment/bin/activate
##  Para instalar as bibliotecas utilizadas:
  pip install -r requirements.txt
# Para criar o projeto no Django, primeiramente execute:
  django-admin starproject nomeprojeto .
Obs: colocando . no final, django-admin starproject nomeprojeto . ele não cria subpasta

Após isto preencha cada arquivo (models, views, apps, urls, etc...) conforme sua aplicação.

Em seguida, execute os utilitários de linha de comando do Django para criar as tabelas do banco de dados automaticamente (Linux e Mac):
$ python manage.py makemigrations
$ python manage.py migrate

## Para listar as migrações de um projeto e seu status.
  python manage.py showmigrations 
Saiba mais em:
https://docs.djangoproject.com/en/5.0/topics/migrations/
  
## Para rodar o servidor e verificar se está funcionando:
  python manage.py runserver
  
## Para criar um usuário admin:
python manage.py createsuperuser
Configure com usuário e senha. Utilize o /admin no navegador para acessar.


## Para criar um script, scripts/populate.py pra popular o banco da intro:
from django import setup

setup()

from primeiro.news.models import Article, Reporter

...

Para usar scripts é necessário instalar o seu projeto como um modulo de python. Nesse caso é necessário (1) configurar o projeto para ser instalado e (2) instalar o projeto como editável.
executar script:

### Para configurar o projeto adicione o seguinte arquivo na raiz:
from setuptools import setup, find_packages

setup(
    name='primeiro',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
)
### Para instalar o projeto primeiro ative o ambiente virtual e em seguida execute:
pip install --editable .
### Então o projeto deve contar com a seguinte estrutura de pastas:
![image](https://github.com/Italo-Engers/Django-at-a-glance/assets/95890206/dee24b87-4164-435a-b5a3-71ec86ee8d12)

### Execute o projeto com a variável de ambiente:
DJANGO_SETTINGS_MODULE=primeiro.settings python scripts/populate.py


# Miridam - Sistemas de gestão de RH - Versão 2

As funções básicas do sistema é de um CRUD com API's, a princio as views rederizarão o frontend em _HTML_. Os usuários logados podem adicionar, remove funcionários, departamentos, cargo e empresas.

## Como rodar a aplicação
- Você deve fazer um clone do repositório
- Abra o local do projeto no terminal
- Criando ambiente virtual : python -m venv venv
- Ative o ambiente virtual (Windowns) : venv\scripts\activate
- Ative o ambiente virtual (Linux) : venv/bin/activate
- Instale todas as libs e frameworks : pip install -r requirements.txt
- Faça as migrações : python manage.py makemigrations
- Faça as migrações : python manage.py migrate
- Inice o servidor local : python manage.py runserver

## Configuração das variváveis de ambiente

- Nesse link está a documentação do python-decouple mostrando o passo a passo de como separar as variaveis de ambiente.
- [Python-Decouple](https://pypi.org/project/python-decouple/)


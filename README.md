#Projeto CRUD em Python

CRUD utilizando a linguagem Python, realizado no curso Crud com Python do Canal Webdesign em Foco, utilizando o sistemas de gerenciamento de bancos de dados MySQL.

Primeiro foi criada uma máquina virtual para os módulos ficarem especificamente para o projeto e não de maneira global, para isso criei uma pasta chamada python e utilizei o comando dentro dela:
> python -m venv venv

Utilizando a venv restringimos que os módulos instalados sejam importados apenas ao projeto atual, sem instalar de modo global.

Ao sair do projeto, para retornar é necessário utilizar o comando dentro da pasta python:
> cd venv/Scripts 

> activate

Tudo o que instalar no projeto ficará restrito nesse diretório.

Para esse projeto, utilizamos o framework Django, com o seguinte comando para instalar: 
> python -m pip install Django  

E posteriormente criei o projeto na pasta python (com seus respectivos arquivos de configuração), com o comando:
> django-admin startproject myproject

O "myproject" no comando acima refere-se ao nome do projeto.

Para criar a aplicação, utiliza-se o comando na pasta do projeto:
> python manage.py startapp app

Para que o projeto entenda que essa pasta app faz parte dele, é necessário inserir o nome dele, no caso 'app', no item INSTALLED_APPS do arquivo settings da pasta myproject.

Para rodar o projeto, utiliza o comando:
> python manage.py runserver
# Projeto CRUD em Python

## Iniciando o projeto

>Descrição: Projeto CRUD utilizando a linguagem Python, realizado no curso Crud com Python do Canal Webdesign em Foco, utilizando o sistemas de gerenciamento de bancos de dados MySQL.

Primeiro foi criada uma máquina virtual para os módulos ficarem especificamente para o projeto e não de maneira global, para isso criei uma pasta chamada python e utilizei o comando dentro dela:
```
python -m venv venv
```

Utilizando a venv restringimos que os módulos instalados sejam importados apenas ao projeto atual, sem instalar de modo global.

Ao sair do projeto, para retornar é necessário utilizar o comando dentro da pasta python:
```
cd venv/Scripts 
```

```
activate
```
Tudo o que instalar no projeto ficará restrito nesse diretório.

## Desenvolvimento do projeto
Para esse projeto, utilizamos o framework Django, com o seguinte comando para instalar: 
```
python -m pip install Django  
```

E posteriormente criei o projeto na pasta python (com seus respectivos arquivos de configuração), com o comando:
```
django-admin startproject myproject
```

O "myproject" no comando acima refere-se ao nome do projeto.

Para criar a aplicação, utiliza-se o comando na pasta do projeto:
```
python manage.py startapp app
```

Para que o projeto entenda que essa pasta app faz parte dele, é necessário inserir o nome dele, no caso 'app', na lista de apps do projeto do item INSTALLED_APPS, do arquivo "settings.py" da pasta "myproject".

### Rodando o projeto

Para rodar o projeto, utiliza-se os comandos: </br>

1 - Dentro da pasta python:
```
cd venv/Scripts 
```

```
activate
```
2 - Retorna à pasta python e roda o projeto:
```
python manage.py runserver
```

## Estrutura do Projeto
A estrutura de um projeto Django é baseada no padrão de arquitetura MVC (Model-View-Controller). 

A estrutura de pastas padrão de um projeto Django é a seguinte:

```
mysite/
    manage.py
    core/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    apps/
        myapp/
            __init__.py
            models.py
            views.py
            urls.py
    templates/
        base.html
        myapp/
            index.html
```

* O arquivo "manage.py" é um script Python que é usado para executar tarefas administrativas, como criar, iniciar e parar o servidor web.

* O arquivo "core/settings.py" contém as configurações do projeto, como a URL base, as configurações de banco de dados e as configurações de segurança.

* O arquivo "core/urls.py" define as URLs do projeto.

* O arquivo "core/wsgi.py" é um arquivo de configuração WSGI que é usado para iniciar o servidor web.

* A pasta "apps/" contém as aplicações do projeto. Cada aplicação é um pacote Python que contém os modelos, as visualizações e os URLs da aplicação.

* A pasta "templates/" contém os templates HTML do projeto.

### Arquivos da pasta apps/myapp/

O arquivo "models.py" contém as definições dos modelos do aplicativo. Os modelos são classes Python que representam os dados do aplicativo. Eles são usados para definir a estrutura do banco de dados e para acessar os dados do banco de dados.

As "views" são responsáveis por toda a lógica de negócios do aplicativo, como acessar os dados do banco de dados, gerar conteúdo HTML e redirecionar os usuários para outras páginas. Cada view é uma função que recebe uma solicitação HTTP como parâmetro e retorna uma resposta HTTP como valor de retorno.

O arquivo "urls.py" define as URLs da aplicação myapp. As URLs são usadas para mapear as solicitações HTTP para as views da aplicação.

### Templates

Os templates são arquivos HTML que são usados para gerar o conteúdo que é exibido para o usuário. Os templates são usados para separar a lógica de negócios da apresentação.

Para o "index.html", foi utilizado o Bootstrap via CDN retirado do site https://getbootstrap.com/, assim como a tabela retirada de https://getbootstrap.com/docs/4.1/content/tables/ modelo Table head options

A documentação do Django https://docs.djangoproject.com/en/4.2/ref/models/fields foi utilizada para consultar exemplo de model, tipos de campos, entre outras informações.


### Banco de Dados

Foi utilizado o SQLLite e o [DB Browser](https://sqlitebrowser.org/) como gerenciador de banco de dados.
Para criação do model na pasta migrations, rodar o comando na pasta python:
```
python manage.py makemigrations
```

Posteriormente rodar o comando para criação do Banco de Dados:
```
python manage.py migrate
```

Esse comando criará o arquivo "db.sqlite3", na pasta venv.
Isso porque no arquivo "settings.py" no item DATABASES foi informado que seria utilizado o sqlite3.

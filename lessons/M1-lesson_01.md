# Aula 01 - Django: Templates e boas práticas 
Neste passo você vai aprender como utilizar Templates com Django e Boas práticas de programação. No final você será capaz de criar suas próprias aplicações web.

## Sobre o Django

O Django é um framework escrito em python, focado e orientado à conteúdo (content-driven). Abaixo estão alguns pontos que devem ser avaliados ao escolher fazer um projeto em Django:

* O Django já prove uma estrutura para uso de banco de dados.
* Facilidade nas construção de operações CRUD.
* Fácil aprendizagem para quem ja tem familiaridade com a linguagem Python.
* Feito para entregas rápidas com pouco código.

O Django utiliza a arquitetura MVT (Model View Template) para desenvolvimendo de aplicações:

* **M - Model:** Camada de abstração para manipular e estruturar os dados da aplicação web, contendo campos e comportamentos esseciais dos dados armazenados. Todo model é uma classe python subclasse de django.db.models.Model, e cada atributo do model representa um campo no banco de dados. Ao criar o model do Django automaticamente é disponibilizada uma API para abstração do banco de dados permitindo criar, recuperar, atualizar e deletar objetos (sem a necessidade de rescrever Queries).
* **V - View:** Função em Python que recebe uma requesição web e devolve uma resposta seja ela uma página HTML, um redirect, erro 404, json, imagens e etc.
* **T - Template:** Arquivo de texto que é usado para gerar qualquer formato baseado em texto como, XML, CSV e principalmente HTML. Contendo partes estáticas das saidas desejadas e algumas sintaxes especiais que descrevem como o conteúdo dinâmico será inserido nele, conhecida como DLT (Django Template Language), variáveis e tags que controlam a lógica do template.

---

O Django é um framework bem completo, trazendo soluções para as questões mais abordadas no desenvolvimento de aplicações web, autenticações, rotas, Object Relational Map (ORM) e até Migrations. Todos estes recursos ficam disponível diretamente no framework, fazendo os time de desenvolvimento ganhar em produtividade e garantindo aplicações performáticas.

DRY (Don't Repeat Yourself) é o princípio fundamental do Django, ou seja, nada de ficar repetindo códigos no seu projeto. Outro ponto fundamental é a segurança, onde o framework conta com recursos para proteção contra ataques como, SQL Injection, Cross Site Scripting (XSS), Cross Site Request Forguety (CSRF) e também Clickjacking.

## Projeto: Boas práticas

Para criar um projeto Django primeiro vamos preparar o ambiente. Os ponto iniciais são:

1. Instalar o Python em sua versão mais rescente.
2. Instalar o PIP em sua versão mais rescente.
3. Instalar o virtualenv em sua versão mais rescente.
4. Configurar um env para o projeto.
5. Instalar o Django isoladamente para o projeto.
6. Criar o projeto Django.
7. Criar o arquivo de requirements.txt.
8. Iniciar o server.

---

1. **Instalando o Python3**

Utilize o primeiro comando para instalar a versão mais rescente do Python3 e em seguida, utilize o comando "ln" para criar links simbólicos para a execução do python através de comandos "python" e/ou "py": 
```
$ sudo apt install python3 -y
$ sudo ln -s /usr/bin/python3 /usr/bin/python
$ sudo ln -s /usr/bin/python3 /usr/bin/py 
``` 

2. **Instalando o PIP**

Utilize o comando abaixo para instalar o python3-pip. Essa dependência é importante para o gerenciamento de pacotes isolatos em seus pacotes Django.
```
$ sudo apt install python3-django -y
```

3. **Instalando o virtualenv**

Instalar o virtualenv é crucial para o isolamento do pacotes e dependências do projeto. Execute o comando abaixo para instala-lo:
```
$ sudo apt install python3-virtualenv -y
```

4. **Configurando um ENV para o projeto**

Uma boa prática para a criação de um projeto Django é isolar todos e pacotes e dependências em um ambiente vitual python. É importante também armazenar todos os arquivos em um unico diretório. Para realizar esta tarefa execute os comandos abaixo:
```
$ mkdir django-app_python
$ cd django-app_python
$ virtualenv venv
```

OBS: O nome venv é uma convenção das boas práticas para a criação do ambiente virtual.

Ao criar o env agora você precisa executa-lo para começar a instalar as dependês do Django:
```
$ source venv/bin/activate
```

Pode-se confirmar a inicialização do ambiente virtual através da informação que aparece ao lado do seu usuário no terminal:
```
(venv) user@host $
```

5. **Instalando o Django**

Agora que vem o pulo do gato. Com o venv ativado vamos usar o PIP para instalar o django somente nesse ambiente virtual:
```
(venv) $ pip install django
```

A saída deve ser algo como:
```
Collecting django
  Downloading Django-4.2.7-py3-none-any.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 37.1 MB/s eta 0:00:00
Collecting asgiref<4,>=3.6.0
  Downloading asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.4.4-py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.2/41.2 kB 6.2 MB/s eta 0:00:00
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-4.2.7 sqlparse-0.4.4
```

6. **Criando o projeto Django**

Para criar um projeto Django é muito simples, basta usar o comando django-admin com a seguinte sintaxe "$ django-admin startproject <name> .". O nome do projeto hoje também é uma convensão, variando entre "config" e "setup":
```
(venv) $ django-admin startproject setup 
```

7. **Criando o arquivo de requirements**

Para criar o arquivo de requirement também vamos utilizar o PIP. No começo do projeto é facil manipular e atualizar esse arquivo manualmente, porém ao decorrer do desenvolvimento as chances de se ter informações incorretas ou ausentes são grandes, por isso o PIP tem uma ação chamada FREEZE que lista todas as dependências do projeto. Para criar o arquivo para direciona a saída conforme o comando abaixo:
```
(venv) $ pip freeze > requirements.txt
```

OBS: Esse comando deve ser utilizado toda vez que o pip install for rodado no seu ambiente virtual, para manter o arquivo de requirements atualizado.

8. **Inciiando o servidor**

Agora vamos iniciar o servidor virtual para acessar nossa aplicação com um dos dois comandos (de acordo):
```
(venv) $ python manage.py runserver
(venv) $ py manage.py runserver
```

### Conclusão

A utilização de ambientes virtuais em projetos Python é uma prática padrão no desenvolvimento de software com a linguagem. O consenso da comunidade Python de que ambientes virtuais são uma ótima prática levou à criação de vários projetos com o objetivo de oferecer versões alternativas de ambientes virtuais e novas formas de gerenciá-los.

A seguir temos alguns exemplos de ambientes virtuais e ferramentas relacionadas mais utilizadas no mercado:

* **venv:** É o ambiente virtual “padrão” do Python e sua grande vantagem é já vir instalado como um módulo na linguagem a partir da versão 3.3. Se trata de um subset (parte menor) da ferramenta virtualenv.
* **Virtualenv:** É uma ferramenta feita especificamente para a criação de ambientes virtuais e precede a criação da venv, sendo um superset (parte maior) dela. Algumas de sua principais vantagens sobre a venv são:
    * Maior velocidade, graças ao método app-data seed;
    * Pode criar ambientes virtuais para versões arbitrárias do Python instaladas na máquina;
    * Pode ser atualizado utilizando a ferramenta pip;
    * Possui uma Programmatic API, capaz de descrever um ambiente virtual sem criá-lo.
* **Conda:** É uma alternativa não apenas às ferramentas de ambiente virtuais já citadas, mas ao instalador de pacotes pip também. Possui um escopo mais centrado na área de ciência de dados e possui a capacidade de instalar pacotes fora do ecossistema do Python.
* **Virtualenvwrapper:** É uma extensão do projeto Virtualenv que torna a criação, deleção e gerenciamento geral dos ambientes virtuais mais fácil. Uma grande vantagem de sua utilização é a organização de todos os ambientes virtuais utilizados em um só lugar, além de facilitar os comandos de CLI.
* **Poetry:** É uma ferramenta para gerenciamento de dependências e pacotes do Python. Através do Poetry é possível declarar quais pacotes um projeto necessita para funcionar, de forma parecida ao requirements.txt, porém, de forma determinística.
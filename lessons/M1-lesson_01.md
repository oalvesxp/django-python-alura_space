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
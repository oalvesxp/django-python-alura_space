# Aula 05 - Django: Templates e boas práticas
Nessa aula vamos aplicar a correção do link de páginas HTML e também vamos aplicar o conceito DRY (Don't repeat yourself) em nosso código.</br>

Os passos a serem executados são:

1. Tageamento das rotas e embedar o código Django nos Links HTML.
2. Criação e configuração do arquivo base.html
3. Criação e confiuguração de um arquivo parcial para o Footer
4. Criação e configuração de um arquivo parcial para o Menu
5. Conclusão do Curso.

---

1. **Tageando as rotas e configurando os links**

Primeiro vamos corrigir o erro de maneira simples. O Django não reconhece links HTML, para navegar entre as páginas é uma boa prática utilizar as rotas para definir os 'links HTML', podemos fazer isso através de tag_names, como o código abaixo demonstra (name='nametag_da_pagina'):
```
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
```

Agora basta inserir o código embedando os links com código Django, usando o {$ url 'nametag_da_pagina' %}:
```
                <a href="{% url 'index' %}"><img src="{% static '/assets/ícones/1x/Home - ativo.png' %}"> Home</a>

                                                <a href="{% url 'imagem' %}">
```

---

2. **Criando o arquivo de base.html**

Agora este é o passo mágico do Django. Vamos criar um template universal para o código que se repete no HTML, como por exemplo, tags HTML, HEAD, TITLE, BODY e as META TAGS. Isso é excelente porque irá poupar tempo de desenvolvimento, performance e tornar o processo de melhorias e modificações no código muito mais eficiente.</br>
Para isso vamos executar:
```
(venv) $ vim templates/galeria/base.html
``` 

**Obs:** O nome 'base.html' para o arquivo é uma convenção da comunidade.


E inserir o código base do HTML que se repete em todas as páginas:
```
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alura Space</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static '/styles/style.css' %}">
</head>

<body>

    {% block content %}{% endblock %}

</body>
</html>
```

Lembrando que essa página também precisa carregar os arquivos estáticos devido as meta tags, então coloque o código Djando apra o load static.

Agora devemos extender esse arquivo em nossas páginas HTML para podermos carregar seu conteúdo para isso vamos modificar as páginas inserindo:
```
{% extends 'galeria/base.html' %}
{% load static %}

{% block content %}

    <!-- conteúdo das páginas -->

{% endblock%}
```

Lembrando que o base.html possui o código HTML até a tag BODY e tudo após o fechamento da mesma, portanto devemos abrir o bloco de conteúdo antes de todo o conteúdo de cada página e fecha-lo após o final do mesmo.

---

3. **Criando o arquivo parcial para Footer**

Agora vamos deixar nosso código menos repetitivo separando o footer em um arquivo template. No base.html, só colocamos o que é estrutura do HTML padrão, demais conteúdos que são inseridos entre as tags BODY, indicamos em outros arquivos chamados de parciais. Que por sua vez os nomes se iniciam com _ , de acordo com a convenção da comunidade.</br>
Para realizar esta tarefa vamos criar o diretório e o arquivo _footer.html
```
(venv) $ mkdir templates/galeria/partials
(venv) $ vim templates/galeria/partials/_footer.html
```

Insira o conteúdo do footer dentro do arquivo parcial:
```
{% load static %}
    <footer class="rodape">
        <div class="rodape__icones">
            <a href="https://twitter.com/AluraOnline" target=”_blank” >
                <img src="{% static '/assets/ícones/1x/twitter.png' %}" alt="ícone twitter">
            </a>
            <a href="https://www.instagram.com/aluraonline/" target=”_blank” >
                <img src="{% static '/assets/ícones/1x/instagram.png' %}" alt="ícone instagram">
            </a>
        </div>
        <p class="rodape__texto">Desenvolvido por Alura</p>
    </footer>
```

E agora dentro da base.html vamos incluir este arquivo parcial de acordo com sua posição estrutural do projeto (após o bloco de conteúdo).
```
<body>

    {% block content %}{% endblock %}
    {% include 'galeria/partials/_footer.html' %}

</body>
```

Lembre-se sempre de remover todo o cógigo repetido das outras páginas do site.

4. **Criando o arquivo parcial para Menu**

Vamos repetir o processo para o menu do site que se repete em ambas as páginas. Vamos criar agora um arquivo chamado _menu.html dentro do partials:
```
(venv) $ vim templates/galeria/partials/_menu.html
```

E inserir o código do menu no arquivo parcial:
```
{% load static %}
<div class="pagina-inicial">
    <header class="cabecalho">
        <img src="{% static '/assets/logo/Logo(2).png' %}" alt="Logo da Alura Space" />
        <div class="cabecalho__busca">
            <div class="busca__fundo">
                <input class="busca__input" type="text" placeholder="O que você procura?">
                <img class="busca__icone" src="{% static '/assets/ícones/1x/search.png' %}" alt="ícone de search">
            </div>
        </div>
    </header>
    <main class="principal">
        <section class="menu-lateral">
            <nav class="menu-lateral__navegacao">
                <a href="{% url 'index' %}"><img src="{% static '/assets/ícones/1x/Home - ativo.png' %}"> Home</a>
                <a href="#"><img src="{% static '/assets/ícones/1x/Mais vistas - inativo.png' %}"> Mais vistas</a>
                <a href="#"><img src="{% static '/assets/ícones/1x/Novas - inativo.png' %}"> Novas</a>
                <a href="#"><img src="{% static '/assets/ícones/1x/Surpreenda-me - inativo.png' %}"> Surpreenda-me</a>
            </nav>
        </section>
```

Por fim incluir o novo arquivo parcial no base.html de acordo com sua posição estrutural da página (antes do bloco de conteúdo):
```
<body>

    {% include 'galeria/partials/_menu.html' %}
    {% block content %}{% endblock %}
    {% include 'galeria/partials/_footer.html' %}

</body>
```

---

5. **Conclusão do curso**

Este foi o resultado do que foi aprendido neste curso de Django: Templates e boas práticas. Criamos e implantamos uma aplicação da AluraSpace com Django priorisando a segurança de dados sessíveis, boas práticas de programação e utilizando o conceito DRY para otimizar e simplificar o código.
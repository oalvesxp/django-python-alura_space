# Aula 02 - Django: persistência de dados e Admin 
Entender como lidar com dados em uma aplicação Django utilizando banco de dados


Notas para quem deseja pegar o projeto a partir deste commit para replicar.</br>
Use o comando, pip para instalar todas as dependências a partir do arquivo de requirements.txt:
```
(venv) $ pip install -r requirements.txt
```

## Projeto: persistência de dados e Admin

Vamos aprender como lidar com os dados dentro do nosso site alura_space, juntamente com a persistência destes dados em um banco, aprendendo também a manipula-los através de um painel admin.

Passos a serem realizados:

1. Entender como os dados são manipulados pelo Django.
2. Criar as classes para os dados manipulados.
3. Realizar a migração para aplicar a tabela no banco de dados.
4. Inserindo dados no banco
5. 

## Execução

1. Entendendo como o dados são manipulados

O Django facilita a manipulação de dados de diversas maneiras, sendo elas:

* **Modelos (Models):** Os modelos representam as tabelas do banco de dados. Você define um modelo para cada tipo de dado que deseja armazenar. Por exemplo, se estiver construindo um blog, você pode ter um modelo para os posts.
* **Migrações (Migrations):** Depois de definir seus modelos, o Django cria um esquema de banco de dados inicial. Quando você faz alterações nos modelos, como adicionar um novo campo, você cria migrações para aplicar essas alterações ao banco de dados.
* **Administração (Admin):** O Django oferece uma interface administrativa automática para interagir com os dados do seu aplicativo. Você pode usar o painel de administração para adicionar, editar ou excluir registros do banco de dados sem escrever código manualmente.
* **Consulta (QuerySet):** Para recuperar dados do banco de dados, você usa consultas. O Django fornece uma API de consulta poderosa chamada QuerySet, que permite filtrar, ordenar e manipular dados de maneira flexível.
* **Formulários (Forms):** Para lidar com a entrada de dados do usuário, você pode criar formulários no Django. Eles facilitam a validação e o processamento dos dados enviados pelos usuários.
* **Views e Templates:** As views processam solicitações do usuário e interagem com os modelos para obter ou salvar dados. Os templates são usados para renderizar as páginas HTML, exibindo os dados aos usuários.

Esses são os componentes principais do Django para manipulação de dados.</br>
Vamos ver na prática como isso se aplica:

Para manipular os primeiros dados vamos criar um dicionário de dados (uma lista) para definir o Nome e Legenda dos cards da nossa index.html. Modifique o arquivo views.py dentro do app galeria/:
```
def index(request):
    
    dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org/ NASA / James Web"},
    2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org/ NASA / Hubble"},
    }

    return render(request, 'galeria/index.html', {"cards": dados})
```

Agora para que o Django entregue nosso conteúdo vamos modificar o HTML para que ele receba as informações do views.py:
```
                    {% for foto_id, info in cards.items %}
                    <div class="cards">
                        <h2 class="cards__titulo">Navegue pela galeria</h2>
                        <ul class="cards__lista">
                            <li class="card">
                                <a href="{% url 'imagem' %}">
                                    <img class="card__imagem" src="{% static '/assets/imagens/galeria/carina-nebula.png' %}" alt="foto">
                                </a>
                                <span class="card__tag">Estrelas</span>
                                <div class="card__info">
                                    <p class="card__titulo">{{ info.nome }}</p>
                                    <div class="card__texto">
                                        <p class="card__descricao">{{ info.legenda }}</p>
                                        <span>
                                            <img src="{% static '/assets/ícones/1x/favorite_outline.png' %}" alt="ícone de coração">
                                        </span>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                    {% endfor %}
```

Aqui usamos um FOR para repetir o nosso código HTML a cada item que for inserido dentro da nossa lista, exibindo seus valores nos respectivos campos.</br>
Ainda sim este não é o modo adequado de se fazer essa manipulação de dados. Vamos melhorar isso no proximo passo.

---
2. Criar classe para os dados

Para que o Django manipule e torne os dados persistentes é necessário criar uma classe no arquivo models.py.</br>
Essas classes são como objetos que serão convertidos em tabelas dentro do banco de dados, sem a necessidade de escrevermos uma linha de código SQL.

Vamos criar nossa classe Fotografia para obter os dados que fizemos em nossa lista:
```
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
```

Uma boa prática é criar uma função que vai retornar o próprio valor da classe para validar o funcionamento:
```
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
```

---
3. Realizando as migrações

Vamos aplicar todas as nossa classes no banco de dados através das migrations. Para que o Django identifique o e gere a nova tabela no banco.</br>
Primeiro execute o comando abaixo para validar que tudo está correto para a migração ser executada:
```
(venv) $ python manage.py makemigrations
```

Isso vai gerar um arquivo dentro do galeria/migrations que obtém todas as informações das migrações que serão realizadas.</br>
Agora faça a migração com o comando abaixo
```
(venv) $ python manage.py migrate
```

O retorno deve ser algo como:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, galeria, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
```

Tudo isso é possível graças a técnologia ORM (Object-Relational-Mapper) leia o arquivo ORM-info.md para ler o artigo e obter mais informações.

---

4. Inserindo dados no banco

Para inserir dados no banco vamos utilizar um terminal interativo do python para executar um comando de insersão.</br>
Para abrir o terminal vamos usar o comando:
```
(venv) $ python manage.py shell
```

Agora vamos importar a nossa classe para criar nosso primeiro objeto:
```
>>> from galeria.models import Fotografia
```

Em seguida vamos inserir um objeto utilizando a seguinte sintaxe:
```
>>> foto = Fotografia(nome="Nebulosa de Carina", legenda="webbtelescope.org/ NASA / James Web", foto="carina-nebula.png")
```

Agora precisamos salvar as informações no banco de dados. Utilize o comando abaixo:
```
>>> foto.save()
```

Para validar podemos utilizar um QuerySet para buscar os dados cadastrados no banco:
```
>>> Fotografia.objects.all()
```

O retorno deve ser algo como:
```
<QuerySet [<Fotografia: Fotografia [nome=Nebulosa de Carina]>]>
```

OBS: é para isso que serve nossa função com seft.nome, para quando os dados forem recuperados no banco de dados, ele traga por default o nome de cada objeto.

Para aprender mais sobre os models, leia a documentação: https://docs.djangoproject.com/pt-br/4.1/topics/db/models/

---
Outra boa prática é importar o arquivo de apps.py do app ao invés de importar o app por si só. Isso é definido lá no arquivo settings.py. 

Exemplo de como estava antes:
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'galeria',
]
```

Exemplo de como deveria ser importando o arquivo apps.py:
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'galeria.apps.GaleriaConfig',
]
```

Isso garante que modificações no apps.py também serão importadas diretamente no settings do Django.
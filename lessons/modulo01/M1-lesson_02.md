# Aula 02 - Django: Templates e boas práticas
Vamos garantir uma maior segurança na aplicação através da utilização do pacote python-dotenv. Aprendemos que dados sensíveis como a SECRET_KEY, devem ser armazenados em em um arquivo específico ao ambiente atual de desenvolvimento.

Passos a serem realizados:

1. Criar um arquivo para variáveis de ambiente.
2. Instalação do pacote python-dotenv
3. Importação do pacote dotenv e os no arquivo settings.py
4. Importação da SECRET_KEY através de uma variável de ambiente.
5. Configuração do arquivo .gitignore.


## Execução

1. **Criação do arquivo .env**

Crie um novo arquivo chamado .env no diretório raiz da aplicação para armazenar a SECRET_KEY.
```
(venv) $ vim .env
```

Conteúdo do arquivo .env:
```
SECRET_KEY=<chave aleatória>
```

2. **Instalação do python-dotenv**

Instale o pacote python-dotenv para a importação das variáveis de ambiente no arquivo de settings.py:
```
(venv) $ pip install python-dotenv
```

Não se esqueça de atulizar o arquivo de requirements:
```
(venv) $ pip freeze > requirements.txt
```

3. **Importando as dependencias no settings.py**

Importe os pacotes python-dotenv e os no arquivo settings.py:
```
from pathlib import os
from dotenv import load_dotenv
```

4. **Importando a variável de ambiente no settings.py**

Importe a SECRET_KEY do arquivo .env e coloque dentro da variável SECRET_KEY no arquivo settings.py
```
load_dotenv()
SECRET_KEY = str(os.getenv('SECRET_KEY'))
```

5. **Configurando o arquivo .gitignore**

Gere um arquivo .gitignore no diretório raiz do projeto. O conteúdo do arquivo pode ser gerado automáticamente por um site chamado https://gitignore.io. Basta acessa-lo e inserir a tecnologia utilizada para gerar o conteúdo de acordo com as convenções da comunidade. Ao gerar todo o conteúdo copie-o e cole no arquivo criado .gitignore.
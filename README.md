# Projeto API de Clientes com Flask

Esta é uma simples API RESTful para gerenciamento de clientes, construída com Flask e SQLite.

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados na sua máquina:

1.  **Python 3.8 ou superior**:

      * Acesse [python.org](https://www.python.org/downloads/) para baixar e instalar.
      * **Importante (para Windows)**: Durante a instalação, marque a caixa que diz **"Add Python to PATH"**.

2.  **Git**:

      * Acesse [git-scm.com](https://git-scm.com/downloads) para baixar e instalar.

## Guia de Instalação e Execução

Siga estes passos no seu terminal (como Git Bash, PowerShell, ou o terminal do Linux/macOS) para configurar e rodar o projeto localmente.

### 1\. Clonar o Repositório

Primeiro, clone o repositório do projeto para a sua máquina local.

```bash
git clone https://github.com/GhabryelHenrique/crud-api.git
```

### 2\. Navegar para a Pasta do Projeto

Entre na pasta que foi criada pelo comando `git clone`.

```bash
cd crud-api
```

### 3\. Criar e Ativar o Ambiente Virtual (`venv`)

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outros projetos Python.

**a) Crie o ambiente:**

```bash
python -m venv venv
```

**b) Ative o ambiente:**

  * **No Windows:**

    ```bash
    .\venv\Scripts\activate
    ```

  * **No macOS e Linux:**

    ```bash
    source venv/bin/activate
    ```

*Após ativar, o nome `(venv)` aparecerá no início da linha do seu terminal.*

### 4\. Instalar as Dependências

Com o ambiente virtual ativo, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt` com um único comando.

```bash
pip install -r requirements.txt
```

*Este comando irá instalar o Flask e todas as suas dependências na versão exata que você usou, garantindo que o ambiente do outro dev seja idêntico ao seu.*

### 5\. Executar a Aplicação

Agora que tudo está configurado, inicie o servidor Flask. O banco de dados (`minha_api.db`) e a tabela `customers` serão criados automaticamente na primeira vez que você executar.

```bash
python seu_arquivo.py
```

*(Substitua `seu_arquivo.py` pelo nome real do seu script principal, como `app.py`)*

O terminal deverá exibir uma saída parecida com esta:

```
Tabela 'customers' não encontrada. Criando tabela...
Tabela 'customers' criada com sucesso.
 * Serving Flask app 'seu_arquivo'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 6\. Testar a API

A API agora está rodando localmente na porta 5000. Você pode testar os endpoints:

  * **GET /customers**: Abra seu navegador e acesse [http://127.0.0.1:5000/customers](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:5000/customers) para ver a lista de clientes (estará vazia no início).

  * **POST /customers**: Use uma ferramenta como [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/) ou o comando `curl` para criar um novo cliente:

    ```bash
    curl -X POST http://127.0.0.1:5000/customers \
         -H "Content-Type: application/json" \
         -d '{"FirstName": "Maria", "LastName": "Silva", "Email": "maria.silva@example.com"}'
    ```

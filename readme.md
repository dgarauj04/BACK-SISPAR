# 📊 Sistema de Gestão de Reembolsos e Colaboradores

Este projeto é uma aplicação backend desenvolvida com **Python**, **Flask** e **SQLAlchemy**, criada para gerenciar colaboradores e seus pedidos de reembolso corporativo. O sistema permite cadastro, autenticação, atualização e exclusão de colaboradores, além de gerenciar solicitações de reembolso, seguindo boas práticas REST e documentação via **Swagger (Flasgger)**.

---

## 📌 Tecnologias Utilizadas

- Python 3.12+
- Flask
- SQLAlchemy
- Flasgger (Swagger para APIs REST)
- Werkzeug (hash de senha)
- SQLite (ou outro banco compatível)

---

## 📖 Funcionalidades

### 🔹 Colaborador

- **Cadastrar colaborador** (`POST /colaborador/cadastrar`)
- **Login de colaborador** (`POST /colaborador/login`)
- **Listar todos os colaboradores** (`GET /colaborador/todos-colaboradores`)
- **Atualizar dados do colaborador** (`PUT /colaborador/atualizar/<id_colaborador>`)
- **Deletar colaborador** (`DELETE /colaborador/deletar/<id_colaborador>`)

### 🔸 Reembolso

- **Solicitar reembolso** (`POST /refunds/new`)
- **Buscar reembolso pelo número de prestação** (`GET /refunds/get-refunds/<num_prestacao>`)
- **Atualizar reembolso** (`PUT /refunds/update/<id_reembolso>`)
- **Deletar reembolso** (`DELETE /refunds/delete/<id_reembolso>`)

---

## 📋 Estrutura de Diretórios
```
venv/
src/
├── app.py
├── __init_.py
├── model/
│  ├── __init_.py
│  ├── colaborador_model.py
│  └── reembolso_model.py
├── controller/
│  ├── colaborador_controller.py
│  └── reembolso_controller.py
├── docs/
│ ├── colaborador/
│ │  ├── cadastrar.yml
│ │  |── atualizar.yml
│ │  |── deletar.yml
│ ├  |── todos-colaboradores.yml
| |  └── login.yml
│ └── reembolso/
│    ├── registrar.yml
│    ├── buscar_reembolso.yml
│    ├── atualizar_reembolso.yml
│    └── apagar.yml
|── security/
|   └── security.py
└── tests
    ├── __init_.py
    └── test_app.py
.env
config.py
requirements.txt
run.py
```
---
## 📦 Como Executar o Projeto atraves do link render
1. **Acesse o link render**
```
https://back-sispar.onrender.com
```
2. **Espere alguns segundos para que o servidor seja iniciado e apareça a mensagem:**
"Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
3. **Após isso, para você poder acessar a documentação Swagger adicionando "/apidocs" no final do link:**
```
https://back-sispar.onrender.com/apidocs
```

## 📦 Como Executar o Projeto pelo clone do repositório

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
4. **Execute a aplicação**
```bash
python run.py
```
5. **Acesse a documentação Swagger**
```bash
No navegador, vá até:
http://localhost:5000/apidocs
```

---
🔒 Segurança
As senhas dos colaboradores são armazenadas utilizando hashing com Werkzeug e verificação segura no login.

---
📑 Documentação via Swagger
A documentação das rotas está definida através de arquivos .yml na pasta docs/, utilizando o Flasgger, permitindo testes diretamente pela interface web.

---
🎨 Autor
Desenvolvido por Douglas Araujo com base no curso Vai na Web e com os grandes instrutores Karynne e Samuel. 

---
📌 Observação
Este projeto faz parte de um projeto de aprendizado Full Stack com padrão MVC, e tem como objetivo o gerenciamento de solicitações de reembolso de colaboradores para empresas.
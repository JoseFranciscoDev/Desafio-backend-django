# 📌 API de Gerenciamento de Tarefas

## 📖 Sobre
Esta API permite o gerenciamento de tarefas e de usuários. Com ela, é possível criar, listar, atualizar e excluir tarefas, além de filtrar por status.

## 🚀 Tecnologias Utilizadas
- Python 3
- Django Rest Framework
- SQLite
- Simple JWT

---

## 📂 Instalação e Configuração

### 🔧 1. Clone o repositório
```sh
git clone https://github.com/JoseFranciscoDev/Desafio-backend-django.git
cd desafio-backend-django
```

### 🐍 2. Crie e ative um ambiente virtual
```sh
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/macOS:
source venv/bin/activate
```

### 📦 3. Instale as dependências
```sh
pip install -r requirements.txt
```

### 🛠️ 4. Execute as migrações do banco de dados
```sh
python manage.py migrate
```

### 🔑 5. Crie um superusuário para acessar o Django Admin
```sh
python manage.py createsuperuser
```

### ▶️ 6. Inicie o servidor local
```sh
python manage.py runserver
```
A API estará disponível em `http://127.0.0.1:8000/`

---
# 📡 Endpoints

## 📍 Autenticação

| Método | Rota                | Descrição                                                         |
|--------|----------------------|-------------------------------------------------------------------|
| POST   | /api/token/           | Gera um token de acesso (necessário para autenticar as requisições) |
| POST   | /api/token/refresh/   | Atualiza o token de acesso. Usado quando o token expira.          |

A autenticação é feita utilizando o Simple JWT, e você precisará do token gerado para acessar endpoints protegidos.

---

## 📍 Usuários

| Método | Rota                       | Descrição                                                      |
|--------|----------------------------|---------------------------------------------------------------|
| GET    | /api/users/                 | Lista todos os usuários registrados no sistema.               |
| GET    | /api/users/id/            | Retorna as informações de um usuário específico, identificado pelo id. |
| POST   | /api/users/                 | Cria um novo usuário. Você precisará enviar os dados do usuário no corpo da requisição. |
| DELETE | /api/users/id/            | Remove um usuário específico, identificado pelo id.         |

Os endpoints de usuários permitem gerenciar as informações de usuários, seja para visualizar, adicionar ou remover.

---

## 📍 Tarefas

| Método | Rota                                    | Descrição                                                      |
|--------|-----------------------------------------|---------------------------------------------------------------|
| GET    | /api/users/user_id/tasks/             | Lista todas as tarefas de um usuário, identificadas pelo user_id. |
| GET    | /api/users/user_id/tasks/?status=<status> | Filtra as tarefas do usuário com base no status (pendente, concluída, etc.). Exemplo de uso: status=pendente. |
| POST   | /api/tasks/                             | Cria uma nova tarefa. Envie as informações da tarefa no corpo da requisição. |
| PATCH  | /api/tasks/id/                        | Atualiza uma tarefa específica, identificada pelo id. O corpo da requisição deve conter os dados a serem atualizados. |
| DELETE | /api/tasks/id/                        | Deleta uma tarefa específica, identificada pelo id.         |

Os endpoints de tarefas permitem o gerenciamento completo das tarefas de um usuário, incluindo a filtragem por status, criação, atualização e exclusão.

---

## 📮 Contribuição
Sinta-se à vontade para contribuir! Faça um **fork**, crie um **branch**, implemente suas melhorias e envie um **pull request**.

---

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

---

Feito com ❤️ por [José Francisco](https://github.com/JoseFranciscoDev).


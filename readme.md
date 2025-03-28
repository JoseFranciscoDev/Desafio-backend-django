# 📌 API de Gerenciamento de Tarefas

## 📖 Sobre
Esta API permite o gerenciamento de tarefas de usuários. Com ela, é possível criar, listar, atualizar e excluir tarefas, além de filtrar por status.

## 🚀 Tecnologias Utilizadas
- Python 3
- Django Rest Framework
- SQLite (ou outro banco de dados configurável)

---

## 📂 Instalação e Configuração

### 🔧 1. Clone o repositório
```sh
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
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

## 📡 Endpoints

### 📍 Autenticação
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/api/token/` | Gera um token de acesso |
| `POST` | `/api/token/refresh/` | Atualiza o token de acesso |

### 📍 Usuários
| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/users/` | Lista todos os usuários |
| `GET` | `/api/users/<id>/` | Busca um usuário pelo ID |
| `POST` | `/api/users/create/` | Cria um novo usuário |
| `DELETE` | `/api/users/delete/<id>/` | Remove um usuário |

### 📍 Tarefas
| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/users/<user_id>/tasks/` | Lista todas as tarefas de um usuário |
| `GET` | `/api/users/<user_id>/tasks/?status=pendente` | Filtra tarefas pelo status |
| `POST` | `/api/tasks/create/` | Cria uma nova tarefa |
| `PATCH` | `/api/tasks/<id>/update/` | Atualiza uma tarefa |
| `DELETE` | `/api/tasks/<id>/delete/` | Deleta uma tarefa |

---

## 📮 Contribuição
Sinta-se à vontade para contribuir! Faça um **fork**, crie um **branch**, implemente suas melhorias e envie um **pull request**.

---

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

---

Feito com ❤️ por [Seu Nome](https://github.com/seu-usuario).


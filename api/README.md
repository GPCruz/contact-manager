# Projeto API

## Visão Geral

Este projeto é uma API desenvolvida com Flask e SQLAlchemy, utilizando boas práticas de programação e seguindo os princípios SOLID. A arquitetura do projeto é organizada de forma a manter uma estrutura limpa e legível, facilitando a manutenção e a escalabilidade.

## Estrutura do Projeto

root/
│
├── controllers/
│   └── user_controller.py
├── db/
│   ├── abstractions/
│   │   └── base.py
│   ├── models/
│   │   ├── contact_model.py
│   │   └── user_model.py
│   ├── schemas/
│   └── db_driver.py
├── services/
│   └── user_service.py
├── tests/
│   └── test_user_service.py
├── __init__.py/
├── .funcignore/
├── .gitignore/
├── config.py/
├── db.sqlite3/
├── function_app.py/
├── host.json/
├── README.md/
├── requirements.txt/
└── routes.py

## Requisitos

- Python 3.8+
- Flask
- Flask-CORS
- SQLAlchemy
- Pydantic
- Azure Functions

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
3. Configure o banco de dados no arquivo [`config.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Ff%3A%2FProjetos%2Fcontact-manager%2Fapi%2Fconfig.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "f:\Projetos\contact-manager\api\config.py").

## Executando a Aplicação

Para executar a aplicação, utilize o comando:

```sh
flask run
```

Princípios SOLID
Este projeto segue os princípios SOLID para garantir uma arquitetura robusta e de fácil manutenção:

Single Responsibility Principle: Cada módulo tem uma única responsabilidade.
Open/Closed Principle: Os módulos são abertos para extensão, mas fechados para modificação.
Liskov Substitution Principle: As subclasses devem ser substituíveis por suas superclasses.
Interface Segregation Principle: Muitas interfaces específicas são melhores do que uma única interface geral.
Dependency Inversion Principle: Dependa de abstrações, não de implementações concretas.
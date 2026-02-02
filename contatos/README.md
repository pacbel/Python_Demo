# Contatos API

## Visão geral
Este projeto é uma API REST simples construída com Python 3.14, Django 6 e Django REST Framework. O objetivo é gerenciar contatos contendo **nome** e **telefone**, persistidos em um banco MariaDB/MySQL local. A documentação interativa é gerada pelo **drf-yasg** (Swagger/Redoc).

A estrutura foi mantida enxuta para atender exclusivamente ao CRUD de contatos:

- `contatos_api/` contém modelo, serializer, viewset e rotas da API.
- `contatos/` contém as configurações do projeto Django, incluindo o backend customizado para suportar MariaDB 10.4.
- `docs` disponíveis via Swagger/Redoc facilitam o teste dos endpoints.

---

## Pré-requisitos
1. **Python** 3.14 instalado (já em uso neste ambiente).
2. **MariaDB 10.4** (ou MySQL) em `localhost`, usuário `root` sem senha.
3. Biblioteca `pip` para instalar dependências (já utilizada).

---

## Instalação e configuração

1. **Instalar dependências Python** (executar no diretório `c:\Drive\Google\Python\contatos`):
   ```powershell
   python -m pip install -r requirements.txt
   ```
   > Caso o `requirements.txt` não exista, use o comando manualmente: `python -m pip install django djangorestframework pymysql drf-yasg`.

2. **Criar o banco** (no terminal do MariaDB):
   ```sql
   CREATE DATABASE contatos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **Aplicar migrations**:
   ```powershell
   python manage.py migrate
   ```

4. **(Opcional) Criar superusuário** para acessar `/admin/`:
   ```powershell
   python manage.py createsuperuser
   ```

---

## Executando o projeto
```powershell
python manage.py runserver
```
A API ficará disponível em `http://127.0.0.1:8000/`.

Endpoints principais:
- `POST /api/contatos/` — cria novo contato.
- `GET /api/contatos/` — lista contatos.
- `GET /api/contatos/{id}/` — detalhe.
- `PUT /api/contatos/{id}/` — substitui contato.
- `PATCH /api/contatos/{id}/` — atualiza parcialmente.
- `DELETE /api/contatos/{id}/` — remove contato.

Todos os endpoints utilizam JSON no corpo das requisições.

---

## Documentação interativa
Com o servidor ativo:
- Swagger UI: `http://127.0.0.1:8000/docs/swagger/`
- Redoc: `http://127.0.0.1:8000/docs/redoc/`
- Esquema JSON: `http://127.0.0.1:8000/docs/swagger.json`

Em Swagger, informe os dados no editor JSON (ex.: `{ "nome": "Maria", "telefone": "11999999999" }`).

---

## Testando via PowerShell

### Criar contato
```powershell
curl -Method POST http://127.0.0.1:8000/api/contatos/ `
     -ContentType "application/json" `
     -Body '{"nome":"João","telefone":"11999990000"}'
```

### Atualizar contato
```powershell
curl -Method PATCH http://127.0.0.1:8000/api/contatos/1/ `
     -ContentType "application/json" `
     -Body '{"telefone":"11888887777"}'
```

### Remover contato
```powershell
curl -Method DELETE http://127.0.0.1:8000/api/contatos/1/
```

---

## Limpeza
Se precisar reiniciar o banco:
```sql
DROP DATABASE contatos_db;
CREATE DATABASE contatos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## Estrutura simplificada
```
contatos/
├── contatos/
│   ├── db_backends/        # Backend custom para MariaDB 10.4
│   ├── settings.py         # Configurações principais
│   └── urls.py             # Rotas gerais + docs
├── contatos_api/
│   ├── models.py           # Modelo Contact
│   ├── serializers.py      # ContactSerializer
│   ├── views.py            # ContactViewSet
│   └── urls.py             # Rotas da API
├── manage.py
└── README.md (este arquivo)
```

---

## Próximos passos sugeridos
1. Implementar autenticação caso deseje restringir acesso.
2. Adicionar testes automatizados em `contatos_api/tests.py`.
3. Configurar deploy (Docker, ambientes na nuvem, etc.) conforme necessidade.


URL Produção Teste : https://internos-python.cyunin.easypanel.host/docs/swagger/
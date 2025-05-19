# Redis com Python

Projeto simples e didático feito com Python que demonstra como integrar o Redis com o SQLite para otimizar o acesso, armazenamento e criação de dados.

## 📌 Sobre o projeto

Este projeto tem como objetivo demonstrar o uso do Redis como cache em conjunto com o banco de dados SQLite. A lógica principal é:

- Tentar buscar a informação primeiro no Redis;
- Caso não exista, buscar no SQLite;
- Se encontrada no SQLite, armazená-la temporariamente no Redis;
- Também é possível **criar novos registros** no banco de dados SQLite e armazenar temporariamente no Redis.

Essa abordagem simula um cenário comum em aplicações reais que utilizam cache para reduzir a carga no banco de dados e acelerar consultas.

## 🚀 Como executar

### Pré-requisitos

- Python 3.8 ou superior
- Redis instalado e rodando localmente
- SQLite (já incluso no Python)

### Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/taleshmm/RedisWithPython.git
cd RedisWithPython
````

2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

> Se não houver `requirements.txt`, instale manualmente:
>
> ```bash
> pip install redis flask pytest
> ```

### Configuração necessária

#### 🔹 Banco de dados SQLite

Você deve **criar seu próprio arquivo de banco de dados SQLite** (por exemplo: `db.sqlite3`) e configurar a conexão diretamente no código, onde for feita a chamada `sqlite3.connect()`.

> Exemplo:
>
> ```python
> conn = sqlite3.connect('db.sqlite3')
> ```

Crie uma tabela com a estrutura, como:

```sql
CREATE TABLE IF NOT EXISTS 'products' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL,
    'price' FLOAT NOT NULL,
    'quantity' INTEGER NOT NULL
);
```

#### 🔹 Redis

O Redis deve estar rodando localmente (`localhost:6379`). Caso use outro host ou porta, ajuste no trecho de conexão Redis:

```python
redis.StrictRedis(host='localhost', port=6379, db=0)
```

## 💡 Funcionalidades

* Buscar dados no Redis (cache)
* Buscar dados no SQLite (persistência)
* Armazenar dados encontrados no SQLite dentro do Redis
* Criar novos registros no SQLite e adicionar no Redis (temporariamente)

## 📚 Tecnologias utilizadas

* Python
* Redis
* SQLite
* Flask
* Pytest

## 🎯 Objetivos

* Estudar e praticar uso de cache com Redis
* Integrar Redis com SQLite de forma simples
* Simular comportamentos comuns em sistemas reais
* Aplicar conceitos de leitura, escrita e invalidação de cache


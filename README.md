# FastAPI Template

Template repository for starting FastAPI projects, including:

- Async FastAPI app structure (src/ layout)
- Async SQLAlchemy ORM + Alembic migration
- OpenID authentication integration
- Pre-configured User entity in all layers
- Environment management via uv
- Pre-commit hooks: Ruff (lint + format), MyPy, YAML/TOML checks
- Docker / Docker Compose for development

## 🚀 Get starting

#### 1️⃣ Clone the Repository

```bash
git clone git@github.com:DarkRader/fastapi-template.git new-project/
cd fnew-project
```
#### 2️⃣ Initialize a new project

Remove template Git history and create a fresh repository:

```bash
rm -rf .git
git init
git add .
git commit -m "chore: initial project from template"
```
#### 3️⃣ Connect to a remote repository

```bash
git remote add origin <your-origin>  # example git@github.com:yourname/new-project.git
git push -u origin main
```

## 🛠️ Get starting

#### 4️⃣ Install dependencies

This project uses **uv**:

```bash
cd fastapi-app
uv sync
source .venv/bit/activate
```

#### 5️⃣ Setup pre-commit hooks

```bash
pre-commit install
pre-commit run --all-files # check if it run properly
```

Included hooks:
- Ruff → lint + auto-format
- MyPy → static type checks
- YAML/TOML validation
- Trailing whitespace / EOF fixes

#### 6️⃣ Configure environment variables

Copy the example .env file:
```bash
cp fastapi-app/.env.example fastapi-app/.env
cp fastapi-app/.env.example .env
```

Update .env with:

- Database connection string (DATABASE_URL)
- OpenID credentials (OPENID_CLIENT_ID, OPENID_CLIENT_SECRET)
- Other secrets

#### 7️⃣ Database setup (PostgreSQL)

Use Docker Compose for development:
```bash
docker compose up -d db
```

Run migrations:
```bash
cd fastapi-app
chmod +x scripts/run_migrations.sh
./scripts/run_migrations.sh
```

#### 8️⃣ Run the application

Development mode (auto-reload)
```bash
uv run fastapi-app/src/main:app --reload
```

Docker mode
```bash
docker compose up --build
```

#### 9️⃣ Run tests

```bash
cd fastapi-app
chmod +x scripts/pytest.sh
./scripts/run_migrations.sh
```

#### 🔟 Folder Structure
```
fastapi-app/
 ├── src/                  # Application code
 ├── tests/                # Test cases
 ├── pyproject.toml        # Project config
 ├── ruff.toml             # Linter config
 ├── mypy.toml             # Type-checking config
 ├── Dockerfile
 └── .env.example

compose.yaml                # Docker Compose dev environment
.pre-commit-config.yaml     # Pre-commit hooks
```

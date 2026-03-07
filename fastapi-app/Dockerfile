FROM python:3.14-slim

# install uv binary
COPY --from=ghcr.io/astral-sh/uv:0.10.8 /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

# install dependencies only
COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# copy project files
COPY src ./src
COPY scripts ./scripts
COPY alembic.ini .

# install project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

RUN chmod +x scripts/run_migrations.sh

ENTRYPOINT ["scripts/run_migrations.sh"]
CMD ["python", "main.py"]

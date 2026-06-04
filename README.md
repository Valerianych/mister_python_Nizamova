# Лабораторные работы по unittest

Репозиторий для практических работ по автоматическому тестированию на Python.

В работе используется стандартный модуль `unittest`. Код лежит отдельно от тестов, чтобы было проще запускать проверки и добавлять новые задания.

## Что есть в проекте

- `labs/` — описания лабораторных работ;
- `src/` — основной код для проверки;
- `tests/` — тесты;
- `tools/run_tests.py` — отдельный запуск тестов для discovery;
- `.github/workflows/tests.yml` — автоматический запуск тестов в GitHub Actions;
- `pyproject.toml` — настройки проекта.

## Как запустить

Установить проект:

```bash
python -m pip install -e .
```

Запустить все тесты:

```bash
python -m unittest discover -s tests -t . -v
```

Запуск unit-тестов из третьей лабораторной:

```bash
python -m unittest discover -s tests/unit -t . -p "*_spec.py" -v
```

Запуск integration-тестов из третьей лабораторной:

```bash
python -m unittest discover -s tests/integration -t . -p "*_it.py" -v
```

Запуск через отдельный runner:

```bash
python tools/run_tests.py -v
```

## Структура проекта

```text
.
├── labs/
├── src/
│   ├── labtools/
│   ├── netutils/
│   ├── qautils/
│   └── shop/
├── tests/
│   ├── integration/
│   └── unit/
├── tools/
├── .github/workflows/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Описание

В репозитории собраны лабораторные работы по основным темам `unittest`: структура проекта, discovery, `TestCase`, fixtures, `TestSuite`, `subTest`, `Mock`, `patch`, `autospec`, работа с внешними зависимостями, логи, предупреждения, асинхронные тесты и CI.

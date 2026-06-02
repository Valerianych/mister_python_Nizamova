# Практические задания по `unittest`

Репозиторий сделан для практики по автоматическому тестированию на Python.
Внутри есть небольшой учебный код и набор тестов на стандартном модуле `unittest`.

## Что есть в работе

- базовые проверки через `TestCase`;
- разные `assert`-методы;
- запуск тестов через discovery;
- `setUp`, `tearDown`, `addCleanup`;
- работа с временными файлами;
- `subTest`;
- `skipIf` и `expectedFailure`;
- `Mock`, `MagicMock`, `patch`, `patch.object`, `patch.dict`;
- `spec`, `spec_set`, `autospec`;
- проверка логов и предупреждений;
- асинхронный тест через `IsolatedAsyncioTestCase`;
- GitHub Actions для автоматического запуска тестов.

## Как запустить

Сначала можно создать виртуальное окружение:

```bash
python -m venv .venv
```

Активация Windows:

```bash
.venv\Scripts\activate
```

Активация Linux/macOS:

```bash
source .venv/bin/activate
```

Установка проекта в editable-режиме:

```bash
python -m pip install -e .
```

Запуск всех тестов:

```bash
python -m unittest discover -s tests -v
```

Запуск одного файла:

```bash
python -m unittest tests.test_practices -v
```

## Структура

```text
.
├── src/
│   └── mister_python/
│       ├── __init__.py
│       ├── async_service.py
│       ├── file_tools.py
│       ├── services.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_practices.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── pyproject.toml
└── README.md
```

## Коротко по практикам

1. Создана структура проекта с папками `src` и `tests`.
2. Написаны первые тесты для функций.
3. Проверен запуск через `unittest discover`.
4. Используются фикстуры `setUp`, `tearDown` и `addCleanup`.
5. Есть пример ручной сборки `TestSuite`.
6. Используются `subTest`, `skipIf`, `expectedFailure`.
7. Есть тесты с `Mock` и `MagicMock`.
8. Используются разные варианты `patch`.
9. Применяются `spec`, `spec_set`, `autospec`.
10. Замоканы файловые операции, время и внешние сервисы.
11. Проверяются предупреждения и логи.
12. Есть асинхронный тест.
13. Добавлен workflow GitHub Actions.

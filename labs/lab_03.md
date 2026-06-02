# Лабораторная работа 3

## Тема

Настройка `unittest discovery` и запуск отдельных наборов тестов.

## Цель работы

Настроить запуск тестов под разные папки и шаблоны файлов, а также проверить запуск через `-k` и через отдельный runner.

## Задание

1. Создать пакет `shop` в папке `src`.
2. Добавить файл `src/shop/pricing.py`.
3. Реализовать функцию `final_price_cents`.
4. Создать unit-тесты в папке `tests/unit` с именем файла `pricing_spec.py`.
5. Создать integration-тесты в папке `tests/integration` с именем файла `pricing_it.py`.
6. Добавить файл `tools/run_tests.py` для запуска нужного набора тестов.

## Требования к `final_price_cents`

Функция принимает:

- `base_cents` — базовая цена в центах, целое число от 0;
- `discount_percent` — скидка от 0 до 100;
- `tax_percent` — налог от 0 до 100.

Сначала применяется скидка, потом налог. Результат возвращается как целое число.

## Команды запуска

Запуск unit-тестов:

```bash
python -m unittest discover -s tests/unit -t . -p "*_spec.py" -v
```

Запуск integration-тестов:

```bash
python -m unittest discover -s tests/integration -t . -p "*_it.py" -v
```

Запуск через фильтр `-k`:

```bash
python -m unittest discover -s tests/unit -t . -p "*_spec.py" -k discount -v
```

Запуск через runner:

```bash
python tools/run_tests.py -v
python tools/run_tests.py -k discount -v
python tools/run_tests.py -s tests/integration -p "*_it.py" -v
```

## Вывод

В работе настроен запуск разных наборов тестов через discovery, шаблоны файлов и отдельный скрипт запуска.

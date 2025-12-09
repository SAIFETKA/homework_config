# конфигурационное управление
## Общее описание
Он поддерживает:
- Однострочные (`:: комментарий`) и многострочные (`/* ... */`) комментарии.
- Числа, строки, массивы `#( ... )` и словари `{ ... }`.
- Объявления переменных: `var имя := значение;`.
- Константные выражения на этапе трансляции:  
  - Арифметика: `? (+ a b)`, `? (- a b)`, `? (* a b)`  
  - Длина массива: `? (len arr)`  
- Доступ к полям словаря через точку: `dict.field`.
- Генерацию корректного TOML-файла на выходе.

## Установка и зависимости
Требуется Python 3.11+ и пакет `lark` и `toml`.  
Установить зависимости:
```bash
pip install lark toml pytest
```
## Запуск
Get-Content ".\examples\example1.cfg" | python ".\src\main.py" -o "output.toml"
в POWERSHELL

## Проверка результата
Get-Content ".\output.toml"

## Тесты
python -m pytest tests/

## Пример toml
host = "localhost"
port = 8080
endpoints = [ "login", "logout", "status",]
total_clients = 110

[server_config]
max_connections = 100
timeout = 30.5
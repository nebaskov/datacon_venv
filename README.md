# Лекция на тему "Организация виртуального пространства"

## Установка интерпретатора Python
### [Ссылка для установки](https://www.python.org/downloads)


## Менеджмент виртуальных окружений

### [Venv](https://docs.python.org/3/library/venv.html)

Основной файл, содержащий зависимости - **requirements.txt**

#### Создание виртуального окружения
```bash
python -m venv env          # Windows

python3 -m venv env         # Linux / MacOS
```

#### Активация виртуального окружения
```bash
.\env\Scripts\activate      # Windows

source ./env/bin/activate   # Linux / MacOS
```

#### Установка зависимостей проекта
```bash
pip install -r requirements.txt
```

#### Установка отдельных пакетов
```bash
pip install requests
```

#### Просмотр установленных зависимостей проекта
```bash
pip list
```

#### Создание файла requirements.txt
```bash
pip freeze >> requirements.txt
```
#### !!! Важно - при повторном выполнении команды файл не перезаписывается, в него продолжается запись с сохранением старого содержания !!!


### [Poetry](https://python-poetry.org/)

Основной файл, содержащий зависимости - **pyproject.toml**

#### Создание виртуального окружения
```bash
poetry init
```

#### Активация виртуального окружения
```bash
poetry shell
```

#### Установка зависимостей проекта
```bash
poetry install
```

#### Установка отдельных пакетов
```bash
poetry add requests
```
Интересная особенность - poetry добавляет установленный пакет в pyproject.toml автоматически

#### Просмотр установленных зависимостей проекта
```bash
poetry show
```

### [Anaconda](https://python-poetry.org/)

Основной файл, содержащий зависимости - **pyproject.toml**

#### Создание виртуального окружения
```bash
poetry init
```

#### Активация виртуального окружения
```bash
poetry shell
```

#### Установка зависимостей проекта
```bash
poetry install
```

#### Установка отдельных пакетов
```bash
poetry add requests
```
Интересная особенность - poetry добавляет установленный пакет в pyproject.toml автоматически

#### Просмотр установленных зависимостей проекта
```bash
poetry show
```



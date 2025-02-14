# Лекция на тему "Организация виртуального пространства"

## [Материалы к лекции](task.md)

## [Установка интерпретатора Python](https://www.python.org/downloads)


## Модули для управления виртуальными окружениями

### [Venv](https://docs.python.org/3/library/venv.html)

Основной файл, содержащий зависимости - **requirements.txt**

#### Создание виртуального окружения

Windows
```bash
python -m venv <my-env>
```

Linux / MacOS
```bash
python3 -m venv <my-env>
```

#### Активация виртуального окружения
Windows
```bash
.\<my-env>\Scripts\activate
```

Linux / MacOS
```bash
source ./<my-env>/bin/activate
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

### [Conda](https://docs.anaconda.com/)

Основной файл, содержащий зависимости - **environment.yml**

#### Создание виртуального окружения
```bash
conda create --name <my-env>
```

#### Создание виртуального окружения с указанием версии Питона
```bash
conda create -n <my-env> python=3.9
```

#### Активация виртуального окружения
```bash
conda activate <my-env>
```

#### Установка зависимостей проекта
```bash
conda env create -f environment.yml
```

#### Установка отдельных пакетов
```bash
conda install requests
```

#### Просмотр установленных зависимостей проекта
```bash
conda list
```

#### Создание файла environment.yml
```bash
conda env export > environment.yml
```
<br>

Особенность conda - можно использовать любое из созданных окружений вне зависимости от проекта
#### Просмотр созданных окружений
```bash
conda env list
```


### Одна команда, которая решит проблему с путями
```bash
export PYTHONPATH=$(pwd)
```
С помощью нее устанавливается переменная окружения **PYTHONPATH**, которая позволяет интерпретатору понять, в какой именно директории располагается запускаемый проект и его модули.<br>

**pwd** (print working directory) - команда в командной строке Linux, позволяющая вывести полный путь до текущей директории пользователя в файловой системе.
# Star Wars Snakemake Workflow

## Описание

Простой workflow на **Snakemake**, который демонстрирует автоматизацию процессов.
В нашем примере workflow запускает Python-скрипт, который генерирует список персонажей **Star Wars** и подсчитывает их количество.

Цель — показать работу Snakemake, управление зависимостями и воспроизводимость результатов.

---

## Структура проекта

```
.
├── Snakefile
├── scripts/
│   └── star_wars.py
└── README.md
```

* **Snakefile** — основной файл workflow, описывает цель и шаги
* **scripts/star_wars.py** — Python-скрипт для генерации отчёта
* **README.md** — документация проекта

---

## Установка

### 1. Создать виртуальное окружение

```powershell
python -m venv venv
```

### 2. Активировать окружение

```powershell
# PowerShell
.\venv\Scripts\Activate.ps1
```

### 3. Установить Snakemake

```powershell
pip install snakemake
```

---

## Запуск workflow

В корне проекта выполните:

```powershell
snakemake
```

* Snakemake создаст файл `result.txt` в корне проекта
* Файл содержит список персонажей и их количество

---

## Пример результата (`result.txt`)

```
Star Wars characters:
- Luke Skywalker
- Leia Organa
- Darth Vader
- Yoda
- Obi-Wan Kenobi

Total characters: 5
```

---

## Git

* Добавьте виртуальное окружение в `.gitignore`:

```
venv/
result.txt
```

* Пушим только код и Snakefile, workflow можно запускать локально

---

## Примечания

* Workflow состоит из одного шага — демонстрация Snakemake
* Входные данные находятся внутри скрипта для простоты


# Yadro Trial Project

## Описание
Этот проект предназначен для обработки UML-моделей, генерации конфигурационных файлов и работы с дельта-изменениями. Программа выполняет следующие задачи:
- Парсинг UML-моделей из XML-файлов.
- Генерация конфигурационных файлов (`config.xml`).
- Генерация мета-данных (`meta.json`).
- Генерация дельта-изменений между конфигурациями (`delta.json`).
- Генерация патченного конфигурационного файла (`res_patched_config.json`).

## Требования
- **Python 3.11** (или выше)
- Стандартные библиотеки Python (дополнительные зависимости отсутствуют)

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone <repository_url>
   cd yadro-trial
   ```
2. Создайте виртуальное окружение (для этого проекта не нужно):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   ```
3. Убедитесь, что у вас установлен Python версии 3.11:
   ```bash
   python --version
   ```

## Структура проекта
```
yadro-trial/
├── data/                   # Входные и выходные данные
│   ├── input/              # Входные файлы (XML, JSON)
│   ├── out/                # Сгенерированные файлы
│   └── logs/               # Логи выполнения программы
├── src/                    # Исходный код
│   ├── generators/         # Генераторы (config, meta, delta, patched config)
│   ├── model/              # Модели данных (UMLModel, DeltaModel)
│   ├── parsers/            # Парсеры (XML, JSON)
│   └── utils/              # Утилиты (логирование, вспомогательные функции)
├── main.py                 # Главная точка входа
├── config.json             # Конфигурационный файл
└── README.md               # Документация
```

## Конфигурация
Файл `config.json` содержит настройки путей для входных и выходных данных:
```json
{
    "input_dir": "data/input",
    "output_dir": "data/out",
    "xml_input_file": "impulse_test_input.xml",
    "json_config_file": "config.json",
    "patched_json_config_file": "patched_config.json",
    "config_output_file": "config.xml",
    "meta_output_file": "meta.json",
    "delta_output_file": "delta.json",
    "patched_config_output_file": "res_patched_config.json"
}
```

## Запуск
1. Поместите входные файлы в папку `data/input`.
2. Запустите программу:
   ```bash
   python main.py
   ```
3. Сгенерированные файлы будут сохранены в папке `data/out`.

## Логирование
Логи выполнения программы сохраняются в папке `data/logs/application.log`.

## Тестирование
Для тестирования можно использовать `unittest`:
```bash
python -m unittest discover
```

## Пример использования
1. Входной XML-файл (`impulse_test_input.xml`):
   ```xml
   <BTS>
       <Class name="ExampleClass" documentation="Example documentation" isRoot="true">
           <Attribute name="attr1" type="string" />
           <Attribute name="attr2" type="int" />
       </Class>
   </BTS>
   ```
2. Сгенерированный `config.xml`:
   ```xml
   <BTS>
       <ExampleClass>
           <attr1>string</attr1>
           <attr2>int</attr2>
       </ExampleClass>
   </BTS>
   ```
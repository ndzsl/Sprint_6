<h><center>YANDEX PRACTICUM SPRINT #6<center></h>

<hr>

## Тестировщик: Надежда Планидина

## <h>Когорта: #12</h>

## <h>Проект: Яндекс Самокат</h>

<hr>

## <h>ИНСТРУКЦИИ ПО ЗАПУСКУ ТЕСТОВ:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt

### <h>2. Запустите все тесты:</h>

> pytest -v

### <h>3. Просмотрите отчет Allure в формате HTML:</h>

> allure serve allure_results

<hr>

<h3 align="left" style="color:green">Файлы проекта и их описание:</h3>

| Название файла                | Содержание файла          |
|-------------------------------|---------------------------|
| main_page_locators.py          | Локаторы для главной страницы |
| order_page_locators.py         | Локаторы для страницы заказа |
| base_page.py                   | Методы базовой страницы   |
| main_page.py                   | Методы главной страницы   |
| order_page.py                  | Методы страницы заказа    |
| test_questions_answers.py      | Тесты на вопросы и ответы |
| test_order_creation.py         | Тесты успешного создания заказа |
| test_page_navigation.py        | Тесты навигации по страницам |
| conftest.py                    | Системный файл проекта     |
| generators.py                  | Генераторы случайных данных для заказов |
| data.py                        | Файл данных проекта       |
| requirements.txt               | Файл с зависимостями       |
| allure_results.dir             | Директория отчетов Allure  |



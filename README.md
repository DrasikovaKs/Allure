Для написания и запуска тестов требуется
1. PyCharm (подключить к проекту библиотеки: pytest, selenium, allure-pytest, allure-pytest-commons)
2. Java
3. PowerShell (для установки allure и просмотра отчётов)

Запуск тестов через консоль:
pytest Tests_Search.py --alluredir results

Просмотр отчётов в allure:
allure serve relults

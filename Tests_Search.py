import allure

from allure_commons.types import AttachmentType
from selenium import webdriver


class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Firefox(executable_path='D:\\_dev\\geckodriver.exe')

    def teardown(self):
        self.driver.quit()

    @allure.feature('Open pages')
    @allure.story('Открываем страницу google.com')
    @allure.severity('blocker')
    def test_google_search(self):
        self.driver.get('https://www.google.com/')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Google"

    @allure.feature('Open pages')
    @allure.story('Открываем страницу yandex.com')
    @allure.severity('critical')
    def test_yandex_search(self):
        self.driver.get('https://yandex.by/')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Яндекс"

    @allure.feature('Open pages')
    @allure.story('Открываем страницу yahoo.com')
    @allure.severity('trivial')
    def test_yahoo_search(self):
        self.driver.get('https://www.yahoo.com/')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            assert self.driver.title == "Yahoo"

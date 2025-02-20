import pytest
from selene import browser, by


def test_desktop(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Мобильное разрешение")
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


def test_mobile(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Десктопное разрешение")
    browser.open("http://github.com")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()
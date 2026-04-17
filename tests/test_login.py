import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login_shows_admin_panel(self, driver, base_url):
        login = LoginPage(driver)
        login.open(base_url)
        login.login("admin", "password")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "roomName")),
            message="Admin panel not visible after valid login"
        )

    def test_invalid_login_stays_on_login_page(self, driver, base_url):
        login = LoginPage(driver)
        login.open(base_url)
        login.login("wrong_user", "wrong_pass")
        assert not login.is_logged_in()

    def test_logout_returns_to_login_form(self, logged_in):
        login = LoginPage(logged_in)
        login.logout()
        assert not login.is_logged_in()

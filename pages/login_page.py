from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    _USERNAME = (By.ID, "username")
    _PASSWORD = (By.ID, "password")
    _LOGIN_BTN = (By.ID, "doLogin")
    _LOGOUT_BTN = (By.XPATH, "//button[normalize-space(text())='Logout']")
    _ALERT = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, base_url: str):
        self.driver.get(f"{base_url}/admin")
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BTN))

    def login(self, username: str, password: str):
        field = self.wait.until(EC.element_to_be_clickable(self._USERNAME))
        field.clear()
        field.send_keys(username)
        pwd = self.driver.find_element(*self._PASSWORD)
        pwd.clear()
        pwd.send_keys(password)
        self.driver.find_element(*self._LOGIN_BTN).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGOUT_BTN)).click()
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BTN))

    def is_logged_in(self) -> bool:
        try:
            return self.driver.find_element(*self._LOGOUT_BTN).is_displayed()
        except Exception:
            return False

    def get_alert_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self._ALERT)).text

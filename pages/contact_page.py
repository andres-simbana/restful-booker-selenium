from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactPage:
    _NAME = (By.CSS_SELECTOR, "input[placeholder='Name']")
    _EMAIL = (By.CSS_SELECTOR, "input[placeholder='Email']")
    _PHONE = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    _SUBJECT = (By.CSS_SELECTOR, "input[placeholder='Subject']")
    _MESSAGE = (By.CSS_SELECTOR, "textarea[placeholder='Message']")
    _SUBMIT = (By.ID, "submitContact")
    _SUCCESS = (By.XPATH, "//*[contains(text(),'Thanks for getting in touch')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, base_url: str):
        self.driver.get(base_url)
        self.wait.until(EC.presence_of_element_located(self._NAME))

    def scroll_to_form(self):
        el = self.driver.find_element(*self._NAME)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)

    def fill_and_submit(self, name: str, email: str, phone: str, subject: str, message: str) -> None:
        self.scroll_to_form()
        self.wait.until(EC.element_to_be_clickable(self._NAME)).send_keys(name)
        self.driver.find_element(*self._EMAIL).send_keys(email)
        self.driver.find_element(*self._PHONE).send_keys(phone)
        self.driver.find_element(*self._SUBJECT).send_keys(subject)
        self.driver.find_element(*self._MESSAGE).send_keys(message)
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT)).click()

    def is_success_shown(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self._SUCCESS))
            return True
        except Exception:
            return False

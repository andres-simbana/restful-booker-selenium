from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class AdminPage:
    _ROOM_NAME = (By.ID, "roomName")
    _ROOM_TYPE = (By.ID, "type")
    _ACCESSIBLE = (By.ID, "accessible")
    _ROOM_PRICE = (By.ID, "roomPrice")
    _CREATE_BTN = (By.ID, "createRoom")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def create_room(self, name: str, room_type: str = "Single", accessible: bool = False, price: str = "150") -> None:
        name_field = self.wait.until(EC.element_to_be_clickable(self._ROOM_NAME))
        name_field.clear()
        name_field.send_keys(name)
        Select(self.driver.find_element(*self._ROOM_TYPE)).select_by_visible_text(room_type)
        Select(self.driver.find_element(*self._ACCESSIBLE)).select_by_value("true" if accessible else "false")
        price_field = self.driver.find_element(*self._ROOM_PRICE)
        price_field.clear()
        price_field.send_keys(price)
        self.driver.find_element(*self._CREATE_BTN).click()

    def room_exists(self, name: str) -> bool:
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, f"roomName{name}"))
            )
            return True
        except Exception:
            return False

    def delete_room(self, name: str) -> None:
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//p[@id='roomName{name}']"
                 "/ancestor::div[@data-testid='roomlisting']"
                 "//span[contains(@class,'roomDelete')]")
            )
        )
        btn.click()

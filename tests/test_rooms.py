import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.admin_page import AdminPage


class TestRooms:

    def test_create_single_room(self, logged_in):
        admin = AdminPage(logged_in)
        admin.create_room("AT101", room_type="Single", price="120")
        assert admin.room_exists("AT101")

    def test_create_double_room(self, logged_in):
        admin = AdminPage(logged_in)
        admin.create_room("AT202", room_type="Double", price="200")
        assert admin.room_exists("AT202")

    def test_create_suite_accessible(self, logged_in):
        admin = AdminPage(logged_in)
        admin.create_room("AT303", room_type="Suite", accessible=True, price="350")
        assert admin.room_exists("AT303")

    def test_delete_room_removes_it_from_list(self, logged_in):
        admin = AdminPage(logged_in)
        admin.create_room("ATDEL", room_type="Twin", price="100")
        assert admin.room_exists("ATDEL")
        admin.delete_room("ATDEL")
        WebDriverWait(logged_in, 10).until_not(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space(text())='ATDEL']")
            )
        )

import pytest
from pages.contact_page import ContactPage


class TestContact:

    def test_valid_contact_form_shows_success(self, driver, base_url):
        contact = ContactPage(driver)
        contact.open(base_url)
        contact.fill_and_submit(
            name="Test Automation",
            email="test@example.com",
            phone="01234567890",
            subject="Automation Test",
            message="This is an automated test message for validation purposes only."
        )
        assert contact.is_success_shown()

    def test_empty_contact_form_does_not_show_success(self, driver, base_url):
        contact = ContactPage(driver)
        contact.open(base_url)
        contact.js_click(contact._SUBMIT)
        assert not contact.is_success_shown()

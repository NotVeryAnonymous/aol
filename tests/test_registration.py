import pytest
from pages.locators import HomePage, Registration, Subscription
from seleniumbase import BaseCase
from configparser import ConfigParser

config = ConfigParser()
config.read(r'config/config.ini')


class RegistrationTestClass(BaseCase):
    def test_registration(self):
        self.get(config.get('config', 'url'))

        self.click(HomePage.sign_up_button)

        # I do the set_text first (and find_text a few lines down) because SeleniumBase is doing a WebDriverWait for us,
        # ensuring that the page is sufficiently loaded before proceeding to the asserts.
        self.set_text(Registration.email_text_box, config.get('config', 'email'))
        assert self.get_current_url() == config.get('config', 'registration_url')
        self.click(Registration.submit_button)

        self.find_text("Become a Member!")
        assert self.get_current_url() == config.get('config', 'subscription_url')




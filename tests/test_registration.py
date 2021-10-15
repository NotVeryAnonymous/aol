import pytest
from pages.locators import HomePage, Registration, Subscription
from seleniumbase import BaseCase
from configparser import ConfigParser

config = ConfigParser()
config.read(r'config/config.ini')


class RegistrationTestClass(BaseCase):
    """
    1. Instead of reinventing the wheel for this assignment by making methods to interact, I used the library called
    SeleniumBase that does a lot of abstraction for us such as WebDriverWait's. I still made some classes in
    pages/locators.py to store the selectors, and config/config.ini to store the configs.
    Reference: https://seleniumbase.io

    2. Note that this won't actually pass right now. The elements to be located are all within multiple layers of a
    shadow DOM that, while possible to traverse, looks quite cumbersome given the scope of the assignment. The elements
    can't even be selected via entering an XPath/selector in the browser console because of the shadow DOM.

    3. The instructions do not have the updated URL for registration, I've used the updated URL in my config.ini

    4. See sort.py for that part of the assignment.
    """
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




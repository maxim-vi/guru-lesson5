from selene import browser
from selenium import webdriver
import pytest


browser.config.driver = webdriver.Firefox()
@pytest.fixture
def size_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 1040
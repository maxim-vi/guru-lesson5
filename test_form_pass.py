from selene import browser , have, be
from selenium import webdriver
import os
import pytest


browser.config.driver = webdriver.Firefox()
@pytest.fixture
def size_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 1040

def test_find_pass(size_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    # name Email Gender Mobile
    browser.element('#firstName').set_value('Максим').should(have.value('Максим'))
    browser.element('#lastName').set_value('Титов').should(have.value('Титов'))
    browser.element('#userEmail').set_value('test.test@gmail.com').should(have.value('test.test@gmail.com'))
    browser.all('#genterWrapper label').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').set_value('9252191919').should(have.value('9252191919'))

    # Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-dropdown-container--select > select').click()
    browser.element('.react-datepicker__month-dropdown-container--select > select > option:nth-child(2)').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-dropdown-container--select > select > option:nth-child(84)').click()
    browser.element('.react-datepicker__day--019.react-datepicker__day--weekend').click()
    browser.element('#dateOfBirthInput').should(have.value('19 Feb 1983'))

    # Subjects, Hobbies
    browser.element('#subjectsInput').type('ma')
    browser.all("#subjectsWrapper div").element_by(have.exact_text("Maths")).click()
    browser.all('#hobbiesWrapper label').element_by(have.exact_text('Reading')).click()

    # picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('file/philin.jpeg'))

    # Fill Current Address
    browser.element('#currentAddress').should(be.blank).type('Russia, Moscow, str.Test')

    # Fill State and City
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    # Click the register button
    browser.element('#submit').click()

    # Check that the modal window has appeared
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # We check that our text is filled in
    browser.element('.table').all('td').even.should(
        have.texts(
            'Максим Титов',
            'test.test@gmail.com',
            'Male',
            '9252191919',
            '19 February,1983',
            'Maths',
            'Reading',
            'philin.jpeg',
            'Russia, Moscow, str.Test',
            'NCR Delhi'
        )
    )

    # Closing the window
    browser.element('#closeLargeModal').click()

    # We check that the form is empty
    browser.element('#firstName').should(be.blank)


























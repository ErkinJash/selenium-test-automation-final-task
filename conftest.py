import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose a browser: chrome or firefox')
    parser.addoption('--language', action='store', default="en",
                     help="Choose code from language code table list for a desired language to be used fro browser")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    list_of_lang_code_table = [
        "ar", "zh-hans", "uk", "sk", "ru", "ro",
        "pt-BR", "pt", "pl", "nl", "ko", "it",
        "fr", "fi", "es", "el", "eo", "en",
        "de", "da", "cs", "ca"
    ]

    if browser_name == 'chrome' and user_language in list_of_lang_code_table:
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}
        )
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox' and user_language in list_of_lang_code_table:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError('''
        Ooops! Something went wrong!
        Browser_name should be 'chrome or firefox',
        Here is the list from language code table that you can use:
                             ar = Arabian
                             ca = Catalan
                             cs = Czech
                             da = Danish
                             de = German
                             en = British English
                             eo = Esperanto
                             el = Greek
                             es = Spanish
                             fi = Finnish
                             fr = French
                             it = Italian
                             ko = Korean
                             nl = Dutch
                             pl = Polish
                             pt = Portuguese
                             pt-BR = Portuguese (Brazil)
                             ro = Romanian 
                             ru = Russian
                             sk = Slovenian
                             uk = Ukrainian
                             zh-hans = Chinese''')

    yield browser
    time.sleep(3)
    browser.quit()
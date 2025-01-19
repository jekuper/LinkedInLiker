from selenium import webdriver

def initialize_driver() -> webdriver.Chrome:
    """Initialize the Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    return webdriver.Chrome(options=options)
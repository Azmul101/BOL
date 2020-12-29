import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from TestData.Data import Testdata

global driver


def pytest_addoption(parser):   # Select the browser name in Jenkins
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):   # Setup method
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        option = Options()
        prefs = {"profile.default_content_setting_values.notifications": 1}
        option.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=option, executable_path=Testdata.chrome)
    elif browser_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        profile.set_preference("dom.push.enabled", False)
        driver = webdriver.Firefox(firefox_profile=profile, executable_path=Testdata.firefox)
    driver.get(Testdata.URL)  # Passing the URL
    driver.maximize_window()
    request.cls.driver = driver  # Pass the request to run driver
    yield
    driver.close()  # TearDown method


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):  # Capture the failed testcases screenshot during the process.
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

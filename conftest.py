#94 Basic patterns and examples of pytest in this website: https://docs.pytest.org/en/6.0.1/example/simple.html

import pytest
from selenium import webdriver
import time
driver = None  #A


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.fixture(scope="class")           #93 this is the annotation to declare fixture
# def setup(request):                     # we gave 'request' instance in here/in local setup because of f line below
#     driver = webdriver.Chrome()
#     driver.get("https://rahulshettyacademy.com/angularpractice")
#     driver.maximize_window()
#     request.cls.driver = driver         #f line. whichever class/test case uses this fixture in that class if there is a 'driver' variable then this driver goes and be assigned to that (basically, when this fixture is used in some test case, it can use driver variable too, that's why we need to write the code in this line)
#     yield
#     driver.close()


# Lecture 94. Passing command line options to select browser at run time

# THIS IS A SYNTAX
# def pytest_addoption(parser):               #94 adding command line option like this is called 'hook'
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"              #--browser_name is a keyword; & we defined chrome as a default browser (url for this command lines given above)
    )




@pytest.fixture(scope="class")
def setup(request):
    global driver       #B
    browser_name = request.config.getoption("browser_name")             #(url for this command lines given above)
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()              # Now in Terminal, if I want to run my test in browser other than Chrome, Instead of py.test command I run:: py.test --browser_name <browserName>

# Lecture 104. When we add following fixture to our 'setup' fixture system automatically will take a screen shot when there is a failure,
  #and following steps are needs to be executed:
    #1. Declared driver globally to none (line A)
    #2. Added line 'global driver' in 'setup' fixture (line B)
    #3. Now all this 'driver' objects in 'setup' test will be pointing to global object only (line B)
    #4. Screen shot also will have access to the Chrome driver path
    #5. When there's failure copy the path of html report given @ the end of the execution & paste in new window of browser, screen shot will be attached in the report

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
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

#sudo rm -rf /Library/PreferencePanes/JavaControlPanel.prefPane
#44cf89f80c484139920afdba1c9c4184
#/Users/husnyaislamova/PycharmProjects1/PythonSelFramework/reports




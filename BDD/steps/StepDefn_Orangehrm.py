import allure
from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(30)
@given('the user launches Application')
def the_user_launches_Application(context):
    context.driver = driver
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('the user verifies logo')
def the_user_verifies_logo(context):
    context.driver = driver
    logo = context.driver.find_element(By.XPATH,'//div[@id="divLogo"]/img')
    assert logo.is_displayed() is True

@when('the user enters username in username field')
def the_user_enters_username_in_username_field(context):
    context.driver = driver
    context.driver.find_element(By.ID,"txtUsername").send_keys("admin")


@then('the user enters password in password field')
def the_user_enters_password_in_password_field(context):
    context.driver = driver
    context.driver.find_element(By.ID, "txtPassword").send_keys("admin123")



@when(u'the user verifies home Page title')
def the_user_verifies_home_Page_title(context):
    context.driver =driver
    HomePageLogo = context.driver.find_element(By.XPATH,'//img[@alt="OrangeHRM"]').is_displayed()
    assert HomePageLogo is True

@then(u'the user clicks on logout button')
def the_user_clicks_on_logout_button(context):
    context.driver = driver
    # wait = WebDriverWait(context.driver, 30)
    # wait.until(expected_conditions.element_to_be_clickable((By.ID,'welcome')))
    welcome = context.driver.find_element(By.ID,'welcome').click()
    # wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[text()='Logout']")))
    Logout = context.driver.find_element(By.XPATH,"//a[text()='Logout']")

    driver.execute_script("arguments[0].click;",Logout)

@then('the user clicks on login button')
def the_user_clicks_on_login_button(context):
    context.driver = driver
#    context.driver.find_element(By.NAME, "Submit").click()




@then(u'the user enters "{password}" in password field')
def step_impl(context,password):
    context.driver = driver
    context.driver.find_element(By.ID, "txtPassword").send_keys(password)


@when(u'the user enters "{username}" in username field')
def step_impl(context,username):
    context.driver = driver
    context.dcriver.find_element(By.ID,"txtUsername").send_keys(username)

def Capture_Screenshot(context):
    context.driver = driver
    allure.attach(context.driver.get_screenshot_as_png(),name=context.step.name,attachment_type=allure.attachment_type.PNG)
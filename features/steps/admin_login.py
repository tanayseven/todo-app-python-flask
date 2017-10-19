from behave import *
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from todo_app.extensions import db
from todo_app.user.repos import AdminRepo

use_step_matcher("re")


@given("Admin user has correct credentials")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    db.drop_all()
    db.create_all()
    AdminRepo.add_new_admin(
        user_name='admin',
        password='admin',
        email='admin@1234.com',
    )


@step("Admin opens the browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.WebDriver(chrome_options=chrome_options)
    driver.get('http://localhost:5000/admin/')
    setattr(context, 'driver', driver)


@step("Admin user enters his user name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = getattr(context, 'driver')
    element = driver.find_element_by_name('loginUsername')
    element.clear()
    element.send_keys('admin')


@step("Admin user enters his password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = getattr(context, 'driver')
    element = driver.find_element_by_name('loginPassword')
    element.clear()
    element.send_keys('admin')


@step("Admin user clicks on the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = getattr(context, 'driver')
    element = driver.find_element_by_id('login')
    element.click()


@then("Admin user should be taken to the login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = getattr(context, 'driver')
    element = driver.find_element_by_id('admin-home')
    assert element is not None

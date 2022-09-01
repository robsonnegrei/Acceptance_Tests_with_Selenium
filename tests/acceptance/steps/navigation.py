from behave import *
from selenium import webdriver

use_step_matcher('re')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    context.browser.get('http://127.0.0.1:5000')


@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()

@then('Iam on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    browser = webdriver.Chrome(chrome_options=chrome_options)
    assert context.browser.current_url == expected_url



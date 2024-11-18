from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

options = ChromeOptions()
driver = webdriver.Remote(
    options=options, command_executor="http://host.docker.internal:4444")
wait = WebDriverWait(driver, 10)
email = ""
password = ""
multi_auth_code = ""


def cdle_splash_page(driver):
    driver.get("https://myui.clouduim.cdle.state.co.us/Claimant/Core/Login.ASPX")

    form = driver.find_element(By.CLASS_NAME, "form-control")
    form.find_element(By.CLASS_NAME, "btn-primary").click()


def id_me_login_form(driver, wait):
    email_locator = (By.ID, "user_email")
    wait.until(EC.presence_of_element_located(email_locator))

    email_input = driver.find_element(*email_locator)
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "user_password")
    password_input.send_keys(password)

    driver.find_element(By.TAG_NAME, "form").submit()


def id_me_multifactor_auth_forms(driver, wait):
    generator_locator = (By.PARTIAL_LINK_TEXT, "generator")
    wait.until(EC.presence_of_element_located(generator_locator))
    driver.find_element(*generator_locator).click()

    multifactor_locator = (By.ID, "multifactor_code")
    wait.until(EC.presence_of_element_located(multifactor_locator))
    driver.find_element(*multifactor_locator).send_keys(multi_auth_code)
    driver.find_element(By.TAG_NAME, "form").submit()

    # Accept consent form
    driver.find_element(By.TAG_NAME, "form").submit()


try:
    cdle_splash_page(driver)
    id_me_login_form(driver, wait)
    id_me_multifactor_auth_forms(driver, wait)

    wait.until(EC.title_contains("Claim Status"))

    print("Successfully Logged in to CDLE!!")

    time.sleep(30)

finally:
    driver.quit()

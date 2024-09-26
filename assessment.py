from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()

try:
    driver.get('https://www.flipkart.com/')
    driver.maximize_window()

    # search_box = driver.find_element(By.XPATH, "//input[@title='Search for Products, Brands and More']")
    # search_box.send_keys('lg soundbar')
    # search_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    # search_button.click()
    
    hover_to_fashion = driver.find_element(By.XPATH, "//span[text()='Fashion']")
    action = ActionChains(driver)
    action.move_to_element(hover_to_fashion).perform()
    hover_mens_footwear = driver.find_element(By.XPATH, "//a[contains(text(),'Top Wear')]")
    action.move_to_element(hover_mens_footwear).perform()
    click_sandals = driver.find_element(By.XPATH, "//a[contains(text(),'T-Shirts')]")
    click_sandals.click()
    
    start_price_adjust = driver.find_element(By.XPATH, "//div[@class='iToJ4v Kaqq1s']//div[@class='PYKUdo']")
    end_price_adjust = driver.find_element(By.XPATH, "//div[@class='iToJ4v D0puJn']//div[@class='PYKUdo']")
    
    action.click_and_hold(start_price_adjust).move_by_offset(75, 0).release().perform()
    time.sleep(2)

    action.click_and_hold(end_price_adjust).move_by_offset(-40, 0).release().perform()
    time.sleep(3)
    click_peter_england_product = driver.find_element(By.XPATH, "//div[text()='PETER ENGLAND']/following-sibling::a[@class='WKTcLC']")
    driver.execute_script("arguments[0].scrollIntoView();", click_peter_england_product)

    time.sleep(2)

    # Now click the PETER ENGLAND product
    click_peter_england_product.click()
    
    time.sleep(5)


finally:
    driver.quit()


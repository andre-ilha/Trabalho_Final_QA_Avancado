from selenium import webdriver
import time

def before_all(context):
    context.browser = webdriver.Firefox()

def after_all(context):
    context.browser.quit()
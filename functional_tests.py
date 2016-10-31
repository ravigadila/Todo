from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Iam here' in browser.body
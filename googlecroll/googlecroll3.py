
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='C:/Users/student/Documents/jinahan/googlecroll/geckodriver.exe')

browser.get("https://www.google.com/search?q="+"조국"+"&sxsrf=ACYBGNSRzU3ufdsJK1P8V79WyrsOnA4NIg:1570437429290&source=lnms&tbm=nws&sa=X&ved=0ahUKEwj4kPWo34nlAhWCwosBHUpoBAYQ_AUIEigB&biw=1067&bih=811?q=")

results = browser.find_elements_by_css_selector('div.g')

hrefs = []

for i in range(0,11):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))

for href in hrefs:
    print(href)

#from furl import furl
#f = furl(href)

for href in hrefs:
    browser.execute_script('window.open("'+ href +'","_blank");')

# print(f.args['url'])





from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def homepage(request):
    num = random.randrange(1022,9899)
    global str_num
    str_num =str(num)
    return render(request,"index.html",{"cap":str_num})    

def submit(request):
    if request.method =="POST":
        captcha = request.POST.get("cap")
        if str_num==str(captcha):
            return HttpResponse("success")
        else:
            return HttpResponse("<h4>captcha error</h4>")
    else:
        return HttpResponse("Error")



#---------------------------------------------------------------------------------
#scrapping from amazone website

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("samsung Phones")
driver.find_element(By.XPATH,"//span[text()='Samsung']").click()
phonenames= driver.find_element(By.XPATH,"//span['contains(@class,'a-color-base a-text-normal')]")
prices = driver.find_element(By.XPATH,"//span['contains(@class,'price-whole')]")

for phone in phonenames:
    print(phone.text)
for price in prices:
    print(price.text) 

print("*"*50)
driver.quit()
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://twitter.com/login/')

i = 0

input("Login first and press enter!!")
driver.get('https://twitter.com/search?q=%23%D8%A7%D9%86%D8%AA%D8%B1%D9%86%D8%AA_%D8%BA%D9%8A%D8%B1_%D9%85%D8%AD%D8%AF%D9%88%D8%AF_%D9%81_%D9%85%D8%B5%D8%B1&src=trend_click&vertical=trends')

sleep(7)
while 1:
    n = random.randint(1, 8000)
    mylist = [
    " احنا قد التحدي احنا مش هنتنازل عن انترنت غير محدود " + str(n) + " - " + str(i),
    " نعم ل اقاله وزير الاتصالات نعم لـ انترنت غير محدود فل مصر " + str(n) + " - " + str(i),
    " Enough deceiving enough stealing enough pressure enough pretending that u don't see anything we need " + str(n) + " - " + str(i),
    " don’t stop until this shit gone we need " + str(n) + " - " + str(i),
    " معادنا الساعه 9 كلنا هنعمل الموبايل وضع طيران تعبيرا عن الغضب وافتكر ان لما يعدي عليهم ساعه بدون كلام دا خساره فلوس " + str(n) + " - " + str(i),
    " كلنا ايد واحده ضدد الاستغلال حارب الاستغلال عن طريق الغاء التعاقد كلنا هنلغي تعاقد بعد العيد ومش هنجدد اشتراكنا في ميعاده " + str(n) + " - " + str(i),
    ]
    g = round(random.uniform(0.4, 1.0), 1)
    k = random.randint(2, 10)
    driver.find_element(by=By.XPATH, value="//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(g)
    v = mylist[random.randint(0, len(mylist)-1)]
    print(v)
    driver.find_element(by=By.XPATH, value="//div[@role='textbox']").send_keys(f"{v} \n #اقاله_وزير_الاتصالات \n")
    driver.find_element(by=By.XPATH, value="//div[@data-testid='tweetButton']").click()
    i += 1
    sleep(k)


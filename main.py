from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("/Users/derrick/chromedriver")
base_url = "https://app.ucas.ac.cn/site/dailyReport/reportAll"
driver.get(base_url)

WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
)
user = driver.find_element_by_xpath("//input[@type='text']")
user.send_keys("YOURACCOUNT")
passwd = driver.find_element_by_xpath("//input[@type='password']")
passwd.send_keys("YOURPASSWORD")
button = driver.find_element_by_xpath("//div[@class='btn']")
button.click()
cookies = driver.get_cookies()
print(cookies)

//number 填姓名学号
dic = {"realname": "YOURNAME", "number": xuehao,"szgj_api_info": {"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","country":{"label":"","value":""},"details":"","province":{"label":"","value":""}},
"szgj": "",
"old_sfzx":"",
"sfzx": 0,
"szdd": "国内",
"ismoved": 0,
"tw": 2,
"bztcyy": "",
"sfcxtz": 0,
"sfyyjc": "",
"jcjgqr": "",
"sfjcbh": 0,
"jcbhlx": "",
"sfcyglq": 0,
"gllx": "",
"sfcxzysx": 0,
"old_szdd": "国内",
"geo_api_info": {"address":"北京市丰台区","details":"新村街道丰葆路总部基地6区","province":{"label":"北京市","value":""},"city":{"label":"","value":""},"area":{"label":"丰台区","value":""}},
"old_city": {"address":"北京市丰台区","details":"新村街道丰葆路总部基地6区","province":{"label":"北京市","value":""},"city":{"label":"","value":""},"area":{"label":"丰台区","value":""}},
"geo_api_infot": {"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},
"date": time.strftime('%Y-%m-%d',time.localtime(time.time())),
"fjsj":"",
"jcbhrq": "",
"glksrq":"",
"fxyy": "",
"jcjg": "",
"jcjgt": "",
"qksm": "",
"remark": "",
"jcjgqk": 1,
"jrsflj": "否",
"ljrq": "",
"qwhd": "",
"chdfj": "",
"jrsfdgzgfxdq": "否",
"ddd": "",
"gtshcyjkzt": "正常",
"app_id": "ucas"}

print(str(dic))
print(str(dic).encode("UTF-8"))
appendix = b""
for key in dic:
    if isinstance(dic[key],dict):
        appendix = appendix + ("&" + key + "=" + str(dic[key])).encode("UTF-8")
    elif isinstance(dic[key],int):
        appendix = appendix + ("&" + key + "=" + str(dic[key])).encode("UTF-8")
    elif isinstance(dic[key], str):
        appendix = appendix + ("&" + key + "=" + dic[key]).encode("UTF-8")
    else:
        print(type(dic[key]))
print(appendix)

requests.post("https://app.ucas.ac.cn/ncov/api/default/save",cookies=cookies)
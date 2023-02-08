from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from flask import Flask, request
import json
app = Flask(__name__)
app.debug = True
# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
@app.route("/", methods=['post'])
def check():
# 注意此处添加了chrome_options参数
# 访问登录页面        '
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://accounts.qingflow.com/acc/passport/login')

    # 定位用户名，密码输入框，验证码
    driver.find_element(By.XPATH,"//div/a[contains(text(),'账号密码登录')]").click()
    username = driver.find_element(By.XPATH, '//input[contains(@placeholder,"手机号/邮箱")]').send_keys("18900565298")
    password = driver.find_element(By.XPATH, '//input[contains(@placeholder,"密码")]').send_keys("Wsj123456")
    driver.find_element(By.XPATH,"//button//span[contains(text(),'登录')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//overlay-scrollbars//span[contains(text(),'首页')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[contains(text(),'Exception Record处理')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//button//span[contains(text(),'拒绝')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div/ul/li[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button//span[contains(text(),'确定')]").click()
    a ={"b":"success"}
    driver.quit()
    return  a
if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0",port=8808,debug=True)# # 将自己的用户名密码替换xxxxxx
# username.send_keys('Seven')
# password.send_keys('Seven1234.')
# inputcode.send_keys(res)
#
# # 定位登录按钮并点击
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/form/div[2]/div/div/span/button').click()

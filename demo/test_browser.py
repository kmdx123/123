from time import sleep


def test_we(driver):

    driver.get("http://baidu.com") # 打开浏览器
    sleep(3)
    driver.get("http://jd.com")
    sleep(3)

    driver.back() #后退
    sleep(3)

    driver.forward() #前进
    sleep(3)

    driver.refresh() #刷新
    sleep(2)




    driver.close() # 关闭浏览器,而不退出driver


    driver.quit() # 关闭浏览器,并且退出driver


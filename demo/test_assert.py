from time import sleep


def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    buttons = driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/button[1]/span')
    buttons.click()
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text
    print (text)
    assert "这是一条消息" in text
    sleep(2)


def test_page(driver):
    driver.get("http://ui.yansl.com/#/message")

    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/div').click()
    sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/ul/li/ul/li[3]").click()
    sleep(2)
    scoure = driver.page_source
    print (scoure)
    assert "手工关闭提示" in scoure
    sleep(2)
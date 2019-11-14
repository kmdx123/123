from time import sleep
#第一次修改
import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_input(driver): # 输入框
    driver.get("http://ui.yansl.com/#/input")
    sleep(2) #停留两秒
    input = driver.find_element_by_xpath("//input[@name='t1']")

    input.clear()# 清空

    input.send_keys("我是谁")
    sleep(2)

def test_ridio(driver): # 单选
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    radio.click()# 点击
    sleep(2)

def test_select(driver):# 下拉框
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    select.click()# 点击

    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)# 类的实例化 相当于鼠标键盘
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()# 点击
    sleep(2)

def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)
    slider = driver.find_element_by_xpath("//*[@id='form']/form/div[5]/div/div/div[2]/div")

    sleep(2)
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(slider,0,200).perform()
    sleep(2)

def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)
    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")

    t1.clear() #清空

    t1.send_keys("14:15:00")# 输入数据
    sleep(2)

def test_flie(driver):# 上传文件
    # 打开浏览器
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    flie = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")

    flie.clear() #清空
# 输入数据(文件路径)
    flie.send_keys("C:\\Users\\guoya\\Desktop\\f97dc410d53c4397d4082295c2d73d5.png")

    sleep(2)



def test_flie2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    flie = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button")
    flie.click()
    autoit.win_wait("打开", 10)
    sleep(1)
        # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\guoya\\Desktop\\f97dc410d53c4397d4082295c2d73d5.png")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(2)



def test_alert(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)
    button = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td[2]/input')
    button.click()
    sleep(2)
    alert = driver.switch_to_alert()
    alert.send_keys("sfjkshfjd")
    alert.accept()
    sleep(2)

def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        if driver.title.__contains__("京东"):
            break



def test_iframe(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
    sleep(2)
    frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to_frame(frame)
    sleep(2)
    driver.find_element_by_link_text('京东').click()
    sleep(2)
    driver.switch_to.parent_frame()
    sleep(2)
    iframe = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
    driver.switch_to.frame(iframe)
    sleep(2)
    input = driver.find_element_by_xpath('//*[@id="key"]')
    input.clear()
    input.send_keys("手机")
    sleep(2)

def test_wait(driver):
    driver.get("http://ui.yansl.com/#/loading")
    bt = driver.find_element_by_xpath('//*[@id="test_wait"]/span')
    bt.click()
    driver.implicitly_wait(5) # 隐试等待
    bt1 = driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div')

    print(bt1.text)
    sleep(2)

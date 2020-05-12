#coding=utf-8

from appium import webdriver
import time

class Moke:
    def __init__(self):
        capabilities = {
          "platformName": "Android",
          "deviceName": "FI7TGAYTIBBUVSV8",
          "app": "D:\\Downloads\\imooc7.2.110102001android.apk",
          # "appActivity": "com.imooc.component.imoocmain.splash.MCSplashActivity",
          "appWaitActivity": "com.imooc.component.imoocmain.index.MCMainActivity",
          # "appWaitActivity": "com.imooc.component.imoocmain.splash.GuideActivity",  # 重新安装应用时，需要访问启动页面
            "noReset": "true"  # 不重置应用

        }
        # print("断点")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(6)
        self.driver_width, self.height = self.get_size()

    def get_size(self):
        size = self.driver.get_window_size()
        return size['width'], size['height']

    def swipe_up(self):
        x = self.driver_width / 2
        y = self.height / 10 * 9
        y1 = self.height / 10
        self.driver.swipe(x, y, x, y1)

    def swipe_down(self):
        x = self.driver_width / 2
        y = self.height / 10
        y1 = self.height / 10 * 9
        self.driver.swipe(x, y, x, y1)

    def swipe_left(self):
        x = self.driver_width / 10 * 9
        x1 = self.driver_width / 10
        y = self.height / 2
        self.driver.swipe(x, y, x1, y)

    def swipe_right(self):
        x = self.driver_width / 10
        x1 = self.driver_width / 10 * 9
        y = self.height / 2
        self.driver.swipe(x, y, x1, y)

    def click_page(self, page):
        self.driver.find_element_by_id(page).click()

    def send_keys(self, page, keys):
        self.driver.find_element_by_id(page).send_keys(keys)

    def close(self):
        self.driver.close_app()

mi3 = Moke()
# mi3.swipe_left()
# time.sleep(1)
# mi3.swipe_left()
# time.sleep(1)
# mi3.swipe_left()
# time.sleep(1)
# mi3.click_page("cn.com.open.mooc:id/viewpager")  # 启动页面跳转
# mi3.click_page("cn.com.open.mooc:id/tvSkip")  # 个人定制页面跳转
mi3.click_page("cn.com.open.mooc:id/ivOperation")  # 点击右上角邮件，跳转到注册
# mi3.click_page("cn.com.open.mooc:id/header_line")  # 个人中心页面的东西
mi3.click_page("cn.com.open.mooc:id/right_text")  # 注册跳转到登录
mi3.send_keys("cn.com.open.mooc:id/accountEdit", "userName")
mi3.send_keys("cn.com.open.mooc:id/passwordEdit", "passWord")
mi3.click_page("cn.com.open.mooc:id/login")
time.sleep(10)
mi3.close()
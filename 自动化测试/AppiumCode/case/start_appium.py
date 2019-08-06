#coding=utf-8

from appium import webdriver

capabilities = {
  "platformName": "Android",
  "deviceName": "FI7TGAYTIBBUVSV8",
  "app": "D:\\Downloads\\imooc7.2.110102001android.apk"
}

webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
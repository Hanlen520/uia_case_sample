import time
from basic_uia.basecase import BaseTestCase

APP_NAME = '饿了么'


#  浏览器搜索调起快应用
class TestCase(BaseTestCase):
    def before(self):
        # unlock
        self.device.wakeup()
        self.api.add_to_board(APP_NAME)
        self.device(text="浏览器").click()
        time.sleep(2)

    def start(self):
        self.device(text="搜索或输入网址").click()
        time.sleep(1)
        self.assertTrue(self.device(text="搜索或输入网址").exists)
        self.device(text="取消").left(text="搜索或输入网址").long_click()
        self.device(text="粘贴").click()
        time.sleep(1)
        self.assertTrue(self.device(text="秒开").exists)
        self.device(text="秒开").click()
        time.sleep(2)
        self.assertTrue(self.api.is_quick_app_on())

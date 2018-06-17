"""
此部分用于自定义API
可以组合一些简单动作
"""


class ExtendAPI(object):
    def __init__(self, device, adb, log, origin_api):
        # 调用uiautomator.device
        self.device = device
        # 调用adb命令
        # 例如 self.adb('shell am start ...')
        self.adb = adb
        # 打印分析日志
        self.log = log
        # 使用原生API（basic_uia/api.py）
        # 主要用于 在扩展API中调用原生API
        self.origin_api = origin_api

    def is_quick_app_on(self):
        """ 快应用是否已经被唤起 """
        return bool(
            self.device(resourceId="android.widget.TextView").exists or
            self.device(className="android.widget.TextView").exists
        )

    def is_entry_exist(self, app_name):
        self.device.press.home()
        self.device.press.home()
        for _ in range(3):
            if self.device(text=app_name).exists:
                return True
            else:
                self.device(className="android.view.ViewGroup").swipe.left()
        else:
            return False

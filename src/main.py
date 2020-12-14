
import time
import random
from concurrent.futures import ThreadPoolExecutor
import tkinter


class ILearnShortcutHelper:
    """我把很多代码都写在了这个类里面"""
    def __init__(self):
        """记住，在init函数里带self的变量是本对象的变量，不带self的是普通局部变量"""
        self.top = tkinter.Tk()  # 主要窗体
        self.top.title("快捷键练习")
        self.top.wm_geometry("300x300+500+300")  # 设置长宽，以及在屏幕上的坐标

        self.hint_label = tkinter.Label(self.top, text="请输入？？？", height=10)  # 提示， 设定内容和高度
        self.hint_label.pack()  # 安装到主窗口上

        self.key_map = {"ctrl-c": '\x03', "ctrl-v": '\x16'}  # 键位和对应的码

        self.hint_key = "ctrl-c"  '''记录当前应该输入的快捷键'''

        self.executor = ThreadPoolExecutor(max_workers=1)   # 线程池 贼好用

    def change_hint_label(self, ):
        """用线程池来运行这个函数"""
        self.hint_label.configure(text="请输入...")  # 制造一点延迟的视觉效果
        time.sleep(0.3)
        self.hint_key = list(self.key_map.keys())[random.randint(0, len(self.key_map)-1)]  # 随机选择一个快捷键
        self.hint_label.configure(text="请输入" + self.hint_key)

    def handle_key(self, key_event):
        """主窗口监听键盘事件，交给这个函数执行"""
        print(key_event.char)
        print(self.key_map[self.hint_key])
        if key_event.char == self.key_map[self.hint_key]:  # 如果键入正确，就随机换一个快捷键
            print("==========eq")
            self.executor.submit(self.change_hint_label)  # 主窗口不能有任何阻塞的代码，所以交给别的线程池来运行

    def get_run(self):

        self.change_hint_label()  # 额。。。。
        self.top.clipboard_clear()  # 清空剪贴板，否则键入ctrl v会黏贴东西
        self.top.bind("<Key>", self.handle_key)  # 设定监听键盘事件， 把键盘事件作为参数交给这个函数
        self.top.mainloop()  # 进入消息循环


if __name__ == '__main__':
    ILearnShortcutHelper().get_run()

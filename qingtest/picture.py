import tkinter
import tkinter as tk
from qingtest.globals import g


class wsj:
    def __init__(self):
        self.baseurl_value = None
        self.password_value = None
        self.email_value = None
        self.password = None
        self.email = None
        self.baseurl = None
        self.accessToken_value = None
        self.enviro_value =   None
        # self.get_var_value = None

    def get_picture(self):
        window = tk.Tk()
        window.geometry("800x400")
        window.title("接口自动化工具")
        frame1 = tk.Frame(window)
        frame1.grid()
        tk.Label(frame1, text="请输入baseurl的值:", font=15).grid(row=1, column=0, sticky=tk.E)
        self.baseurl_value = tk.StringVar()
        entry_baseurl = tk.Entry(frame1, textvariable=self.baseurl_value, border=1)
        entry_baseurl.grid(row=1, column=1)
        tk.Label(frame1, text="请输入email的值:", font=15).grid(row=2, column=0, sticky=tk.E)
        self.email_value = tk.StringVar()
        entry_baseurl = tk.Entry(frame1, textvariable=self.email_value, border=1)
        entry_baseurl.grid(row=3, column=1)
        tk.Label(frame1, text="请输入password的值:", font=15).grid(row=3, column=0, sticky=tk.E)
        self.password_value = tk.StringVar()
        entry_baseurl = tk.Entry(frame1, textvariable=self.password_value, border=1)
        entry_baseurl.grid(row=2, column=1)
        tk.Label(frame1, text="请输入accessToken的值:", font=15).grid(row=4, column=0, sticky=tk.E)
        self.accessToken_value = tk.StringVar()
        entry_baseurl = tk.Entry(frame1, textvariable=self.accessToken_value, border=1)
        entry_baseurl.grid(row=4, column=1)
        tk.Label(frame1, text="请输入private/openApi:", font=15).grid(row=5, column=0, sticky=tk.E)
        self.enviro_value = tk.StringVar()
        entry_baseurl = tk.Entry(frame1, textvariable=self.enviro_value, border=1)
        entry_baseurl.grid(row=5, column=1)
        t1 = tk.Button(frame1, text="测试启动", font=10, command=self.get_var_value, bg="blue", fg="#FB9337", width=8,
                       height=3,
                       cursor="hand1", relief="flat", bd=0,)
        t1.grid(row=2, column=2, pady=10, sticky=tk.W)
    def get_var_value(self):
        g.baseurl = self.baseurl_value.get()
        g.password = self.password_value.get()
        g.email = self.email_value.get()
        g.accessToken = self.accessToken_value.get()
        g.enviro = self.enviro_value






# if __name__ == '__main__':
#     wwk = wsj()
#     wwk.get_start()
#     tk.mainloop()

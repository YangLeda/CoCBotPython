
import wx
import win32gui


# custom
import window_capture
import image_match



class HelloFrame(wx.Frame):

    def __init__(self, parent, title):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(parent, title=title, size=(1000,600))
        self.InitUI()
        self.Center()

    def InitUI(self):
        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText("未启动")

        pnl = wx.Panel(self)

        vbox_0 = wx.BoxSizer(wx.VERTICAL)

        hbox_0 = wx.BoxSizer(wx.HORIZONTAL)
        self.start_button = wx.Button(pnl, label = "启动")
        self.start_button.Bind(wx.EVT_BUTTON, self.OnStartBtn)
        hbox_0.Add(self.start_button, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)

        hbox_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.log_tc = wx.TextCtrl(pnl, style=wx.TE_MULTILINE)
        self.log_tc.AppendText("未启动\n")
        #self.result_st = wx.StaticText(pnl, label="未启动")
        #font = self.st.GetFont()
        #font.PointSize += 10
        #font = font.Bold()
        #self.st.SetFont(font)
        hbox_1.Add(self.log_tc, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)

        empty_screenshot_bitmap = wx.Image("ui/empty_screenshot.jpg", wx.BITMAP_TYPE_ANY).Scale(642, 377).ConvertToBitmap()
        self.screenshot_sb = wx.StaticBitmap(pnl, -1, empty_screenshot_bitmap)
        hbox_1.Add(self.screenshot_sb, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)

        vbox_0.Add(hbox_0)
        vbox_0.Add(hbox_1)
        pnl.SetSizer(vbox_0)

    def OnStartBtn(self, event):
        # 获得模拟器窗口句柄
        hwnd = win32gui.FindWindow(0, "夜神模拟器")
        if hwnd != 0:
            self.statusbar.SetStatusText("窗口句柄： " + str(hwnd))
            self.log_tc.AppendText("窗口句柄： " + str(hwnd) + "\n")
        else:
            self.statusbar.SetStatusText("未找到模拟器窗口")
            self.log_tc.AppendText("未找到模拟器窗口\n")

        # 模拟器截图
        window_capture.window_capture(hwnd, "window_capture.jpg")

        # 查找采集水
        result_save_marked = image_match.image_match("window_capture.jpg", "samples/collect_water.jpg")
        # UI显示标记后的截图
        if result_save_marked:
            image = wx.Image("marked.jpg", wx.BITMAP_TYPE_ANY).Scale(642, 377, wx.IMAGE_QUALITY_HIGH)
            self.screenshot_sb.SetBitmap(image.ConvertToBitmap())


if __name__ == '__main__':
    # Create an application object.
    app = wx.App()
    # Then a frame.
    frm = HelloFrame(None, title="Hello World")
    # Show it.
    frm.Show()
    # Start the event loop.
    app.MainLoop()

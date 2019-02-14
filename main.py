
import wx
import win32gui


# custom
import window_capture
import image_match

# debug
import time
import cv2


class HelloFrame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        self.SetSize((800, 600))
        self.Center()

        # create a panel in the frame
        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        self.st = wx.StaticText(pnl, label="Hello World!", pos=(25,25))
        font = self.st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        self.st.SetFont(font)

        open_button = wx.Button(pnl, label = "Start")
        open_button.Bind(wx.EVT_BUTTON, self.OnStart)

        self.screenshot_sb = wx.StaticBitmap(pnl, -1, wx.NullBitmap, (100, 100))

    def OnStart(self, event):
        hwnd = win32gui.FindWindow(0, "夜神模拟器")

        if hwnd != 0:
            self.st.SetLabel(str(hwnd))
        else:
            self.st.SetLabel("未找到模拟器窗口")

        timeStart = time.time()

        # 截图并查找
        window_capture.window_capture(hwnd, "window_capture.jpg")
        result_save_marked = image_match.image_match("window_capture.jpg", "samples/collect_water.jpg")
        
        timeEnd = time.time()
        print(timeEnd - timeStart)

        # UI显示标记后的截图
        if result_save_marked:
            image = wx.Image("marked.jpg", wx.BITMAP_TYPE_ANY)
            image = image.Scale(642, 377, wx.IMAGE_QUALITY_HIGH)
            self.screenshot_sb.SetBitmap(image.ConvertToBitmap())
            #wx.StaticBitmap(self, -1, image.ConvertToBitmap(), (50, 50))

        


if __name__ == '__main__':
    # Create an application object.
    app = wx.App()
    # Then a frame.
    frm = HelloFrame(None, title="Hello World")
    # Show it.
    frm.Show()
    # Start the event loop.
    app.MainLoop()
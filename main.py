
import wx

import win32gui

import time

# 
import window_capture


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

        open_button = wx.Button(pnl, label = "查找模拟器窗口句柄")
        open_button.Bind(wx.EVT_BUTTON, self.OnStart)


    def OnStart(self, event):
        hwnd = win32gui.FindWindow(0, "夜神模拟器")
        print(hwnd)
        if hwnd != 0:
            self.st.SetLabel(str(win32gui.GetWindowRect(hwnd)))
        else:
            self.st.SetLabel("未找到模拟器窗口")

        timeStart = time.time()
        window_capture.window_capture(hwnd, "haha.jpg")
        timeEnd = time.time()
        print(timeEnd - timeStart)
        


if __name__ == '__main__':
    # Create an application object.
    app = wx.App()
    # Then a frame.
    frm = HelloFrame(None, title="Hello World")
    # Show it.
    frm.Show()
    # Start the event loop.
    app.MainLoop()
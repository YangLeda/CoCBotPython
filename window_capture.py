import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import math

def window_capture(hwnd, filepath):

  left, top, right, bot = win32gui.GetClientRect(hwnd)
  w = math.ceil((right - left) *  1.25)
  h = math.ceil((bot - top) *  1.25)
  print(w)
  print(h)

  # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
  hwndDC = win32gui.GetWindowDC(hwnd)
  # 根据窗口的DC获取mfcDC
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcDC创建可兼容的DC
  saveDC = mfcDC.CreateCompatibleDC()
  # 创建bigmap准备保存图片
  saveBitMap = win32ui.CreateBitmap()
  # 为bitmap开辟空间
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # 高度saveDC，将截图保存到saveBitmap中
  saveDC.SelectObject(saveBitMap)


  result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
  print(result)

  bmpinfo = saveBitMap.GetInfo()
  bmpstr = saveBitMap.GetBitmapBits(True)

  im = Image.frombuffer(
      'RGB',
      (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
      bmpstr, 'raw', 'BGRX', 0, 1)

  win32gui.DeleteObject(saveBitMap.GetHandle())
  saveDC.DeleteDC()
  mfcDC.DeleteDC()
  win32gui.ReleaseDC(hwnd, hwndDC)

  if result == 1:
      #PrintWindow Succeeded
      im.save(filepath)
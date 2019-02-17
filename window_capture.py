import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import math

def window_capture(hwnd, filepath):

  left, top, right, bot = win32gui.GetClientRect(hwnd)

  # Windows 10 UI 缩放设置为 125%
  w = math.ceil((right - left) *  1.25)
  h = math.ceil((bot - top) *  1.25)
  
  # 模拟器窗口不能最小化，但可以失去焦点 或被其他窗口遮挡 或不在屏幕范围内
  if w == 0 or h == 0:
    return False

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

  # 后台截图
  result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)

  if result != True:
    return False

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

  im.save(filepath)

  return True

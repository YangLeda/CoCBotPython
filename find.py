import finder as ac

confidencevalue=0.5
imsrc = ac.imread("window_capture.jpg")
imobj = ac.imread("samples/army.jpg")

print (ac.find_all_template(imsrc, imobj))
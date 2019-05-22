import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('movie_1.mp4')
success,image = vidcap.read()
count = 0
offset = 5
counter = 0
success = True
str_3 = ".png"
sciezka_dostępu = "C:/Users/Krystyna/Documents/Convertmp4toim/seq/"
while success:
  if (count % offset) == 0:
    str_buff = "TEST"
    if (counter >-1) and (counter < 10):
      str_1 = sciezka_dostępu + "0000"
      str_2 = str(counter)
      str_buff = str_1 + str_2 + str_3
    if (counter > 9) and (counter < 100):
      str_1 = sciezka_dostępu + "000"
      str_2 = str(counter)
      str_buff = str_1 + str_2 + str_3
    if (counter) > 99 and (counter < 1000):
      str_1 = sciezka_dostępu + "00"
      str_2 = str(counter)
      str_buff = str_1 + str_2 + str_3
    if (counter > 999) and (counter < 10000):
      str_1 = sciezka_dostępu + "0"
      str_2 = str(counter)
      str_buff = str_1 + str_2 + str_3
    cv2.imwrite(str_buff, image)     # save frame as JPEG file
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    print(int(counter))
    counter += 1
  else:
    success, image = vidcap.read()
  count += 1

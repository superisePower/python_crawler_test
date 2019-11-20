import os
import time
import cv2

# 启用PC前置摄像头拍摄  原文：https://juejin.im/post/5d6b31486fb9a06afe12ae5f
nowTime = time.localtime()
filename = "weixinTemp_" + str(nowTime.tm_mday)+str(nowTime.tm_hour)+str(nowTime.tm_min)+str(nowTime.tm_sec)+".jpg"
cap = cv2.VideoCapture(0)
time.sleep(5)  # 延迟 5 秒再读取
ret, img = cap.read()
cv2.imwrite("D:\\"+filename, img)
cap.release()
cv2.destroyAllWindows()
print("照片已保存到了当前目录：" + os.getcwd() + "\n")
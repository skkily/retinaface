#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from retinaface import Retinaface
import tensorflow as tf
import cv2

gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

retinaface = Retinaface()



image = cv2.imread(r"img\timg.jpg")
if image is None:
    print('Open Error! Try again!')
else:
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    r_image = retinaface.detect_image(image)
    r_image = cv2.cvtColor(r_image,cv2.COLOR_RGB2BGR)
    cv2.imshow("after",r_image)
    cv2.waitKey(0)

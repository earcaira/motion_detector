import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    cv2.imshow("Hey",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,resized_image)

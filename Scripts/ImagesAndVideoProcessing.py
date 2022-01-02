## Installing the library ##
    ## pip install opencv-python
    ## import cv2
## Installing the library ##

import cv2
import os
## Loading, Displaying, Resizing and Creating images ##
def resizeImg(OriginalFile):
    path="./Files/images/"
    if os.path.exists(path+OriginalFile):
        img=cv2.imread(path+OriginalFile,1)
        print(type(img))
        #print(img)
        print(img.shape)
        print(img.ndim)

        resize_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
        cv2.imshow("OriginalFile", resize_image)
        if os.path.exists(path+'resized_'+OriginalFile):
            print("Img already exists")
        else:
            cv2.imwrite(path+'resized_'+OriginalFile, resize_image)
            print("Img created succesfull")
        cv2.waitKey(2500)
        cv2.destroyAllWindows()
    else:
        print("File doesn't exist")
# print(img.shape)
## Loading, Displaying, Resizing and Creating images ##

resizeImg('galaxy.jpg')
resizeImg('Lighthouse.jpg')
resizeImg('kangaroos-rain-australia_71370_990x742.jpg')
resizeImg('Moon sinking, sun rising.jpg')
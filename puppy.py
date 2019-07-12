import cv2

img = cv2.imread('DATA/00-puppy.jpg')
new_img = cv2.resize(img, (0,0), img, 0.5, 0.5)

while True:
    cv2.imshow('Puppy', new_img)
    
    # If we've waited atleast 1 ms AND we've pressed Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

        
cv2.destroyAllWindows()
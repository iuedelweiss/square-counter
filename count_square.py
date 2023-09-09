# Copyright (c) 2023 아이유 에델바이스 (iuedelweiss@daum.net)
# The MIT License (MIT)

import cv2
import os
import glob
import pandas as pd

def count_square(filename):
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    # resize for higher resolution
    height, width = image.shape[:2]
    image = cv2.resize(image, (width*2, height*2))
    
    # convert to binary image and find contours
    _, binary_image = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours = contours[:-1] #remove the outer box

    # visualize coutours and label with the count
    for i, contour in enumerate(contours[::-1]):
        cv2.drawContours(image, [contour], -1, (0, 0, 0), 2)
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
            cv2.putText(image, str(i + 1), (cX - 15, cY + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

    cv2.imshow(filename, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return len(contours)


data_dir = 'iuniverse'
output_file = 'result.xlsx'

areas = []
seats = []

image_list = glob.glob(os.path.join(data_dir, '*.png'))
for image_file in image_list:
    seat_count = count_square(image_file)
    areas.append(os.path.basename(image_file).split('.')[0])
    seats.append(seat_count)

areas.append('Total')
seats.append(sum(seats))

df = pd.DataFrame({"area": areas, "seats": seats})
df.to_excel(output_file, index=False)
print(f'Saved results to {output_file}')
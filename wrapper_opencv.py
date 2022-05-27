import cv2,numpy as np
from operator import itemgetter
from glob import glob
import matplotlib.pyplot as plt
import imutils
from math import sqrt

def phytagoras(mat_x_y,  # First coord
               mat_x_y2  # Second coord
               ):
    x = mat_x_y[0]
    y = mat_x_y[1]
    x2 = mat_x_y2[0]
    y2 = mat_x_y2[1]
    result = sqrt((x - x2) ** 2 + (y - y2) ** 2)
    return result

def count_distance_top(mat_x_y,  # First coord
                       mat_x_y2  # Second coord
                       ):
    return mat_x_y[1] - mat_x_y2[1]


def count_distance_bottom(mat_x_y,  # First coord
                          mat_x_y2  # Second coord
                          ):
    return mat_x_y2[1] - mat_x_y[1]


def count_distance_left(mat_x_y,  # First coord
                        mat_x_y2  # Second coord
                        ):
    return mat_x_y[0] - mat_x_y2[0]


def count_distance_right(mat_x_y,  # First coord
                         mat_x_y2  # Second coord
                         ):
    return mat_x_y2[0] - mat_x_y[0]


def warp(frame,  # frame that cropped from closest rect
         M,  # transformation matrix
         size=(672, 936),  # The real Card size
         max_height=500):  # Max height of card result
    warped = cv2.warpPerspective(frame, M, size)
    img = imutils.resize(warped, height=max_height)
    return img

def cnts2warpcoord(cnts,  # All contour
                   current_frame,  # Current frame that cropped from closest rect
                   target_size=None  # target card size
                   ):
    # Sort wrap value
    if target_size is None:
        target_size = [936, 672]

    y_frame, x_frame = current_frame.shape[:2]
    y_target, x_target = target_size[0], target_size[1]

    max_distance = phytagoras(mat_x_y=[0, 0], mat_x_y2=[x_frame, y_frame])

    frame_corner = [[0, 0], [0, y_frame], [x_frame, 0], [x_frame, y_frame]]
    target_mat = [[0, 0], [0, y_target], [x_target, 0], [x_target, y_target]]
    most_lt = []
    most_lb = []
    most_rt = []
    most_rb = []

    tmp_lt = max_distance
    tmp_lb = max_distance
    tmp_rt = max_distance
    tmp_rb = max_distance

    for cnt in cnts:
        cnt = cnt[0]

        # dist1 = phytagoras(cnt, frame_corner[0])
        # dist2 = phytagoras(cnt, frame_corner[1])
        # dist3 = phytagoras(cnt, frame_corner[2])
        # dist4 = phytagoras(cnt, frame_corner[3])

        dist1 = count_distance_top(cnt, frame_corner[0])
        dist2 = count_distance_left(cnt, frame_corner[1])
        dist3 = count_distance_right(cnt, frame_corner[2])
        dist4 = count_distance_bottom(cnt, frame_corner[3])

        if dist1 < tmp_lt:
            most_lt = cnt
            tmp_lt = dist1

        if dist2 < tmp_lb:
            most_lb = cnt
            tmp_lb = dist2

        if dist3 < tmp_rt:
            most_rt = cnt
            tmp_rt = dist3

        if dist4 < tmp_rb:
            most_rb = cnt
            tmp_rb = dist4

    source_mat = [most_lt, most_lb, most_rt, most_rb]
    source_mat = np.array(source_mat, np.float32)
    target_mat = np.array(target_mat, np.float32)
    print('warp 1', np.array(target_mat), np.array(source_mat))
    M = cv2.getPerspectiveTransform(source_mat, target_mat)

    return M, source_mat

morph = cv2.imread("nAlXd.jpg")
morph = cv2.cvtColor(morph, cv2.COLOR_BGR2GRAY)

# orig_im_coor = np.float32([[640, 184], [1002, 409], [211, 625], [589, 940]])
height , width = 450,350
# new_image_coor =  np.float32([[0, 0], [width, 0], [0, height], [width, height]])


                      
# P = cv2.getPerspectiveTransform(orig_im_coor,new_image_coor)

# perspective = cv2.warpPerspective(input_image2,P,(width,height))
# cv2.imshow("Perspective transformation", perspective)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cnts, _ = cv2.findContours(morph.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
x,y,w,h = cv2.boundingRect(cnt)
print(x,y,w,h)

morph = morph[y:y + h, x:x + w]

morph = cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR)
M, source_mat = cnts2warpcoord(cnts=cnt, current_frame=morph)
result = warp(frame=morph, M=M)
for i in source_mat:
    cv2.circle(morph, (i[1], i[0]), 10, color=(255, 0, 0), thickness=-1)

cv2.imshow("Perspective transformation2", morph)
cv2.imshow("Perspective transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
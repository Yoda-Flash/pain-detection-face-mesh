result = detector.detect(img)

y_inner_left_eyebrow_point = result.face_landmarks[0][55].y
y_outer_left_eyebrow_point = result.face_landmarks[0][24].y
y_inner_right_eyebrow_point = result.face_landmarks[0][285].y
y_outer_right_eyebrow_point = result.face_landmarks[0][353].y
y_top_of_left_eye = result.face_landmarks[0][27].y
y_bottom_of_left_eye = result.face_landmarks[0][23].y
y_top_of_right_eye = result.face_landmarks[0][257].y
y_bottom_of_right_eye = result.face_landmarks[0][53].y
y_mouth_corner_left = result.face_landmarks[0][61].y
y_mouth_corner_right = result.face_landmarks[0][291].y
mouth_center = result.face_landmarks[0][0].y

y_inner_left_eyebrow_point_old = result.face_landmarks[0][55].y
y_inner_right_eyebrow_point_old = result.face_landmarks[0][285].y
y_inner_left_eyebrow_point_new = result.face_landmarks[0][55].y
y_inner_right_eyebrow_point_new = result.face_landmarks[0][285].y
y_top_of_left_eye_old =result.face_landmarks[0][27].y
y_top_of_right_eye_old = result.face_landmarks[0][257].y
y_top_of_left_eye_new = result.face_landmarks[0][27].y
y_top_of_right_eye_new = result.face_landmarks[0][257].y
y_mouth_corner_left_new =result.face_landmarks[0][61].y 
y_mouth_corner_right_new = result.face_landmarks[0][291].y
y_mouth_corner_left_old = result.face_landmarks[0][61].y
y_mouth_corner_right_old = result.face_landmarks[0][291].y

if y_inner_left_eyebrow_point < y_outer_left_eyebrow_point \
    or y_inner_right_eyebrow_point < y_outer_right_eyebrow_point:
    if y_top_of_left_eye - y_bottom_of_left_eye < 0.1 \
        or y_top_of_right_eye - y_bottom_of_right_eye < 0.01  \
        or y_mouth_corner_left > mouth_center or \
            y_mouth_corner_right > mouth_center:
            pain = True

elif y_top_of_left_eye - y_bottom_of_left_eye < 0.1 \
    or y_top_of_right_eye - y_bottom_of_right_eye < 0.01:
        if y_inner_left_eyebrow_point < y_outer_left_eyebrow_point \
            or y_inner_right_eyebrow_point < y_outer_right_eyebrow_point \
            or y_mouth_corner_left > mouth_center \
            or y_mouth_corner_right > mouth_center:
            pain = True

elif y_mouth_corner_left > mouth_center \
    or y_mouth_corner_right > mouth_center:
        if y_top_of_left_eye - y_bottom_of_left_eye < 0.1 \
            or y_top_of_right_eye - y_bottom_of_right_eye < 0.01 \
            or y_inner_left_eyebrow_point < y_outer_left_eyebrow_point \
            or y_inner_right_eyebrow_point < y_outer_right_eyebrow_point:
            pain = True

elif y_inner_left_eyebrow_point_old > y_inner_left_eyebrow_point_new \
    or y_inner_right_eyebrow_point_old > y_inner_right_eyebrow_point_new:
        if y_top_of_left_eye_old > y_top_of_left_eye_new \
            or y_top_of_right_eye_old > y_top_of_right_eye_new \
            or y_mouth_corner_left_new > y_mouth_corner_left_old \
            or y_mouth_corner_right_new > y_mouth_corner_right_old:
            pain = True

elif y_mouth_corner_left_new > y_mouth_corner_left_old \
    or y_mouth_corner_right_new > y_mouth_corner_right_old:
        if y_top_of_left_eye_old > y_top_of_left_eye_new \
            or y_top_of_right_eye_old > y_top_of_right_eye_new \
            or y_inner_left_eyebrow_point_old > y_inner_left_eyebrow_point_new \
            or y_inner_right_eyebrow_point_old > y_inner_right_eyebrow_point_new:
            pain = True

elif  y_top_of_left_eye_old > y_top_of_left_eye_new \
    or y_top_of_right_eye_old > y_top_of_right_eye_new:
        if y_mouth_corner_left_new > y_mouth_corner_left_old \
            or y_mouth_corner_right_new > y_mouth_corner_right_old \
            or y_inner_left_eyebrow_point_old > y_inner_left_eyebrow_point_new \
            or y_inner_right_eyebrow_point_old > y_inner_right_eyebrow_point_new:
            pain = True
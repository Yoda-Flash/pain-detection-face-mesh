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


if (y_inner_left_eyebrow_point + y_inner_right_eyebrow_point)/2 > (y_outer_left_eyebrow_point + y_outer_right_eyebrow_point)/2:
    if (y_top_of_left_eye + y_top_of_right_eye)/2- (y_bottom_of_left_eye + y_bottom_of_right_eye)/2 < 0.01  or (y_mouth_corner_left + y_mouth_corner_right)/2 > mouth_center:
            pain = True

elif (y_top_of_left_eye + y_top_of_right_eye)/2- (y_bottom_of_left_eye + y_bottom_of_right_eye)/2 < 0.01:
        if (y_inner_left_eyebrow_point + y_inner_right_eyebrow_point)/2 > (y_outer_left_eyebrow_point + y_outer_right_eyebrow_point)/2 or (y_mouth_corner_left + y_mouth_corner_right)/2 > mouth_center:
            pain = True

elif (y_mouth_corner_left + y_mouth_corner_right)/2 > mouth_center:
        if (y_top_of_left_eye + y_top_of_right_eye)/2- (y_bottom_of_left_eye + y_bottom_of_right_eye)/2 < 0.01 or (y_inner_left_eyebrow_point + y_inner_right_eyebrow_point)/2 > (y_outer_left_eyebrow_point + y_outer_right_eyebrow_point)/2:
            pain = True


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

if (y_inner_left_eyebrow_point_old + y_inner_right_eyebrow_point_old)/2 > (y_inner_left_eyebrow_point_new + y_inner_right_eyebrow_point_new)/2:
    if (y_top_of_left_eye_old + y_top_of_right_eye_old)/2 > (y_top_of_left_eye_new + y_top_of_right_eye_new)/2 or (y_mouth_corner_left_new + y_mouth_corner_right_new)/2 > (y_mouth_corner_left_old + y_mouth_corner_right_old)/2:
        pain = True

elif (y_mouth_corner_left_new + y_mouth_corner_right_new)/2 > (y_mouth_corner_left_old + y_mouth_corner_right_old)/2:
    if (y_top_of_left_eye_old + y_top_of_right_eye_old)/2 > (y_top_of_left_eye_new + y_top_of_right_eye_new)/2 or (y_inner_left_eyebrow_point_old + y_inner_right_eyebrow_point_old)/2 > (y_inner_left_eyebrow_point_new + y_inner_right_eyebrow_point_new)/2:
        pain = True

elif  (y_top_of_left_eye_old + y_top_of_right_eye_old)/2 > (y_top_of_left_eye_new + y_top_of_right_eye_new)/2:
    if (y_inner_left_eyebrow_point_old + y_inner_right_eyebrow_point_old)/2 > (y_inner_left_eyebrow_point_new + y_inner_right_eyebrow_point_new)/2 or (y_mouth_corner_left_new + y_mouth_corner_right_new)/2 > (y_mouth_corner_left_old + y_mouth_corner_right_old)/2:
        pain = True
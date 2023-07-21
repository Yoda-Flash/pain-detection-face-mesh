import redis
import pickle

class Pain:
    # pain = r.set("pain", "False")
    def __init__(self):
        self.redis_client = redis.Redis(host='redis', port=6379, db=0)
        self.target = [{
            "target": 55,
            "condition": ">"
        },
        {
            "target": 285,
            "condition": ">"
        },
        {
            "target": 27,
            "condition": ">"
        },
        {
            "target": 257,
            "condition": ">"
        },
        {
            "target": 61,
            "condition": "<"
        },
        {
            "target": 291,
            "condition": "<"
        }
        ]
    def current(self, id, cur):
        print(f'cur: {cur}')
        return cur[0][id].y

    def initial(self, id):
        return self.init[0][id].y
    # input: landmark_result -> true / false
    def detection(self, current):
        self.init = self.redis_client.get("first_result")
        self.init = pickle.loads(self.init)
        id = []
        counter = 0
        for x in self.target:
            if x.get("condition") == ">":
                if self.initial(x.get("target")) > self.current(x.get("target"), current):
                    counter += 1
                    id.append(self.current(x.get("target"), current))
            elif x.get("condition") == "<":
                if self.initial(x.get("target")) < self.current(x.get("target"), current):
                    counter += 1
                    id.append(self.current(x.get("target"), current))
        if counter >= 2:
            return id
        # if self.initial(55) > self.current(55, current) or self.initial(285) > self.current(285, current):
        #     counter += 1
        #     id.append(self.current(55, current))
        #     id.append(self.current(285, current))
        #
        # elif self.initial(27) > self.current(27, current) or self.initial(257) > self.current(257, current):
        #     counter += 1
        #     id.append(self.current(27, current))
        #     id.append(self.current(257, current))
        #
        # elif self.initial(61) < self.current(61, current) or self.initial(291) < self.current(291, current):
        #     counter += 1
        #     id.append(self.current(61, current))
        #     id.append(self.current(291, current))


    
    # y_inner_left_eyebrow_point_old = init[0][55].y
    # y_inner_right_eyebrow_point_old = init[0][285].y
    # y_inner_left_eyebrow_point_new = current[0][55].y
    # y_inner_right_eyebrow_point_new = current[0][285].y
    # y_top_of_left_eye_old =init[0][27].y
    # y_top_of_right_eye_old = init[0][257].y
    # y_top_of_left_eye_new = init[0][27].y
    # y_top_of_right_eye_new = init[0][257].y
    # y_mouth_corner_left_new =init[0][61].y
    # y_mouth_corner_right_new = init[0][291].y
    # y_mouth_corner_left_old = init[0][61].y
    # y_mouth_corner_right_old = init[0][291].y

    # elif y_mouth_corner_left_new > y_mouth_corner_left_old \
    #     or y_mouth_corner_right_new > y_mouth_corner_right_old:
    #     if y_top_of_left_eye_old > y_top_of_left_eye_new \
    #         or y_top_of_right_eye_old > y_top_of_right_eye_new \
    #         or y_inner_left_eyebrow_point_old > y_inner_left_eyebrow_point_new \
    #             or y_inner_right_eyebrow_point_old > y_inner_right_eyebrow_point_new:
    #             return pain

    # elif  y_top_of_left_eye_old > y_top_of_left_eye_new \
    #     or y_top_of_right_eye_old > y_top_of_right_eye_new:
    #     if y_mouth_corner_left_new > y_mouth_corner_left_old \
    #         or y_mouth_corner_right_new > y_mouth_corner_right_old \
    #         or y_inner_left_eyebrow_point_old > y_inner_left_eyebrow_point_new \
    #             or y_inner_right_eyebrow_point_old > y_inner_right_eyebrow_point_new:
    #             return pain
    
    # if y_inner_left_eyebrow_point < y_outer_left_eyebrow_point \
    #     or y_inner_right_eyebrow_point < y_outer_right_eyebrow_point or \
    #     y_top_of_left_eye - y_bottom_of_left_eye < deadband \
    #     or y_top_of_right_eye - y_bottom_of_right_eye < deadband \
    #     or y_mouth_corner_left > mouth_center or y_mouth_corner_right > mouth_center:
    #             return pain

    # y_inner_left_eyebrow_point = current[0][55].y
    # y_outer_left_eyebrow_point = current[0][24].y
    # y_inner_right_eyebrow_point = current[0][285].y
    # y_outer_right_eyebrow_point = current[0][353].y
    # y_top_of_left_eye = current[0][27].y
    # y_bottom_of_left_eye = current[0][23].y
    # y_top_of_right_eye = current[0][257].y
    # y_bottom_of_right_eye = current[0][53].y
    # y_mouth_corner_left = current[0][61].y
    # y_mouth_corner_right = current[0][291].y
    # mouth_center = current[0][0].y

    # deadband = 0.01

    # elif y_top_of_left_eye - y_bottom_of_left_eye < deadband \
    #     or y_top_of_right_eye - y_bottom_of_right_eye < deadband:
    #     if y_inner_left_eyebrow_point < y_outer_left_eyebrow_point \
    #         or y_inner_right_eyebrow_point < y_outer_right_eyebrow_point \
    #         or y_mouth_corner_left > mouth_center \
    #             or y_mouth_corner_right > mouth_center:
    #             return pain

    # elif y_mouth_corner_left > mouth_center \
    #     or y_mouth_corner_right > mouth_center:
    #     if y_top_of_left_eye - y_bottom_of_left_eye < deadband \
    #         or y_top_of_right_eye - y_bottom_of_right_eye < deadband \
    #         or y_inner_left_eyebrow_point < y_outer_left_eyebrow_point \
    #             or y_inner_right_eyebrow_point < y_outer_right_eyebrow_point:
    #             return pain
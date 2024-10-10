import redis
import pickle
import math
from config import REDIS_HOST

class Pain:
    # pain = r.set("pain", "False")
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.buffer = 5
        self.redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0)
        self.target = [{
            "target": 353,
            "condition": "brows",
            "relative": 359,
        },
        {
            "target": 285,
            "condition": "brows",
            "relative": 463,
        },
        {
            "target": 55,
            "condition": "brows",
            "relative": 243,
        },
        {
            "target": 124,
            "condition": "brows",
            "relative": 130,
        },
        {
            "target": 61,
            "condition": "brows",
            "relative": 0,
        },
        {
            "target": 291,
            "condition": "brows",
            "relative": 0,
        }]

    def current(self, id, cur):
        print(f'cur: {cur}')
        return [cur[id].x, cur[id].y]

    def initial(self, id):
        return [self.init[id].x, self.init[id].y]
    
    # 1920 1080
    def relative(self):
        return 
    
    def get_distance(self, target, landmark):
        # get target object by target id
        # target = self.target.map(lambda x: x == target_id, self.target)
        # return the Euclidean distance by pixel 
        # print(landmark[0])
        target_x = landmark[target.get("target")].x * self.width
        relative_x = landmark[target.get("relative")].x * self.width
        target_y = landmark[target.get("target")].y * self.height
        relative_y = landmark[target.get("relative")].y * self.height
        return math.sqrt(((target_x) - (relative_x)) ** 2 + ((target_y) - (relative_y)) ** 2)


    # initial_distance = [self.get_distance(x, ) for x in self.target]
    # current_distance = 

    # original_distance = math.sqrt( ((initial[0]-relative[0])**2)+((initial[1]-relative[1])**2) )
    # current_distance = math.sqrt( ((current[0]-relative[0])**2)+((current[1]-relative[1])**2) )
    
    # input: landmark_result -increase true / false
    def detection(self, current):
        self.init = self.redis_client.get("first_result")
        self.init = pickle.loads(self.init)[0]
        # print("athena", type(self.init[0]), flush=True)
        # print("athena", (self.init[0][0].x), flush=True)

        id = []
        counter = 0
        for x in self.target:
            if x.get("condition") == "brows":
                if self.get_distance(x, self.init) >= self.get_distance(x, current) - self.buffer:
                    counter += 1
                    id.append(self.current(x.get("target"), current))
            elif x.get("condition") == "mouth":
                # if self.initial(x.get("relative")) - self.initial(x.get("target")) < self.current(x.get("relative"), current) - self.current(x.get("target"), current):
                    counter += 1
                    id.append(self.current(x.get("target"), current))
        if counter >= 2:
            return id
import redis
import pickle
from config import REDIS_HOST

class Pain:
    # pain = r.set("pain", "False")
    def __init__(self):
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
            "condition": "mouth",
            "relative": 0,
        },
        {
            "target": 291,
            "condition": "mouth",
            "relative": 0,
        }]

    def current(self, id, cur):
        print(f'cur: {cur}')
        return cur[0][id].y

    def initial(self, id):
        return self.init[0][id].y
    
    # input: landmark_result -increase true / false
    def detection(self, current):
        self.init = self.redis_client.get("first_result")
        self.init = pickle.loads(self.init)
        id = []
        counter = 0
        for x in self.target:
            if x.get("condition") == "brows":
                if self.initial(x.get("target")) - self.initial(x.get("relative")) < self.current(x.get("target"), current) - self.current(x.get("relative"), current):
                    counter += 1
                    id.append(self.current(x.get("target"), current))
            elif x.get("condition") == "mouth":
                if self.initial(x.get("relative")) - self.initial(x.get("target")) < self.current(x.get("relative"), current) - self.current(x.get("target"), current):
                    counter += 1
                    id.append(self.current(x.get("target"), current))
        if counter >= 2:
            return id
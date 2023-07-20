import redis
import pickle
import json
import time
r = redis.Redis(host='localhost', port=6379, db=0)

result = r.get("current_result")
result = pickle.loads(result)

# TODO: set the result into redis db
# start = time.time()
# # type your code here
# r.set('pickle', pickle.dumps(result))
#
# print(time.time() - start)
#


# TODO: convert the result into xy only and save with hset into redis db
start = time.time()
# result_dict = json.dumps(list(map((lambda x: [r.hset('dict', [i.x, i.y]) for i in x]), result)))
result_dict = json.dumps([i for i in map(lambda x: [[i.x, i.y] for i in x], result)])
# result_dict = json.dumps([[i.x, i.y] for i in result[0]])
# print(result_dict)
r.hset('dict', 'test', result_dict)
# type your code here
print(time.time() - start)


#
# print(result)
# print(result[0][0].x)
# print((result[0]))
# result_dict = map(lambda x: [[i.x, i.y] for i in x], result)
# print(list(result_dict))
# print(json.dumps(list(result)))
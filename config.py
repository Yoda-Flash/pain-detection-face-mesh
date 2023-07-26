import os

REDIS_HOST= os.environ("REDIS_HOST") if os.environ("REDIS_HOST") is not None else "localhost"

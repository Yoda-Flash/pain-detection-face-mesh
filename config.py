import os

REDIS_HOST= os.environ.get("REDIS_HOST") if os.environ.get("REDIS_HOST") is not None else "localhost"

import os

from fastapi_cache.decorator import cache
from motor.motor_asyncio import AsyncIOMotorClient


def nocache(*args, **kwargs):
    def decorator(func):
        return func

    return decorator


DATABASE_URL = os.environ["MONGODB_URL"]
DATABASE_NAME = os.environ["MONGODB_DATABASE_NAME"]
REDIS_URL = os.getenv("REDIS_URL", None)

cache = cache if REDIS_URL else nocache
client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_NAME]

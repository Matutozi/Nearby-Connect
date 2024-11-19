import geocoder
from fastapi import FastAPI
from contextlib import asynccontextmanager
"""
g = geocoder.ip("me")
if g.latlng:
    print(f"Your location is : {g.latlng[0], g.latlng[1]}")
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initialise the database and also do operations before you start recieving requests")
    keys = Keys()
    await initialize_redis(keys)
    yield
    print("Clear resources")

app = FastAPI(lifespan=lifespan)


import redis

# Connect to Redis (adjust host and port if needed)
redis_client = redis.Redis(
    host='localhost',  # or 'redis' if using Docker Compose
    port=6379,         # default Redis port
    db=0,              # default Redis database
)

# Test connection
response = redis_client.ping()
print(response)  # Should print: True

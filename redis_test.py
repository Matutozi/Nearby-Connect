import datetime
from redis_om import HashModel, get_redis_connection
from typing import Optional
from pydantic import StrictInt, field_validator
import redis


redis_connection = get_redis_connection(
    host="localhost",  # Redis host (your Docker container's mapped address)
    port=6379,         # Redis port
     # Optional: Decodes responses to strings
)


class Customer(HashModel):
    first_name : str
    last_name: str
    email : str
    join_date : datetime.date
    age: StrictInt
    bio: Optional[str] = "Super Fun"


    class Meta:
        database = redis_connection

    # Add a field validator for age
    @field_validator("age", mode="before")
    def parse_age(cls, value):
        if isinstance(value, str):
            return int(value)
        return value
     
andrew = Customer(
    first_name="Andrew",
    last_name="Brookins",
    email="andrew.brookins@example.com",
    join_date=datetime.date.today(),
    age=38,
    bio="Python developer, works at Redis, Inc."
)

andrew.save()
print(andrew)

retrieved_customer = Customer.get(andrew.pk)
print(retrieved_customer)
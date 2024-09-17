from pydantic import BaseModel

# Define a Pydantic model for request body


class Message(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 0.0

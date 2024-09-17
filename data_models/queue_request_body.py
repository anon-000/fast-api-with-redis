from pydantic import BaseModel

# Define a Pydantic model for request body


class QueueRequestBody(BaseModel):
    numberOfMessages: int

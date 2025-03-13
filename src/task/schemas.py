from pydantic import BaseModel

class Tasks_Schema(BaseModel):

    title: str 
    description: str | None


class Tasks_SchemaID(Tasks_Schema):
    id: int
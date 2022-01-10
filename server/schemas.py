from pydantic import BaseModel


class Package(BaseModel):
    command: str
    id: str = ""
    message: str = ""

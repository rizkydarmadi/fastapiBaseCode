from pydantic import BaseModel, field_serializer, NonNegativeFloat
from datetime import datetime


class UsersList(BaseModel):
    id: int
    email: str
    user_name: str
    password: float
    is_active: str
    created_at: datetime
    updated_at: datetime | None

    @field_serializer("created_at")
    def serialize_created_at(self, created_at: datetime, _info):
        return created_at.strftime("%Y-%m-%d %H:%M:%S")

    @field_serializer("updated_at")
    def serialize_updated_at(self, updated_at: datetime, _info):
        return updated_at.strftime("%Y-%m-%d %H:%M:%S") if updated_at != None else None


class UsersDetail(BaseModel):
    id: int
    email: str
    user_name: str
    password: float
    is_active: str
    created_at: datetime
    updated_at: datetime | None

    @field_serializer("created_at")
    def serialize_created_at(self, created_at: datetime, _info):
        return created_at.strftime("%Y-%m-%d %H:%M:%S")

    @field_serializer("updated_at")
    def serialize_updated_at(self, updated_at: datetime, _info):
        return updated_at.strftime("%Y-%m-%d %H:%M:%S") if updated_at != None else None


class UserRequest(BaseModel):
    user_name: str
    email: str
    password: str

    class Config:
        from_attributes = True

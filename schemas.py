from typing import Optional

from pydantic import BaseModel, ConfigDict


class SStudentAdd(BaseModel):
    name: str
    description: str


class SStudent(SStudentAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SStudentId(BaseModel):
    ok: bool = True
    student_id: int

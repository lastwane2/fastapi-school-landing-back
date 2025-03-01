from typing import Annotated

from fastapi import APIRouter, Depends

from repository import StudentRepository
from schemas import SStudentAdd, SStudent, SStudentId

router = APIRouter(
    prefix="/students",
    tags=["Ученики"],
)


@router.post("")
async def add_student(
        student: Annotated[SStudentAdd, Depends()],
) -> SStudentId:
    student_id = await StudentRepository.add_one(student)
    return {"ok": True, "student_id": student_id}


@router.get("")
async def get_students() -> list[SStudent]:
    students = await StudentRepository.find_all()
    return students

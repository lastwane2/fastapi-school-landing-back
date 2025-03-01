from sqlalchemy import select

from database import new_session, StudentOrm
from schemas import SStudentAdd, SStudent


class StudentRepository:
    @classmethod
    async def add_one(cls, data: SStudentAdd) -> int:
        async with new_session() as session:
            student_dict = data.model_dump()

            student = StudentOrm(**student_dict)
            session.add(student)
            await session.flush()
            await session.commit()
            return student.id

    @classmethod
    async def find_all(cls) -> list[SStudent]:
        async with new_session() as session:
            query = select(StudentOrm)
            result = await session.execute(query)
            student_models = result.scalars().all()
            student_schemas = [SStudent.model_validate(student_model) for student_model in student_models]
            return student_schemas

from typing import Any
from fastapi import APIRouter, HTTPException
from app.pets.pets_service import pets_service
from app.shared.response_wrapper import ApiResponse
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("", response_model=list[Student])
def find_all():
    return students_service.find_all()


@router.get("/{student_id}", response_model=Student)
def find_by_id(student_id: str):
    return students_service.find_by_id(student_id)


@router.post("", status_code=201, response_model=Student)
def create(body: CreateStudentDto):
    return students_service.create(body)


@router.patch("/{student_id}", response_model=Student)
def update(student_id: str, body: UpdateStudentDto):
    return students_service.update(student_id, body)


@router.delete("/{student_id}", response_model=ApiResponse[Any])
def delete(student_id: str):
    try:
        deleted = students_service.delete(student_id)
        pets_service.delete_all_for_student(student_id)

        return ApiResponse(
            success=True,
            status=200,
            message="Estudiante eliminado correctamente",
            data=deleted
        )
    except HTTPException:
        return ApiResponse(
            success=False,
            status=404,
            message="Estudiante no encontrado",
            data=None
        )
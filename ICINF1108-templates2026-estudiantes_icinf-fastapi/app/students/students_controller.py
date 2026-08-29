from typing import Any
from fastapi import APIRouter, HTTPException
from app.pets.pets_service import pets_service
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service
from app.shared.api_response import ApiResponse

router = APIRouter(prefix="/api/students", tags=["Students"])

@router.get("")
def find_all() -> ApiResponse[list[Student]]:
    estudiantes = students_service.find_all()
    return ApiResponse(
        success=True,
        message="Lista de estudiantes obtenida correctamente",
        data=estudiantes
    )


@router.get("/{student_id}")
def find_by_id(student_id: str) -> ApiResponse[Student]:
    estudiante = students_service.find_by_id(student_id)
    return ApiResponse(
        success=True,
        message="Estudiante encontrado",
        data=estudiante
    )


@router.post("", status_code=201)
def create(body: CreateStudentDto) -> ApiResponse[Student]:
    nuevo_estudiante = students_service.create(body)
    return ApiResponse(
        success=True,
        status=201,
        message="Estudiante creado exitosamente",
        data=nuevo_estudiante
    )


@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto) -> ApiResponse[Student]:
    estudiante_actualizado = students_service.update(student_id, body)
    return ApiResponse(
        success=True,
        status=200,
        message="Estudiante actualizado correctamente",
        data=estudiante_actualizado
    )


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
from fastapi import APIRouter
from app.pets.pets_service import pets_service
from app.shared.response_wrapper import ApiResponse
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all() -> list[Student]:
    return students_service.find_all()


@router.get("/{student_id}")
def find_by_id(student_id: str) -> Student:
    return students_service.find_by_id(student_id)


@router.post("", status_code=201)
def create(body: CreateStudentDto) -> Student:
    return students_service.create(body)


@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto) -> Student:
    return students_service.update(student_id, body)


@router.delete("/{student_id}")
def delete(student_id: str):
    deleted = students_service.delete(student_id)
    
    # Manejo de error si el estudiante no existe (status 404)
    if not deleted:
        return ApiResponse(
            success=False,
            status=404,
            message="Estudiante no encontrado",
            data=None
        )

    # Eliminar las mascotas asociadas al estudiante
    pets_service.delete_all_for_student(student_id)

    # Respuesta exitosa (status 200)
    return ApiResponse(
        success=True,
        status=200,
        message="Estudiante eliminado correctamente",
        data=deleted
    )
from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
<<<<<<< HEAD
from app.shared.api_response import ApiResponse

@router.get("")
def find_all(student_id: str) -> ApiResponse[list[Pet]]:
    mascotas = pets_service.find_all(student_id)
    return ApiResponse(
        success=True,
        message="Lista de mascotas obtenida correctamente",
        data=mascotas
    )

@router.post("", status_code=201)
def create(student_id: str, body: CreatePetDto) -> ApiResponse[Pet]:
    nueva_mascota = pets_service.create(student_id, body)
    return ApiResponse(
        success=True,
        message="Mascota creada exitosamente",
        data=nueva_mascota
    )

@router.patch("/{pet_id}")
def update(student_id: str, pet_id: str, body: UpdatePetDto) -> ApiResponse[Pet]:
    mascota_actualizada = pets_service.update(student_id, pet_id, body)
    return ApiResponse(
        success=True,
        message="Mascota actualizada correctamente",
        data=mascota_actualizada
    )

@router.delete("/{pet_id}", status_code=204)
def delete(student_id: str, pet_id: str):
    pets_service.delete(student_id, pet_id)
    return ApiResponse(
        success=True,
        message="Mascota eliminada correctamente",
        data=None
    )
=======

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str) -> list[Pet]:
    return pets_service.find_all_for_student(studentId)


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> Pet:
    return pets_service.create(studentId, body)


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto) -> Pet:
    return pets_service.update(studentId, petId, body)


@router.delete("/{petId}")
def delete(studentId: str, petId: str) -> Pet:
    return pets_service.delete(studentId, petId)
>>>>>>> 7511bcff5713372d6328dda7822594c4fbbe485a

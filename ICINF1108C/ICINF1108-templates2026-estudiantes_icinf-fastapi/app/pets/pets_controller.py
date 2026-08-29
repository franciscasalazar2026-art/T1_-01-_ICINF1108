from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str):
    pets = pets_service.find_all_for_student(studentId)
    return {
        "success": True,
        "status": 200,
        "message": "Mascotas obtenidas correctamente",
        "data": pets,
    }

        
@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto):
    new_pet = pets_service.create(studentId, body)
    return {
        "success": True,
        "status": 201,
        "message": "Mascota creada correctamente",
        "data": new_pet
    }


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto) -> Pet:
    return pets_service.update(studentId, petId, body)


@router.delete("/{petId}")
def delete(studentId: str, petId: str) -> Pet:
    return pets_service.delete(studentId, petId)

from fastapi import APIRouter
from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str) -> ApiResponse[list[Pet]]:
    pets = pets_service.find_all_for_student(studentId)
    return ApiResponse(
        success=True,
        status=200,
        message="Mascotas obtenidas con éxito",
        data=pets,
    )


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> ApiResponse[Pet]:
    new_pet = pets_service.create(studentId, body)
    return ApiResponse(
        success=True,
        status=201,
        message="Mascota creada correctamente",
        data=new_pet,
    )


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto):
    updated_pet = pets_service.update(studentId, petId, body)
    if not updated_pet:
        return ApiResponse(
            success=False,
            status=404,
            message="Mascota no encontrada",
            data=None,
        )
    return ApiResponse(
        success=True,
        status=200,
        message="Mascota actualizada correctamente",
        data=updated_pet,
    )


@router.delete("/{petId}")
def delete(studentId: str, petId: str):
    deleted_pet = pets_service.delete(studentId, petId)
    if not deleted_pet:
        return ApiResponse(
            success=False,
            status=404,
            message="Mascota no encontrada",
            data=None,
        )
    return ApiResponse(
        success=True,
        status=200,
        message="Mascota eliminada correctamente",
        data=deleted_pet,
    )
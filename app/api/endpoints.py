from fastapi import APIRouter, HTTPException
from app.services.iching_service import IChingService
from app.api.models import (
    ConsultationRequest, 
    ConsultationResponse, 
    HexagramResponse,
    ErrorResponse
)

# Crear los routers
hexagrams = APIRouter()
consultation = APIRouter()

@hexagrams.get(
    "/hexagrams/{number}",
    response_model=HexagramResponse,
    responses={404: {"model": ErrorResponse}}
)
async def get_hexagram(number: int):
    """Obtener un hexagrama específico por número (1-64)"""
    if number < 1 or number > 64:
        raise HTTPException(
            status_code=404, 
            detail="Hexagrama no encontrado. Debe ser un número entre 1 y 64."
        )
    
    hexagram = IChingService.get_hexagram(number)
    if not hexagram:
        raise HTTPException(
            status_code=404, 
            detail=f"Hexagrama {number} no encontrado."
        )
    
    return hexagram

@consultation.post(
    "/consult",
    response_model=ConsultationResponse,
    responses={400: {"model": ErrorResponse}}
)
async def consult_oracle(request: ConsultationRequest):
    """Realizar una consulta al oráculo del I Ching"""
    try:
        result = IChingService.generate_hexagram()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Error al consultar el oráculo: {str(e)}"
        )

@hexagrams.get("/hexagrams", response_model=list[HexagramResponse])
async def get_all_hexagrams():
    """Obtener todos los hexagramas"""
    return IChingService.get_all_hexagrams()

@consultation.post(
    "/consult",
    response_model=ConsultationResponse,
    responses={400: {"model": ErrorResponse}}
)
async def consult_oracle(request: ConsultationRequest):
    """Realizar una consulta al oráculo del I Ching"""
    try:
        result = IChingService.generate_hexagram()
        return {
            "question": request.question,
            "result": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Error al consultar el oráculo: {str(e)}"
        )
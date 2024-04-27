from fastapi import APIRouter, Depends, HTTPException
from .ejemplo_strategy import UAN, UCC, Unimag, UniversidadStrategy
from enum import Enum


class Universidades(Enum):
    UNIMAG = "unimag"
    UCC = "ucc"
    UAN = "uan"


def get_strategy(universidades: Universidades) -> UniversidadStrategy:
    if universidades == Universidades.UNIMAG:
        return Unimag
    elif universidades == Universidades.UCC:
        return UCC
    elif universidades == Universidades.UAN:
        return UAN
    else:
        raise HTTPException(status_code=400, detail="Invalid universidad")


router = APIRouter()


@router.get("/reconocimiento")
def reconocimiento(estrellas:int, universidades: UniversidadStrategy = Depends(get_strategy) ) ->int:
    return universidades.get_reconocimiento(estrellas=estrellas)

@router.get("/costo")
def costo(valor_matricula: float, universidades: UniversidadStrategy = Depends(get_strategy) ) ->int:
    return universidades.get_costo(valor_matricula= valor_matricula)

@router.get("/costo")
def tiempo(origin: int, destination: int, universidades: UniversidadStrategy = Depends(get_strategy) ) ->float:
    return universidades.get_tiempo(origin=origin, destination=destination)
from sqlalchemy import PrimaryKeyConstraint
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class guilda(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    membros: List["membros"] = Relationship(back_populates="guilda")
    missoes: List["missoes"] = Relationship(back_populates="guilda")
    descrição: Optional[str] = None


class membro(SQLModel, table = True):
    id: int
    nome: str
    ap:int # nivel de poder
    guilda_id: int = Field(foreign_key="guilda.id")
    guilda: Optional["guilda"] = Relationship(back_populates="membros")
    hierarquia : "hierarquia" = Relationship(back_populates="membro")


class missao(SQLModel, table = True):
    id: int
    descrição: str
    guilda_id: int = Field(foreign_key="guilda.id")
    guilda: Optional["guilda"] = Relationship(back_populates="missoes")
    qtd_aventureiros_max: int

class cargo(SQLModel, table = True):
    id: int
    nome: str
    hierarquia_em_int : int
    membro_id: int = Field(foreign_key="membro.id")
    membro: Optional["membro"] = Relationship(back_populates="hierarquia")
    # de 1 até 10 sendo 10 o cargo de mais baixo nivel
    atividade: str

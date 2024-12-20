from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import xml.etree.ElementTree as ET
import os

app = FastAPI()
XML_FILE = "livros.xml"

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    genero: str

def inicializar_xml():
    if not os.path.exists(XML_FILE):
        root = ET.Element("livros")
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)

def carregar_livros():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    livros = []
    for livro in root.findall("livro"):
        livros.append({
            "id": int(livro.find("id").text),
            "titulo": livro.find("titulo").text,
            "autor": livro.find("autor").text,
            "ano": int(livro.find("ano").text),
            "genero": livro.find("genero").text,
        })
    return livros

def salvar_livros(livros):
    root = ET.Element("livros")
    for livro in livros:
        livro_elem = ET.Element("livro")

        id_elem = ET.SubElement(livro_elem, "id")
        id_elem.text = str(livro["id"])

        titulo_elem = ET.SubElement(livro_elem, "titulo")
        titulo_elem.text = livro["titulo"]

        autor_elem = ET.SubElement(livro_elem, "autor")
        autor_elem.text = livro["autor"]

        ano_elem = ET.SubElement(livro_elem, "ano")
        ano_elem.text = str(livro["ano"])

        genero_elem = ET.SubElement(livro_elem, "genero")
        genero_elem.text = livro["genero"]

        root.append(livro_elem)

    tree = ET.ElementTree(root)
    tree.write(XML_FILE)

inicializar_xml()

@app.post("/livros", response_model=Livro)
def criar_livro(livro: Livro):
    livros = carregar_livros()
    if any(l.get("id") == livro.id for l in livros):
        raise HTTPException(status_code=400, detail="Livro com esse ID já existe.")

    novo_livro = livro.dict()
    livros.append(novo_livro)
    salvar_livros(livros)
    return novo_livro

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    livros = carregar_livros()
    return livros

@app.get("/livros/{id}", response_model=Livro)
def buscar_livro(id: int):
    livros = carregar_livros()
    livro = next((l for l in livros if l["id"] == id), None)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro

@app.put("/livros/{id}", response_model=Livro)
def atualizar_livro(id: int, dados: Livro):
    livros = carregar_livros()
    livro = next((l for l in livros if l["id"] == id), None)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")

    livro.update(dados.dict())
    salvar_livros(livros)
    return livro

@app.delete("/livros/{id}", response_model=dict)
def deletar_livro(id: int):
    livros = carregar_livros()
    livro = next((l for l in livros if l["id"] == id), None)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")

    livros.remove(livro)
    salvar_livros(livros)
    return {"message": "Livro deletado com sucesso."}

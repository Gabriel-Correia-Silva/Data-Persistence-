from fastapi import FastAPI, HTTPException
from database import get_session, criar_db_and_tables
from models import guilda, membro, missao, cargo
from sqlmodel import select

app = FastAPI()


# Inicializar o banco de dados
@app.on_event("startup")
def startup():
    criar_db_and_tables()




@app.post("/guildas/", response_model=guilda)
def criar_guilda(guilda_data: guilda):
    with get_session() as session:
        session.add(guilda_data)
        session.commit()
        session.refresh(guilda_data)
        return guilda_data


@app.get("/guildas/", response_model=list[guilda])
def listar_guildas():
    with get_session() as session:
        query = session.execute(select(guilda))
        return query.scalars().all()


@app.get("/guildas/{guilda_id}", response_model=guilda)
def obter_guilda(guilda_id: int):
    with get_session() as session:
        g = session.get(guilda, guilda_id)
        if not g:
            raise HTTPException(status_code=404, detail="Guilda não encontrada")
        return g


@app.put("/guildas/{guilda_id}", response_model=guilda)
def atualizar_guilda(guilda_id: int, guilda_data: guilda):
    with get_session() as session:
        g = session.get(guilda, guilda_id)
        if not g:
            raise HTTPException(status_code=404, detail="Guilda não encontrada")
        for key, value in guilda_data.dict(exclude_unset=True).items():
            setattr(g, key, value)
        session.commit()
        session.refresh(g)
        return g


@app.delete("/guildas/{guilda_id}")
def deletar_guilda(guilda_id: int):
    with get_session() as session:
        g = session.get(guilda, guilda_id)
        if not g:
            raise HTTPException(status_code=404, detail="Guilda não encontrada")
        session.delete(g)
        session.commit()
        return {"message": "Guilda deletada com sucesso"}



@app.post("/membros/", response_model=membro)
def criar_membro(membro_data: membro):
    with get_session() as session:
        session.add(membro_data)
        session.commit()
        session.refresh(membro_data)
        return membro_data


@app.get("/membros/", response_model=list[membro])
def listar_membros():
    with get_session() as session:
        query = session.execute(select(membro))
        return query.scalars().all()


@app.get("/membros/{membro_id}", response_model=membro)
def obter_membro(membro_id: int):
    with get_session() as session:
        m = session.get(membro, membro_id)
        if not m:
            raise HTTPException(status_code=404, detail="Membro não encontrado")
        return m


@app.put("/membros/{membro_id}", response_model=membro)
def atualizar_membro(membro_id: int, membro_data: membro):
    with get_session() as session:
        m = session.get(membro, membro_id)
        if not m:
            raise HTTPException(status_code=404, detail="Membro não encontrado")
        for key, value in membro_data.dict(exclude_unset=True).items():
            setattr(m, key, value)
        session.commit()
        session.refresh(m)
        return m


@app.delete("/membros/{membro_id}")
def deletar_membro(membro_id: int):
    with get_session() as session:
        m = session.get(membro, membro_id)
        if not m:
            raise HTTPException(status_code=404, detail="Membro não encontrado")
        session.delete(m)
        session.commit()
        return {"message": "Membro deletado com sucesso"}



@app.post("/missoes/", response_model=missao)
def criar_missao(missao_data: missao):
    with get_session() as session:
        session.add(missao_data)
        session.commit()
        session.refresh(missao_data)
        return missao_data


@app.get("/missoes/", response_model=list[missao])
def listar_missoes():
    with get_session() as session:
        query = session.execute(select(missao))
        return query.scalars().all()


@app.get("/missoes/{missao_id}", response_model=missao)
def obter_missao(missao_id: int):
    with get_session() as session:
        miss = session.get(missao, missao_id)
        if not miss:
            raise HTTPException(status_code=404, detail="Missão não encontrada")
        return miss


@app.put("/missoes/{missao_id}", response_model=missao)
def atualizar_missao(missao_id: int, missao_data: missao):
    with get_session() as session:
        miss = session.get(missao, missao_id)
        if not miss:
            raise HTTPException(status_code=404, detail="Missão não encontrada")
        for key, value in missao_data.dict(exclude_unset=True).items():
            setattr(miss, key, value)
        session.commit()
        session.refresh(miss)
        return miss


@app.delete("/missoes/{missao_id}")
def deletar_missao(missao_id: int):
    with get_session() as session:
        miss = session.get(missao, missao_id)
        if not miss:
            raise HTTPException(status_code=404, detail="Missão não encontrada")
        session.delete(miss)
        session.commit()
        return {"message": "Missão deletada com sucesso"}



@app.post("/cargos/", response_model=cargo)
def criar_cargo(cargo_data: cargo):
    with get_session() as session:
        session.add(cargo_data)
        session.commit()
        session.refresh(cargo_data)
        return cargo_data


@app.get("/cargos/", response_model=list[cargo])
def listar_cargos():
    with get_session() as session:
        query = session.execute(select(cargo))
        return query.scalars().all()


@app.get("/cargos/{cargo_id}", response_model=cargo)
def obter_cargo(cargo_id: int):
    with get_session() as session:
        c = session.get(cargo, cargo_id)
        if not c:
            raise HTTPException(status_code=404, detail="Cargo não encontrado")
        return c


@app.put("/cargos/{cargo_id}", response_model=cargo)
def atualizar_cargo(cargo_id: int, cargo_data: cargo):
    with get_session() as session:
        c = session.get(cargo, cargo_id)
        if not c:
            raise HTTPException(status_code=404, detail="Cargo não encontrado")
        for key, value in cargo_data.dict(exclude_unset=True).items():
            setattr(c, key, value)
        session.commit()
        session.refresh(c)
        return c


@app.delete("/cargos/{cargo_id}")
def deletar_cargo(cargo_id: int):
    with get_session() as session:
        c = session.get(cargo, cargo_id)
        if not c:
            raise HTTPException(status_code=404, detail="Cargo não encontrado")
        session.delete(c)
        session.commit()
        return {"message": "Cargo deletado com sucesso"}

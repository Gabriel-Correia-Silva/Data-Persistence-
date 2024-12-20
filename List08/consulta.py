from database import get_session
from models import membro, cargo, guilda, missao

def listar_membros_com_cargos():
    with get_session() as session:
        resultados = session.query(
            membro.nome.label("nome_membro"),
            membro.ap.label("ap"),
            cargo.nome.label("cargo_nome"),
            cargo.hierarquia_em_int.label("hierarquia"),
            cargo.atividade.label("atividade")
        ).join(cargo, membro.id == cargo.membro_id).all()

        if resultados:
            print("Membros com seus respectivos cargos:")
            for resultado in resultados:
                print(f"- {resultado.nome_membro} (AP: {resultado.ap})")
                print(
                    f"  Cargo: {resultado.cargo_nome}, Hierarquia: {resultado.hierarquia}, Atividade: {resultado.atividade}")
        else:
            print("Nenhum membro com cargo encontrado.")


listar_membros_com_cargos()


def listar_missoes_da_guilda(nome_guilda: str):
    with get_session() as session:
        resultados = session.query(
            missao.descrição.label("descricao_missao"),
            missao.qtd_aventureiros_max.label("max_aventureiros")
        ).join(guilda, missao.guilda_id == guilda.id).filter(guilda.nome == nome_guilda).all()

        if resultados:
            print(f"Missões da guilda '{nome_guilda}':")
            for resultado in resultados:
                print(f"- {resultado.descricao_missao} (Máximo de aventureiros: {resultado.max_aventureiros})")
        else:
            print(f"Nenhuma missão associada à guilda '{nome_guilda}' encontrada.")


listar_missoes_da_guilda("Guilda dos aventureiros")

def listar_membros_e_guildas_com_cargos():
    with get_session() as session:
        resultados = session.query(
            membro.nome.label("nome_membro"),
            membro.ap.label("ap"),
            guilda.nome.label("nome_guilda"),
            cargo.nome.label("nome_cargo")
        ).join(guilda, membro.guilda_id == guilda.id) \
            .join(cargo, membro.id == cargo.membro_id).all()

        if resultados:
            print("Membros, suas guildas e cargos:")
            for resultado in resultados:
                print(f"- {resultado.nome_membro} (AP: {resultado.ap})")
                print(f"  Guilda: {resultado.nome_guilda}, Cargo: {resultado.nome_cargo}")
        else:
            print("Nenhum membro encontrado com guilda ou cargo associado.")


listar_membros_e_guildas_com_cargos()

def guildas_com_membros_de_ap_baixo(ap_limite: int):
    with get_session() as session:
        resultados = session.query(
            guilda.nome.label("nome_guilda"),
            membro.nome.label("nome_membro"),
            membro.ap.label("ap")
        ).join(membro, guilda.id == membro.guilda_id) \
            .filter(membro.ap < ap_limite).all()

        if resultados:
            print(f"Guildas com membros de AP abaixo de {ap_limite}:")
            for resultado in resultados:
                print(f"- Guilda: {resultado.nome_guilda}")
                print(f"  Membro: {resultado.nome_membro} (AP: {resultado.ap})")
        else:
            print(f"Nenhuma guilda possui membros com AP abaixo de {ap_limite}.")


guildas_com_membros_de_ap_baixo(50)


def missoes_acima_de_limite_aventureiros(limite: int):
    with get_session() as session:
        resultados = session.query(
            guilda.nome.label("nome_guilda"),
            missao.descrição.label("descricao_missao"),
            missao.qtd_aventureiros_max.label("max_aventureiros")
        ).join(guilda, missao.guilda_id == guilda.id) \
            .filter(missao.qtd_aventureiros_max > limite).all()

        if resultados:
            print(f"Missões com mais de {limite} aventureiros máximo:")
            for resultado in resultados:
                print(f"- Guilda: {resultado.nome_guilda}")
                print(f"  Missão: {resultado.descricao_missao} (Máx: {resultado.max_aventureiros} aventureiros)")
        else:
            print(f"Nenhuma missão encontrada com mais de {limite} aventureiros máximo.")


missoes_acima_de_limite_aventureiros(5)
from database import get_session
from models import membro, cargo, missao, guilda



def listar_cargos(nome_membro: str):
    with get_session() as session:
        m = session.query(membro).filter(membro.nome == nome_membro).first()
        if m:
            print(f"Cargos de {nome_membro}:")
            if m.hierarquia:
                print(
                    f"- {m.hierarquia.nome} (Nível: {m.hierarquia.hierarquia_em_int}, Atividade: {m.hierarquia.atividade})")
            else:
                print("Nenhum cargo encontrado.")
        else:
            print(f"Membro '{nome_membro}' não encontrado.")


listar_cargos("Arthur")


def listar_cargos_da_guilda(nome_guilda: str):
    with get_session() as session:
        g = session.query(guilda).filter(guilda.nome == nome_guilda).first()
        if g:
            print(f"Cargos da guilda {nome_guilda}:")
            for m in g.membros:
                if m.hierarquia:
                    print(
                        f"- {m.hierarquia.nome} ({m.nome}: Nível {m.hierarquia.hierarquia_em_int}, Atividade: {m.hierarquia.atividade})")
        else:
            print(f"Guilda '{nome_guilda}' não encontrada.")


listar_cargos_da_guilda("Guilda dos aventureiros")


def detalhes_missao(descricao_missao: str):
    with get_session() as session:
        miss = session.query(missao).filter(missao.descrição == descricao_missao).first()
        if miss:
            print(f"Detalhes da missão '{descricao_missao}':")
            print(f"- Guilda: {miss.guilda.nome if miss.guilda else 'Desconhecida'}")
            print(f"- Aventureiros Máximos: {miss.qtd_aventureiros_max}")
        else:
            print(f"Missão '{descricao_missao}' não encontrada.")


detalhes_missao("Recuperar o artefato perdido")


from database import get_session




def listar_membros_com_ap_entre_0_e_10():
    with get_session() as session:
        membros = session.query(membro).filter(membro.ap >= 0, membro.ap <= 10).all()
        if membros:
            print("Membros com AP entre 0 e 10:")
            for m in membros:
                print(f"- {m.nome}: {m.ap} AP")
        else:
            print("Nenhum membro com AP entre 0 e 10 encontrado.")


listar_membros_com_ap_entre_0_e_10()


from database import get_session, criar_db_and_tables
from models import guilda, membro, missao, cargo


# Função para popular o banco
def popular_dados():
    with get_session() as session:
        # Criando guildas
        g1 = guilda(nome="Guilda dos aventureiros", descrição="Guilda focada em missões de resgate")
        g2 = guilda(nome="Guilda dos mercenários", descrição="Guilda especializada em combates e guerras")

        # Adicionando guildas na sessão
        session.add(g1)
        session.add(g2)

        # Criando membros
        m1 = membro(nome="Arthur", ap=80, guilda=g1)
        m2 = membro(nome="Luna", ap=95, guilda=g1)
        m3 = membro(nome="Dark", ap=45, guilda=g2)

        # Adicionando membros na sessão
        session.add(m1)
        session.add(m2)
        session.add(m3)

        # Criando missões
        miss1 = missao(descrição="Recuperar o artefato perdido", guilda=g1, qtd_aventureiros_max=4)
        miss2 = missao(descrição="Derrotar o dragão vermelho", guilda=g1, qtd_aventureiros_max=6)
        miss3 = missao(descrição="Espionar a guilda rival", guilda=g2, qtd_aventureiros_max=2)

        # Adicionando missões na sessão
        session.add(miss1)
        session.add(miss2)
        session.add(miss3)

        # Criando cargos
        c1 = cargo(nome="Líder", hierarquia_em_int=1, membro_id=1, atividade="Coordenação geral")
        c2 = cargo(nome="Guerreiro", hierarquia_em_int=3, membro_id=2, atividade="Missão de combate")
        c3 = cargo(nome="Espião", hierarquia_em_int=5, membro_id=3, atividade="Coletar informações")

        # Adicionando cargos na sessão
        session.add(c1)
        session.add(c2)
        session.add(c3)

        # Salvando alterações no banco
        session.commit()


# Criando as tabelas e populando os dados
criar_db_and_tables()
popular_dados()

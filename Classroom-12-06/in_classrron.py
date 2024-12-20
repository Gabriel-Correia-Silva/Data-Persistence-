import psycopg2

try:
    conn = psycopg2.connect(
        dbname='exemplo',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    
    )

    cursor= conn.cursor()

    try: 
        #criar tabela
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS alunos (
                       id SERIAL PRIMARY KEY,
                       nome TEXT NOT NULL)
                       '''
                       )
        
        #inserir dados
        cursor.execute('INSERT INTO alunos () VALUES (%s)', ('Maria',))
        cursor.execute('INSERT INTO alunos () VALUES (%s)', ('João',))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f'Erro ao executar operacoes no banco de dados')


        #consultar dados
        cursor.execute('')
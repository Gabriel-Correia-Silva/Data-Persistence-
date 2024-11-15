import yaml
dados = {"nome": "alice", "idade": "25", "cursos": ["python", "java"]}

with open("dados.yaml", "w") as file:
    yaml.dump(dados, file)
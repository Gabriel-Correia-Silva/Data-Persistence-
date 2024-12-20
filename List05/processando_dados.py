import json
import logging
import yaml

def carregaConfiguracao(caminho_config):
    with open(caminho_config, 'r') as arquivo:
        return yaml.safe_load(arquivo)

def configuraLogging(config_logging):
    nivel = getattr(logging, config_logging['level'].upper(), logging.INFO)
    logging.basicConfig(
        level=nivel,
        filename=config_logging['file'],
        format=config_logging['format']
    )

def validaRegistro(registro):
    campos_obrigatorios = ['id', 'name', 'age']
    for campo in campos_obrigatorios:
        if campo not in registro or registro[campo] is None:
            return False
    return True

def processaJson(caminho_entrada):
    try:
        with open(caminho_entrada, 'r') as arquivo_entrada:
            dados = json.load(arquivo_entrada)
            logging.info(f"Arquivo {caminho_entrada} lido com sucesso.")
    except (FileNotFoundError, json.JSONDecodeError) as erro:
        logging.error(f"Erro ao ler o arquivo {caminho_entrada}: {erro}")
        return

    registros_validos = []
    registros_invalidos = 0

    for registro in dados:
        if validaRegistro(registro):
            registros_validos.append(registro)
        else:
            registros_invalidos += 1
            logging.warning(f"Registro inválido encontrado: {registro}")

    if registros_validos:
        logging.info(f"{len(registros_validos)} registros válidos processados.")
    if registros_invalidos > 0:
        logging.info(f"{registros_invalidos} registros inválidos encontrados e ignorados.")

if __name__ == "__main__":
    configuracao = carregaConfiguracao('config.yaml')
    configuraLogging(configuracao['logging'])
    processaJson(configuracao['data']['file'])

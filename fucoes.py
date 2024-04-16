from dados import veiculos
from dados import motoristas

def cadastrar_veiculo(veiculo):
    veiculos.append(veiculo)

def listar_veiculos():
    return veiculos

def consultar_veiculo(placa):
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            return veiculo
    return None

def atualizar_veiculo(placa, novo_veiculo):
    for i, veiculo in enumerate(veiculos):
        if veiculo['placa'] == placa:
            veiculos[i] = novo_veiculo
            break

def deletar_veiculo(placa):
    for i, veiculo in enumerate(veiculos):
        if veiculo['placa'] == placa:
            del veiculos[i]
            break

def cadastrar_motorista(motorista):
    motoristas.append(motorista)

def listar_motoristas():
    return motoristas

def consultar_motorista(nome):
    for motorista in motoristas:
        if motorista['nome'] == nome:
            return motorista
    return None

def atualizar_motorista(nome, novo_motorista):
    for i, motorista in enumerate(motoristas):
        if motorista['nome'] == nome:
            motoristas[i] = novo_motorista
            break

def deletar_motorista(nome):
    for i, motorista in enumerate(motoristas):
        if motorista['nome'] == nome:
            del motoristas[i]
            break

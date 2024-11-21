from datetime import datetime
import os


def calcular_idade(data_nasc):
    hoje = datetime.today()
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade


def dados_paciente(nome, email, cpf, rg, tel, data_nasc, arquivo="./aula10/exercicio/lista_pacientes.txt"):
    idade = calcular_idade(data_nasc)
    grupo_risco = idade >= 65
    status_risco = "(Grupo de Risco)" if grupo_risco else ""
    
    dados_paciente  = (
        f"Nome: {nome}\n"
        f"E-mail: {email}\n"
        f"CPF: {cpf}\n"
        f"RG: {rg}\n"
        f"Telefone: {tel}\n"
        f"Data de Nascimento: {data_nasc}"
        f"Idade: {idade}\n"
        f"Grupo de Risco: {status_risco}\n"
        f"{"---" * 50}"
    )

    with open(arquivo, "a") as a:
        a.write(dados_paciente)
        print(f"Paciente {nome} registrado com sucessso!")


def listar_pacientes(arquivo="./aula10/exercicio/lista_pacientes.txt"):
    if not os.path.exists(arquivo):
        print("Não há pacientes registrados ainda.")
        return   
    with open(arquivo, "r") as a:
        print("Pacientes Registrados: ")
        print(a.read())      


def registrar_pacientes():

    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    cpf = input("Digite seu CPF: ")
    rg = input("Digite seu RG: ")
    tel = input("Digite seu telefone: ")
    data_nasc = input("Digite sua da data de nascimento (dd/mm/aaaa): ")

    dados_paciente(nome, email, cpf, rg, tel, data_nasc)


if __name__ == "__main__":
    while True:
        listar_pacientes()
        op = input("Deseja registrar um novo paciente?(s/n) ").lower()
        if op == "s":
            registrar_pacientes()
        elif op == "n":

            print("Programa encerrado!")
            break
        else:
            print("Opcao inválida!")
    

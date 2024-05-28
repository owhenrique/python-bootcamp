import sys

from utils.limpar_tela import LimparTela

from utils.menu_inicial import MenuInicial
from utils.menu_usuario import MenuUsuario
from utils.menu_numero_conta import MenuNumeroConta

from application.criar_usuario import CriarUsuario
from application.criar_conta_corrente import CriarContaCorrente

from application.sacar import Sacar
from application.depositar import Depositar
from application.extrato import Extrato

def main():
    LimparTela()

    usuarios = [{
        "nome": "Paulo Silva",
        "data_nascimento": "24/11/99",
        "cpf": "024",
        "endereco": "Quadra 42 - Leste - Gama/DF"}]
    contas = []
    numero_conta = 1
    
    while True:
        opcao_inicial = MenuInicial()
        LimparTela()
        
        if opcao_inicial == 'q':
            break
        elif opcao_inicial == 'u':
            # criar usuario
            nome_usuario, data_nascimento_usuario, cpf_usuario, endereco_usuario = CriarUsuario(usuarios)
            usuarios.append({
                "nome": nome_usuario,
                "data_nascimento": data_nascimento_usuario,
                "cpf": cpf_usuario,
                "endereco": endereco_usuario
            })
        else:
            # criar conta
            agencia, saida = CriarContaCorrente(contas, usuarios)
            if saida == 'q':
                pass
            else:    
                contas.append({
                    "agencia": agencia,
                    "numero_conta": numero_conta,
                    "usuario": saida,
                    "saldo": 0,
                    "extrato": [{"deposito": []}, {"saque": []}],
                    "saques_realizados": 0,
                })

                numero_conta += 1

        # LimparTela()

        while True:
            opcao_usuario = MenuUsuario()
            LimparTela()

            if opcao_usuario == 'q':
                # sair
                break
            elif opcao_usuario == 's':
                # sacar
                numero_conta = MenuNumeroConta()

                for conta in contas:
                    if conta["numero_conta"] == numero_conta:
                        saldo_apos_saque, extrato_apos_saque, saques_realizados = Sacar(conta=conta)

                        conta["saldo"] = saldo_apos_saque
                        conta["extrato"][1]["saque"].append(extrato_apos_saque)

            elif opcao_usuario == 'd':
                # depositar
                numero_conta = MenuNumeroConta()
                
                for conta in contas:
                    if conta["numero_conta"] == numero_conta:
                        saldo_apos_deposito, extrato_apos_deposito = Depositar(conta)

                        conta["saldo"] = saldo_apos_deposito
                        conta["extrato"][0]["deposito"].append(extrato_apos_deposito)

            elif opcao_usuario == 'c':
                # criar conta
                agencia, saida = CriarContaCorrente(contas, usuarios)
                if saida == 'q':
                    pass
                else:    
                    contas.append({
                        "agencia": agencia,
                        "numero_conta": numero_conta,
                        "usuario": saida,
                        "saldo": 0,
                        "extrato": [{"deposito": []}, {"saque": []}],
                        "saques_realizados": 0,
                    })
                    numero_conta += 1
            else:
                # extrato
                numero_conta = MenuNumeroConta()

                for conta in contas:
                    if conta["numero_conta"] == numero_conta:
                        Extrato(conta["saldo"], extrato=conta["extrato"])
                

if __name__ == "__main__":
    sys.exit(main())
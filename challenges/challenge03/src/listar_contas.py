import textwrap

def listar_contas(contas):
    for conta in contas:
        print('*' * 47)
        print(textwrap.dedent(str(conta)))

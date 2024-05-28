# Otimizando o Sistema Bancário

## Objetivo Geral

Separar as funções existentes em saque, deposíto e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Desafio

Precisamor deixar nosso código mais modularizado, para devemos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos cirar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

## Funções

### Saque

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saque. Sugestão de retorno: saldo e extrato.

### Depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

### Extrato

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, agumentos nomeados: extrato.

## Novas funções

Precisamos criar duas novas funções: criar usuario e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

### Criar usuário

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, numero, bairro, cidade/sigla e estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.

### Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta, e usuário. O número da conta é sequencial, iniciado em 1. o número de agência é fixo: "0001". O usuário pode ter mais de uma conta, mais conta só pertence a somente um usuário.

## ! Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

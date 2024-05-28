# Estuturas de repetição e condicionais em Python

## Identação e Blocos

```python
# É passado um self, um valor e o método não retorna nada -> None

def sacar(self, valor: float) -> None: # inicio do bloco do método
	
	if self.valor >= valor:
		
		self.saldo -= valor
	
	# fim do bloco do if

# fim do bloco do método
```

## Estruturas condicionais

### if/else

```python
saldo = 2000
saque = float(input("Informe o valor: "))

if saldo >= saque:
	print("Realizando o saque")
	
else:
	print("Saldo insuficiente")
```

### if/elif/else

```python
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato"))

if opcao == 1:
	valor = float(input("Digite o valor para saque: "))
	
elif opcao == 2:
	print("Imprimindo extrato")

else:
	sys.out("Opção inválida")
```

### if ternário

```python
status = "SUCESSO" if saldo >= saque else "FALHA"

printf(f"{status} ao realizar o saque!")
```

## Estruturas de repetição

### Comando for

```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")
		
print() # adiciona uma quebra de linha
```

### Função built-in `range`

Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido:

`i, i+1, i+2, i+3, …, j-1`

Ela recebe três argumentos: stop(obrigatório), start (opcional) e step (opcional).

```python
>>> range(4) # retorna um range object
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(0, 16, 5))
[0, 5, 10, 15]

```
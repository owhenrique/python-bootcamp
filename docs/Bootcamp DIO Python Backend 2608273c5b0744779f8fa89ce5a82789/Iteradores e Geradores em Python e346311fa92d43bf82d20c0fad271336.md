# Iteradores e Geradores em Python

Iterador é um objeto que contém um número contável de valores que podem ser iterados, o que significa que você pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais `__iter__()`

e `__next__()` .

Exemplo, ler arquivos grandes:

- Economizar memória evitando carrega todas as linhas do arquivo.
- Iterar linha a linha do arquivo.

```python
class FileIterator:
	def __init__(self, filename):
		self.file = open(filename)
	
	def __iter__(self):
		return self
		
	def __next__(self):
		line = self.file.readline()
		if line != '':
			return line
		else:
			self.file.close()
			raise StopIteration
			
for line in FileIterator('large_file.txt')
	print(line)
```

## Geradores

São tipos especiais de iteradores, ao contário das listas ou outros iteráveis, não armazenam todos os seus valores na memória. São definidos usando funções regulares, mas, ao invés de retornar valores usando `return`, utilizam `yield`.

### Características de geradores

- Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente
- O estado interno de um gerador é mantido entre as chamadas
- A execução de um gerador é pausada na declaração `yield` e retomada daí na próxima vez que ele for chamado

```python
import requests

def fetch_products(api_url, max_pages=100):
	page = 1
	while page <= max_pages:
		response = requests.get(f"{api_url}?page={page}")
		data = response.json()
		for product in data['products']:
			yield product
		if 'next_page' not in data:
			break
		page += 1
		
		
for product in fetch_products("http://api.exempla.com/products"):
	print(product['name'])
```

> Geradores são usados para tarefas mais simples, por exemplo multiplar numeros de uma lista, mas para tarefas mais complexas, como por exemplo, percorrer uma árvore binária e fazer operações em seus nós e folhas.
> 

```python
def meu_gerador(numeros: list[int):
	for numero in numeros:
		yield numero * 2
		
for i in meu_gerador(numeros=[1, 2, 3, 4])
```
# Dicionários em Python

Um dicionários é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por virgulas.

```python
pessoa = {'nome': 'Paulo', 'idade': 28}

pessoa = dict(nome='Paulo', idade=28)

pessoa['telefone'] = '3333-3334'
```

### Acessando valores em dicionários

```python
dados = {'nome': 'Paulo', 'idade': 28, 'telefone': '3333-3333'}

# Slice
dados['nome']      # 'Paulo'
dados['idade']     # 28
dados['telefone']  # '3333-3333'

# Dicionários não permitem a adicição de chaves com o mesmo valor (chaves iguais),
# portanto, quando se adiciona chaves que já existem o valor da chave é alterado.
dados['nome'] = 'Maria'
dados['idade'] = 24

dados  # {'nome': 'Maria', 'idade': 24, 'telefone': '3333-3333'}
```

### Dicionários aninhados

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para este valor seja um objeto imutável como (strings e números).

```python
dados = {
	'paulo': {'nome': 'Paulo', 'idade': 28, 'telefone': '3333-3333'},
	'maria': {'nome': 'Maria', 'idade': 24, 'telefone': '3333-3331'}
}

dados['maria']['idade'] # 24
```

### Iterar dicionários

```python
# Forma menos elegante de se percorrer um dicionário
for chave in contatos:
	print(chave, contatos[chave])
	
# Forma mais elegante
for chave, valor in contatos.items():
	print(chave, valor)
```

## Métodos da classe dict

```python
contatos = {
	'paulo': {'nome': 'Paulo', 'idade': 28, 'telefone': '3333-3333'},
	'maria': {'nome': 'Maria', 'idade': 24, 'telefone': '3333-3331'}
}
```

### Clear

- `clear` : Apaga todos os valores do dicionários
- `copy` : Tira uma cópia do dicionário (similar ao método copy de outras classes)
- `fromkeys` : Cria chaves, em duas situações, a primeira é para criar chaves sem valor 
(`"nome"`: `None`); a segunda é para criar um conjunto de chaves com valor padrão
(`dict.fromkeys([’nome’, ‘telefone’], ‘vazio’)`).
- `get` : Acessar valores dentro do dicionário, ao contrário do slice, acessar chaves que não existem não lançam erros.
    - `contatos.get("chave")`        # keyerror
    - `contatos.get("chave", {})` # {} é o valor padrão de resposta
    - `contatos.get(”paulo”, {})` # 'paulo': {'nome': 'Paulo', 'idade': 28, 'telefone': '3333-3333'},
- `items` : retorna uma lista de tuplas
    
    > **Uma tupla ( tuple ) em Python é uma sequência imutável de valores de qualquer tipo.**
    > 
- `keys` : retorna as chaves de um dicionário
- `pop` :  remove e retonar chaves do dicionário, também podemos passar um valor padrão caso não exista a chave, semelhante ao método `get`
- `popitem`: remove itens na sequência, caso não existem mais chaves, ele lança um keyerror
- `setdefault`: se o atributo estiver no dicionário, ele retorna o dicionário e não altera, caso ele não exista, ele adiciona e retorna o dicionário
- `update`: ele permite que o dicionário seja atualizado, alterando valores que já existem ou criando novos
- `values`: retorna todos os valores amarrados à chaves
- `in`: forma elegante para saber se uma chave existe em um dicionário
    
    ```python
    # Forma menos elegante de verificar se uma chave existe no dicionário
    
    lista_chaves: list = contatos.keys()
    
    has_reference = lista_chaves.count("marcos")
    
    if has_reference:
    	# lógica
    	
    # Forma mais elegante
    
    resultado = 'paulo' in contatos          # True
    resultado = 'idade' in contatos['maria'] # True
    ```
    
- `del`: remove valores de um dicionário, diferente do pop ele não retorna os valores removidos.
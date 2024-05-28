# Herança em POO

Em programação, herança é a capacidade de uma classe filha derivar ou herdas as características e comportamentos da classe pai (base). A classe extende da classe pai.

> É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A
> 

### Sintaxe da herança

```python
class A:
	pass
	
class B(A): # Classe B extende a Classe A
	pass
```

## Herança simples e Herança múltipla

### Herança simples

Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples.

### Herança múltipla

Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.

```python
class A:
	pass

class B:
	pass

class C(A, B):
	pass
```
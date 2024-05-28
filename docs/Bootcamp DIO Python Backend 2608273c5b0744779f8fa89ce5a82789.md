# Bootcamp DIO Python Backend

## Tipos de dados

> Tipos servem para definir as características e comportamentos de um valor (objeto) para o interpretador.
> 

**Tipos básicos em Python**

| Text | str |
| --- | --- |
| Numeric | int, float, complex |
| Sequence | list, tuple, range |
| Map | dict |
| Collection | set, frozenset |
| Boolean | bool |
| Binary | bytes, bytearray, memoryview |

**[Modo interativo](https://wiki.python.org.br/ModoInterativo)**

```bash
$: python3 -i
```

> Método dir retorna uma lista de atributos válidos para objeto fornecido.
> 

```bash
>>> dir(100)
>>> dir("olá mundo")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', \
	'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', \
	'__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', \
	'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', \
	'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', \
	'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', \
	'__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', \
	'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', \
	'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', \
	'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', \
	'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', \
	'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', \
	'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', \
	'translate', 'upper', 'zfill']
>>> "olá mundo".upper()
'OLÁ MUNDO'
```

**Variávies** e **constantes**

> Em linguagens de programção podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de **variáveis**, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.
> 

```python
age, name = (23, 'Paulo')
```

> Assim como as variáveis, **constantes** são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.
> 

**Python não tem constantes**

> Em Python usamos uma convenção para dizer que uma variável é uma constante. Criando uma variável em uppercase, subentende-se que esta variável deve ser uma constante.
> 

```python
DEBUG=True
STATE = [
	'SP',
	'RJ',
	'MG',
]
AMOUNT=30.2
```

## Boas práticas em Python

- Nomes em snake_case  (boas_praticas)
- Nomes sugestivos (limite_saque)
- Nomes de contantes todo em maiúsculo (DEBUG)

## Conversão de tipos

```python
preco = 10

print(float(preco))
>>> 10.0

print(preco)
>>> 10

print(preco / 2)
>>> 5.0

print(preco // 2) // assegura que o retorno será um número inteiro
>>> 5

texto = f'o preco e {preco}' // o f serve para dizer q vão existir variáveis na string
print(texto)
>>> o preco e 10

preco = '10.50'
print(float(preco))
>>> 19.50

print(type(preco))
>>> <class 'str'> // classe do tipo da variáveil
```

## Funções de entrada e saída

```python
nome = input('Informe o seu nome: ')
>>> Informe seu nome: Paulo

print(nome)
>>> Paulo

nome = 'Paulo'
sobrenome = 'Silva'

print(nome, sobrenome)
print(nome, sobrenome, end='...\n') // ao final o output será impresso ... e uma quebra de linha
print(nome, sobrenome, sep='#') // troca o separador pradrão ' ' por '#'

>>> Paulo Silva
>>> Paulo Silva...
>>> Paulo#Silva
```

## Versionamento de código

### Sistemas de controle de versão

Controlam as versões de arquivos ao longo do tempo.

- Registra o histórico de um arquivo;
- Gerencia quais foram as alterações, a data, autor, etc;
- Organização, controle e segurança.

### Tipos de sistema de controle de versão

Dentre os Sistemas de Controle de Versão (VCS), temos:

- VCS Centralizado (CVSC)
    - CVS, Subversion.
- VCS Distribuído (DCVS)
    - Git, Mercurial;
    - Clona o repositório completo, o que inclui o histórico de versões;
    - Cada clone é como um bakcup;
    - Possibilita um fluxo de trabalho flexível;
    - Possibilidade de trabalhar sem conexão à rede.

## Git

Por padrão a branch principal é nomeada como “master”. Porém este nome já não é mais tão utilizado. Para trocar o nome padrão da branch principal ao iniciar um projeto git, utiliza-se: 

```bash
$: git config --global init.defaultBranch main
```

### Autenticação via token

Caso seja necessário utilizar tokens do git e para não precisar salvar o token, ou ficar criando novos token toda vez que for fazer uma ação git, dentro do repositório git local utiliza-se:

```bash
$: git config credential.helper store 
```

Caso seja um pc compartilhado, para salvar o token por tempo determinado, utiliza-se:

```bash
$: git config credential.helper cache
```

Ao utilizar o cache, pode passar uma flag `--timeout <seconds>` para salvar a configuração por tempo determinado. Por padrão o tempo é de 15 minutos. E caso deseje salvar este token em escopo global, basta passar a flag `--global`.

Para criar um arquivo podemos utilizar o comando abaixo:

```bash
$: touch <nome do arquivo> 
```

Para fazer uma alteração em arquivos vazios podemos utilizar o seguinte comando:

```bash
$: echo .gitkeep > .gitignore
```

O comando acima está adicionando o arquivo .gitkeep ao arquivo .gitignore.

### Desfazendo alterações no repositório local

**Árvore de trabalho (working tree):** arquivos que sofreram alterações ou arquivos novos (pré 

`git add`).

**Árvore de preparação (staging area):** arquivos prontos para serem enviados ao repositório remoto (pós `git add`).

Para remover o versionamento Git de um repositório utiliza-se: 

```bash
$: rm -rf .git
```

Para restaurar um arquivo de uma árvore de trabalho, utilizamos: 

```bash
git restore <nome do arquivo>
```

Imagine que fizemos alterações em arquivo sem querer, por exemplo, apagamos uma função importante, com o comando acima iremos desfazer essas alterações. **Atenção**, este comando irá desfazer todas as alterações feitas neste arquivo e não estão “salvas”.

Para remover arquivos da área de preparação utiliza-se:

```bash
$: git restore --staged <nome do arquivo>
```

Para editar informações do commit pode se utilizar:

```bash
$: git commmit --amend -m <mensagem>
```

ou:

```bash
$: git commit --amend 
```

Este comando irá abrir o editor, onde consigo editar várias informações relacionadas ao commit 

Para desfazer o commit e voltar para um commit anterior:

```bash
$: git reset --soft <hash do commit>
```

O `reset --soft` trás o commit de volta, mas mantem os arquivos posteriores ao commit resetado na árvore de preparação.

Uma alternativa ao reset `—soft` é utilizar o `—mixed`, que, diferente do `—soft`, ele adiciona os arquivos à árvore de trabalho. Por padrão o `git reset` já é um `--mixed` então não é preciso passar esta flag. Também existe a flag `--hard`, que, diferente de ambos, não trás os arquivos posteriores ao commit nem à árvore de preparação e nem à de trabalho. 

**O ideial é que essas alterações sejam feitas antes de enviar o commit ao repositório remoto, pois, essas alterações podem causar conflitos.**

Uma alternativa ao comando `git log` é o `git reflog` que trás informações adicionais sobre os commits. 

### Trabalhando com branchs

> Uma branch (tradução, “Ramo”) é uma ramificação do seu projeto. Uma branch é um ponteiro móvel para um commit no histórico do repositório. Quando você cria uma nova branch a partir de uma existente, a nova se inicia apontando para o mesmo commit da branch que estava quando foi criada.
> 

Para conectar um repositório remoto ao seu repositório local, utiliza-se:

```bash
$: git add -u remote origin <link do repositório remoto>
```

A flag `-u` é para indicar o upstream.

> **Upstream** é tudo que você insere no git: criar um repositório no git, fazer um commit, fazer um push. **Downstream** é tudo que você pega do git: clonar um repositório, fazer um pull.
> 
> 
> **Ramificação** é o branch, ou seja um repositório paralelo.
> 

Para listar o último commit de cada branch, utiliza-se:

```bash
$: git branch -v
```

Para deletar uma branch, utiliza-se:

```bash
$: git branch -d <nome da branch>
```

Para baixar os commits no repositório remoto, sem mergear (git pull + git merge), utiliza-se:

```bash
$: git fetch
```

E para visualizar as diferenças entre o repositório local e o repositório remoto (origin/main):

```bash
$: git diff main origin/main // ou o nome da branch no servidor
```

E após trazer as mudanças presentes no repositório remoto, para mesclar as mudanças com o repositório local, utiliza-se: 

```bash
$: git merge origin/main // ou o nome da branch no servidor 
```

Para clonarmos apenas uma branch podemos utilizar o comando:

```bash
$: git clone <link do repositório> --branch <nome da branch> --single-branch
```

Caso não seja indicado qual branch clocar após a flag `—branch`, apenas clonaremos a branch principal. 

O comando `git stash` arquiva a última modificação feita no repositório, ou seja, as modificações na árvore de trabalho, e assim poderemos, por exemplo, criar uma nova branch sem as modificações feitas.

- O comando `git stash list` tras todas as modificações feitas e arquivadas.
- O comando `git stash pop` joga fora todas as modificações arquivadas.
- O comando `git stash apply` aplica todas as modificações arquivadas.

[Tipos de operadores em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Tipos%20de%20operadores%20em%20Python%20839d03f987684325b2b9adbed31a296e.md)

[Estuturas de repetição e condicionais em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Estuturas%20de%20repetic%CC%A7a%CC%83o%20e%20condicionais%20em%20Python%204b8899c1c2654ae1a0cf2e593ff8794b.md)

[Manipulando Strings](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Manipulando%20Strings%200f0205ff45104d639ceb4827959df442.md)

[Trabalhando com listas em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Trabalhando%20com%20listas%20em%20Python%20940af588fb43407a8456ee2866cdc442.md)

[Conhecendo tuplas em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Conhecendo%20tuplas%20em%20Python%206588a91ba73444b0b3f3011f3e8952f7.md)

[Explorando conjuntos em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Explorando%20conjuntos%20em%20Python%201faf157139b246f0a47091ee32da3858.md)

[Dicionários em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Diciona%CC%81rios%20em%20Python%203c274e27701d4e80bd2400e492aaeb83.md)

[Dominando funções em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Dominando%20func%CC%A7o%CC%83es%20em%20Python%20f82df64f4da649df8cda93a9a231e040.md)

[Programação Orientada a Objetos](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Programac%CC%A7a%CC%83o%20Orientada%20a%20Objetos%20f595981f79684f19961fbafef76894ee.md)

[Herança em POO](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Heranc%CC%A7a%20em%20POO%2022b134fb6ca549d0946ac4a900f7cc68.md)

[Encapsulamento em Python](Bootcamp%20DIO%20Python%20Backend%202608273c5b0744779f8fa89ce5a82789/Encapsulamento%20em%20Python%20c9939e35d3014f41849d087e957c2d42.md)
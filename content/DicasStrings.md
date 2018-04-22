Title: Dicas de manipulação de Strings em Python
Date: 2018-04-21 19:23
Modified: 2018-04-21 19:23
Category: Python
Tags: python, strings, dicas 
Slug: dicas-strings
Authors: Eliézer
Summary: Algumas dicas de manipulação de Strings em python

# Aspas
Aspas simples e duplas são tratadas da mesma forma em Python. Não há diferença.
Isso é util quando for inserir uma aspa dentro de uma string. Três aspas podem ser utilizadas para strings muito grandes.

```python
print('''"Heeded my words not, did you?
     Pass on what you have learned.
     Strength, mastery. But weakness, folly, failure also.
     Yes, failure most of all.
     The greatest teacher, failure is.
     Luke, we are what they grow beyond.
     That is the true burden of all masters."
     — Master Yoda''')
```

# True ou False?

Quando uma string é vazia ela retorna False e True quando está preenchida.

```python
s = "May the Force be with you."
if s:
    print("Tem conteúdo!")

s = ""
if not s:
    print("Está vazio")
```

# Adição e multiplicação de Strings

```python
s = ' the '
print('Fell'+s+'Force.')
```

```Fell the Force.```

```python
print('*'*50)
```

```**************************************************```


# Interpolação de Strings
## Utilizando %
É a forma mais antiga. Não é muito usado atualmente.

```python
j = 'Jedi'
f = 'Force'

print("A %s" % j)

print("A %s uses the %s for knowledge and defense, never for attack." % (j, f))

print("A %(x)s uses the %(y)s for knowledge and defense, never for attack." % ({"x": j, "y": f}))

'A Jedi uses the Force for knowledge and defense, never for attack.'
```

## Utilizando .format()

```python
print("A {} uses the {} for knowledge and defense, never for attack.".format(j, f))

print("A {x} uses the {y} for knowledge and defense, never for attack.".format(x=j, y=f))

print("A {0} uses the {1} for knowledge and defense, never for attack.".format(j, f))

'A Jedi uses the Force for knowledge and defense, never for attack.'
```

## Utilizando f-strings

A partir do Python 3.6, onde você pode utilizar as variáveis diretamente dentro da String.

```python
print(f"A {j} uses the {f} for knowledge and defense, never for attack.")
'A Jedi uses the Force for knowledge and defense, never for attack.'

print(f"A {j.upper()} uses the {f.upper()} for knowledge and defense, never for attack.")
'A JEDI uses the FORCE for knowledge and defense, never for attack.'
```

# Inspeção de Conteúdo
```python
s = "Feel the Force"

len(s)
14

s.startswith('Feel')
True

s.endswith('Force')
True

"the" in s
True

s.find('Force')
9

s.index('the')
5
```

# Slicing
Dividindo strings
```python
s = 'Patience you must have my young Padawan.'

s[0]
'P'

s[0:8]
'Patience'

s[-2]
'n'

s[::-1]
'.nawadaP gnuoy ym evah tsum uoy ecneitaP'
```

# Transformação
```python
'fell the force.'.title()
'Fell The Force.'

'fell the force.'.capitalize()
'Fell the force.'

'fell the force.'.upper()
'FELL THE FORCE.'

'FELL THE FORCE.'.lower()
'fell the force.'

'Fell The Force.'.swapcase()
'fELL tHE fORCE.'

'fell the force.'.replace('force', '*')
'fell the *.'

'   fell the force.   '.strip()
'fell the force.'

'   fell the force.   '.lstrip()
'fell the force.   '

'   fell the force.   '.rstrip()
'   fell the force.'

'42'.zfill(10)
'0000000042'

```

# Listas e Strings
## De lista para string
```python
l = ['Do.', 'Or', 'do', 'not.', 'There', 'is', 'no', 'try.']
' '.join(l)
'Do. Or do not. There is no try.'
```

## De String para lista
```python
s = 'Do. Or do not. There is no try.'

s.split()
['Do.', 'Or', 'do', 'not.', 'There', 'is', 'no', 'try.']

s.split(None, 1)
['Do.', 'Or do not. There is no try.']

s.split('.')
['Do', ' Or do not', ' There is no try', '']
```

# Iterar uma String
```python
s = 'Truly wonderful, the mind of a child is.'
for c in s:
    print(c)
```

T
r
u
l
y
 
w
o
n
d
e
r
f
u
l
,
 
t
h
e
 
m
i
n
d
 
o
f
 
a
 
c
h
i
l
d
 
i
s
.


[Estes exemplos estão disponíveis em meu repositório do GitHub](https://github.com/eliezerfb/python_tests/blob/master/manipulacao_strings/Manipula%C3%A7%C3%A3o%20de%20Strings.ipynb)

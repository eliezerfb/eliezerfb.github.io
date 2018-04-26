Title: Data Cleaning em marcas de veículos
Date: 2018-04-26 18:58
Modified: 2018-04-26 18:58
Category: Data Science
Tags: data science, data cleaning, 
Slug: data-cleaning-marca-veiculo
Authors: Eliézer
Summary: Exemplo de data cleaning em um dataset de marcas de veículos

Em ciência de dados é comum encontrar datasets onde é necessário realizar algum trabalho de limpeza de dados. Seja por erros de digitação ou algum problema na coleta de dados. Costuma-se dizer que 80% da análise de dados é gasto no processo de limpeza e preparação dos dados, (Dasu e Johnson 2003).

Neste post mostro um exemplo de limpeza de dados em um caso onde foi necessário realizar a padronização de nomes de marcas de veículos (caminhões e carretas). Por desconhecimento ao realizar o cadastros dos veículos em um sistema os usuário acabaram informando o modelo do veículo no mesmo campo da marca. Neste dataset existem 898 veículos, sendo que em 49% apresentavam este problema.

A primeira coisa a ser feitas foi verificar quantas formas únicas existiam:

```python
df_veiculos['MARCA'].unique()
```

No total haviam 214 tipos diferentes de marcas cadastradas, onde além do problema do modelo misturado com a marca, havia também problemas na ortografia (exemplo: 'MERCEDES BENZ', 'MERCEDES-BENZ', 'MERCEDES BENZA', 'MERCEDZ BENS’).

Para começar a limpeza a primeira coisa removi os números e caracteres estranhos encontrados:

```python
df_veiculos['MARCA'] = df_veiculos['MARCA'].str.replace(r'[^A-Za-z]+', ' ')
```

E substituí os valores nulos por espaço em branco: 

```python
df_veiculos['MARCA'].replace(np.nan, '', inplace=True)
```

Para ajudar a remover as letras isoladas que restaram, também adicionei espaços em branco extra:

```python
df_veiculos['MARCA'] = ' '+df_veiculos['MARCA']+' '
```

Apenas com esse tratamento já foi possível reduzir de 214 para 157 marcas únicas.

Normalmente as marcas possuem mais de 3 caracteres, com algumas exceções como 'MAN', 'DAF', 'MWM', 'VW' e 'M' (Sendo que ‘M’ se refere a MERCEDES-BENZ). O restante eliminei pois se tratavam de siglas que não deveriam de ser informadas:

```python
def replacevalues(df, column, search, replace):
    for item in search:
        r = re.compile(' '+item+' ', flags=re.IGNORECASE)
        df[column] = df[column].str.replace(r, replace)

dont_remove = ['MAN', 'DAF', 'MWM', 'VW', 'M']

# Para o restante das marcas, cria uma lista para remoção
remove = [x.split() for x in df_veiculos['MARCA'].unique()]
remove = [item for sublist in remove for item in sublist]
remove = [item for item in remove if len(item) <= 3 and item not in dont_remove]

replacevalues(df_veiculos, 'MARCA', remove, ' ')

```

Depois disso, verifiquei que algumas palavras que tinham mais que 3 caracteres, deveriam ser removidas também:

```python
remove = ['SRCA', 'SRCS', 'PRANCHA', 'SRFG', 'STRALIS', 'CARGA', 'CARGO',
          'AXOR', 'ATEGO', 'ACTROS', 'ABERT', 'CHARGER', 'STRALYS', 'SYDER',
          'PORTA CONTAINER', 'CAVALO', 'SEMI REBOQUE', 'TRUCK', 'REBOQUE',
          'TRAC TRATOR']
replacevalues(df_veiculos, 'MARCA', remove, ' ')

```

Após, removi os espaços em branco extras:

```python
df_veiculos['MARCA'] = df_veiculos['MARCA'].str.strip()
```

Nesse momento o número de marcas únicas reduziu para 57.

Algumas inconsistências tiveram de ser corrigidas de forma direta. Algumas abreviações, erros muito grandes ou duas marcas para o mesmo veículo:

```python
df_veiculos['MARCA'].replace({'VOLKSWAGEN MAN': 'VOLKSWAGEN',
                              'VOLKS MAN': 'VOLKSWAGEN',
                              'VOLKS': 'VOLKSWAGEN',
                              'VW MWM': 'VOLKSWAGEN',
                              'VW': 'VOLKSWAGEN',
                              'M BENZ': 'MERCEDES-BENZ',
                              'MERCEDES': 'MERCEDES-BENZ',
                              'SCANIA RANDON': 'SCANIA',
                              'NOPIA': 'NOMA'},
                             inplace=True)
```

Chegou-se assim no seguinte conjunto de marcas:

```python

       ['', 'VOLKSWAGEN', 'GUERRA', 'SCANIA', 'MERCEDES BENZ',
       'LOIBRELATTO', 'FACCHINI', 'RANDON', 'LIBRELATTO', 'FORD', 'VOLVO',
       'FACHINI', 'JARDINOX', 'RECRUSUL', 'MERCEDES-BENZ', 'IVECO',
       'KRONE', 'MAN', 'TRIEL', 'RODOLINEA', 'FIBRASIL', 'NOMA', 'SOUFER',
       'SCHIFFER', 'RANSON', 'LIBRELATO', 'MARINO', 'GURRA', 'MANN',
       'MERCEDZ BENS', 'FACCHINI TANQUE', 'FACCIHINI', 'RANDONSP', 'GUERA',
       'ELLFEN', 'LIBERATO', 'DAF', 'VOVLO', 'IDAF', 'MERCEDES BENZA',
       'RANDN', 'FACCHIN', 'VOLKSWAGEM', 'RAMDON', 'RODOTECNICA', 'FORS',
       'THERMOSUL', 'NOMAQ', 'FACHIN']

```

Já é possível perceber uma significativa melhora. Agora só resta algumas marcas com erros de grafia. Para corrigir isso utilizei a biblioteca *fuzzywuzzy*. Com base em uma lista de marcas corretas, esta biblioteca permite realizar uma comparação e se determinada string possuir uma semelhança mínima ela é substituída. Eu utilizei uma taxa de semelhança 70%, visto que marcas normalmente possuem diferenças significativas em sua grafia. Em outros casos é necessário utilizar taxas maiores.

```python
def replace_matches_in_column(df, column, string_to_match, min_ratio=90, only_test=False):
    # function to replace rows in the provided column of the provided dataframe
    # that match the provided string above the provided ratio with
    # the provided string

    # get a list of unique strings
    strings = df[column].unique()

    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings,
                                         limit=10,
                                         scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > x
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]
    if len(close_matches) > 0:
        print(string_to_match, ':', close_matches)

    if not(only_test):
        # get the rows of all the close matches in our dataframe
        rows_with_matches = df[column].isin(close_matches)

        # replace all rows with close matches with the input matches
        df.loc[rows_with_matches, column] = string_to_match

for marca in df_marcas_ok['NOME']:
    replace_matches_in_column(df=df_veiculos, column='MARCA', 
                              string_to_match=marca, min_ratio=70)
	
```

Finalmente, chegou-se ao número de 25 marcas únicas, que corresponde uma redução de 88%. Nos veículos que apenas foi informado o modelo do veículo foi necessário uma rápida pesquisa na internet e definiu-se manualmente:

```python
def set_marcas(codigos, marca):
    rows = df_veiculos['CODIGO'].isin(codigos)
    df_veiculos.loc[rows, 'MARCA'] = marca

set_marcas(codigos=[57, 392], marca='VOLVO')
set_marcas(codigos=[544, 609, 696], marca='VOLKSWAGEN')
set_marcas(codigos=[70, 207, 210, 880], marca='MERCEDES-BENZ')
set_marcas(codigos=[165], marca='IVECO')
set_marcas(codigos=[202, 282], marca='FORD')
set_marcas(codigos=[792], marca='SCANIA')
set_marcas(codigos=[72], marca='GUERRA')
set_marcas(codigos=[213], marca='LIBRELATTO')

```

Já os veículos que originalmente não possuíam esta informação, foi definido como marca não especificada:

```python
nao_especificado = df_veiculos[df_veiculos['MARCA'] == '']['CODIGO']
set_marcas(codigos=nao_especificado, marca='NAO ESPEC.')
```

Considerando no total do dataset, os veículos com problema na marca caíram de 49% para 7%. Somente ficaram sem a informação da marca os veículos que originalmente não possuíam essa informação.

Dificilmente algum dataset no mundo real é perfeito, livre de problemas. A etapa de higienização dos dados é muito importante para que a análise seja realizada de forma correta. Apesar deste código estar de forma linear, este foi um processo cíclico onde o resultado final era avaliado e melhorado.

O código completo está disponível no [GitHub](https://github.com/eliezerfb/data-cleaning/tree/master/marcas-veiculos).





Title: Dicas de Data Cleaning
Date: 2018-03-31 20:23
Modified: 2018-04-02 21:07
Category: Data Science
Tags: data science, data cleaning, 
Slug: dicas-cata-cleaning
Authors: Eliézer
Summary: Algumas dicas e para efetuar limpeza em dados

O processo de limpeza e preparação dos dados representa cerca de 80% do trabalho de um cientista de dados. Datas em diversos formatos, diversos encodings, dados incompletos, erros de digitação são muito comuns. Antes de realizar qualquer análise é necessário tratar estes problemas. Neste post reúno algumas dicas de pré-processamento que são úteis no dia-a-dia.

# Manipulação de Dados Faltantes

Para obter o número de pontos de dados perdidos por coluna, podemos utilizar o código:

    missing_values_count = df.isnull().sum()
    total_cells = np.product(df.shape)
    total_missing = missing_values_count.sum()
    print((total_missing/total_cells) * 100)

Também podemos visualizar os dados faltantes com a ajuda da biblioteca [missingno](https://github.com/ResidentMario/missingno){:target="_blank"}. 

    pip install missingno
    
Esta biblioteca permite diversas visualizações, abaixo é possível ver um exemplo de código:    

    from quilt.data.ResidentMario import missingno_data
    collisions = missingno_data.nyc_injurious_collisions()
    collisions = collisions.replace("nan", np.nan)
    import missingno as msno
    %matplotlib inline
    msno.matrix(collisions.sample(250))

![msgno example](/images/msgno.png){:height="90%" width="90%" class="img-responsive"}

Mas nem todos dados faltantes são erros. Nesse momento é necessário se perguntar: **um dado faltante é porque não foi gravado ou porque não existe?**

Se um valor é faltante porque ele não existe (como a altura do filho mais velho de quem não tem filhos), então não faz sentido tentar adivinhar este valor. Estes valores devem ser mantidos como NaN. Por outro lado, se um valor não existe porque não foi gravado, então podemos tentar adivinhar seu valor baseado em outros valores nesta coluna e linha. 

## Descartar valores ausentes

Se não houver uma razão para descobrir por que os valores estão faltando, uma opção é apenas remover as linhas ou colunas que contiverem valores ausentes. Porém esta abordagem não é muito recomendada, principalmente em projetos importantes. Vale a pena dedicar um tempo para analisar os dados e observar todas as colunas com valores ausentes um a um para realmente conhecer o dataset.  

O código abaixo remove todas as linhas que contém um valor faltante:  

    df.dropna()

E para remover todas as colunas que contiver um valor faltante, basta informar axis=1:  

    df.dropna(axis=1)

## Preencher valores ausentes automáticamente

Outra opção é tentar preencher os valores ausentes. Para preencher todos NaN com zero:  

    df.fillna(0)

Para um conjunto de dados que possuem uma ordem lógica pode ser feito dessa forma:  

    df.fillna(method = 'bfill', axis=0).fillna("0")

O método bfill preenche os valores ausentes com qualquer valor que venha diretamente após ele na mesma coluna. Um exemplo de uso pode ser na observação de temperatura ou dados pluviométricos.  

# Converter colunas date para datetime

Colunas tipo data que são reconhecidas como texto devem ser convertidas para ser reconhecidas como uma data. Este procedimento chama-se "parsing dates" porque nós pegamos uma string e indentificamos suas partes.  
Para formatar as datas com o pandas nós utilizamos um guia chamado [strftime directive](http://strftime.org){:target="_blank"}. A ideia básica é que você precisa indicar quais partes da data estão onde e qual pontuação está entre elas. Há muitas possibilidades de partes de data, mas a mais comum são %d para dia, %m para mês, %y para ano de dois dígitos e %Y para ano de quatro dígitos.  

Alguns exemplos:

* 1/17/07 tem o formato "%m/%d/%y"
* 17-1-2007 tem o formato "%d-%m-%Y"

Para converter uma coluna data:

    df['date_parsed'] = pd.to_datetime(df['date'], format = "%m/%d/%y")

Mesmo especificando o formato de data, às vezes obtém-se um erro quando houver vários formatos de data em umam única coluna. Se isso acontecer, pode tentarr utilizar o pandas para inferir qual deve ser o formato correto. Isso pode ser feito da seguinte maneira:

    df['date_parsed'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

**Porque não usar sempre infer_datetime_format = True?** Há dois grandes motivos para não deixar o pandas adivinhar o formato da data/hora. A primeira é que o pandas nem sempre é capaz de descobrir o formato correto, especialmente se alguém foi criativo com a entrada de dados. A segunda é que é muito mais lento do que especificar o formato exato das datas.

## Distribuição do dia do mês para checar a conversão de data

Um dos grandes perigos na conversão de datas é misturar os meses e dias. A função to_datetime() ajuda muito com as mensagens de erro, mesmo assim é boa ideia checar novamente se os dias dos meses extraídos fazem sentido.  
Para fazer isso é possível fazer um gráfico de histograma com os dias do mês. É esperado termos valores distribuídos uniformemente entre 1 e 31, uma vez que não há razão que um dia seja mais comum que outro (exceto 31, pois nem todos os meses tem 31 dias). 

    day_of_month = df['date_parsed'].dt.day
    day_of_month = day_of_month.dropna()
    sns.distplot(day_of_month, kde=False, bins=31)

![plot days](/images/plot_days_month.png){:class="img-responsive"}

## Codificação de caracteres

Codificação de caracteres (Character encodings) são conjuntos específicos de regras para mapeamento de sequências de bytes binários brutos (que se parece com isso: 0110100001101001) para caracteres que compõem o texto legível (como "oi"). Existem muitas codificações diferentes, e se você tentou ler em texto com uma codificação diferente da que foi originalmente escrita, você acabou com um texto embaralhado chamado "mojibake" (mo-gee-bah-kay). Aqui está um exemplo de mojibake:

    æ–‡å—åŒ–ã??

Você também pode acabar com um caractere "desconhecido". Há o que é impresso quando não há mapeamento entre um byte específico e um caractere na codificação que você está usando para ler sua cadeia de bytes e eles se parecem com isso:

    ����������

UTF-8 é a codificação de texto padrão. Todo o código Python está em UTF-8 e, idealmente, todos os dados também devem estar.

Para converter uma variável string para bytes:

    before = "This is the euro symbol: €"
    after = before.encode("utf-8", errors = "replace")

Ao imprimir a variável after fica da seguinte forma:

    b'This is the euro symbol: \xe2\x82\xac'

Para visualizar o texto corretamente é necessário converter para string, da seguinte maneira:

    print(after.decode("utf-8"))


## Lendo arquivos com problemas de codificação

Para descobrir a codificação de um arquivo pode ser utilizado o seguinte código:

    with open("ks-projects-201801.csv", 'rb') as rawdata:
        print(chardet.detect(rawdata.read(10000)))

Resultando em:
    {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}

Portanto, chardet tem 73% de confiança de que a codificação correta é "Windows-1252". Para carregar o arquivo com a codificação correta usando o pandas:

    pd.read_csv("ks-projects-201612.csv", encoding='Windows-1252')


Este post foi baseado em [Data cleaning challenge by Kaggle](https://www.kaggle.com/rtatman/data-cleaning-challenge-handling-missing-values){:target="_blank"}.


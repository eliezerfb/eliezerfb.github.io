Title: Dicas de Data Cleaning
Date: 2018-03-31 20:23
Modified: 2018-03-31 20:23
Category: Data Science
Tags: data science, data cleaning, 
Slug: dicas-cata-cleaning
Authors: Eliézer
Summary: Algumas dicas e para efetuar limpeza em dados

O processo de limpeza e preparação dos dados representa cerca de 80% do trabalho de um cientista de dados. Datas em diversos formatos, diversos encodings, dados incompletos, erros de digitação são muito comuns. Antes de realizar qualquer análise é necessário tratar estes problemas. Neste post reúno algumas dicas de pré-processamento que são úteis no dia-a-dia.

## Manipulação de Dados Faltantes

Para obter o número de pontos de dados perdidos por coluna, podemos utilizar o código:

    missing_values_count = df.isnull().sum()
    total_cells = np.product(df.shape)
    total_missing = missing_values_count.sum()
    print((total_missing/total_cells) * 100)

Também podemos visualizar os dados faltantes com a ajuda da biblioteca [missingno](https://github.com/ResidentMario/missingno). 

    pip install missingno
    
Esta biblioteca permite diversas visualizações, abaixo é possível ver um exemplo de código:    

    from quilt.data.ResidentMario import missingno_data
    collisions = missingno_data.nyc_injurious_collisions()
    collisions = collisions.replace("nan", np.nan)
    import missingno as msno
    %matplotlib inline
    msno.matrix(collisions.sample(250))

[msgno example]({filename}/images/msgno.png)

Mas nem todos dados faltantes são erros. Nesse momento é necessário se perguntar: **um dado faltante é porque não foi gravado ou porque não existe?**

Se um valor é faltante porque ele não existe (como a altura do filho mais velho de quem não tem filhos), então não faz sentido tentar adivinhar este valor. Estes valores devem ser mantidos como NaN. Por outro lado, se um valor não existe porque não foi gravado, então podemos tentar adivinhar seu valor baseado em outros valores nesta coluna e linha. 


Veja também:
[Data cleaning challenge by Kaggle](https://www.kaggle.com/rtatman/data-cleaning-challenge-handling-missing-values)  


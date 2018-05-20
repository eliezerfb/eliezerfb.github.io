Title: Python e Twitter
Date: 2018-05-20 09:06
Modified: 2018-05-20 09:06
Category: Python
Tags: python, twitter, dicas 
Slug: dicas-twitter
Authors: Eliézer
Summary: Algumas dicas de como extrair dados do Twitter com Python


Neste exemplo vou mostrar como extrair dados do Twitter com o Python com a biblioteca **python-twitter**.  

# Criar o Aplicativo no Twitter
O aplicativo no Twitter é necessário para realizar a autenticação no serviço, nada mais é que um conjunto de chaves que garantem a sua identificação.  
1) Acesse o [Twitter Apps](https://apps.twitter.com/) com a sua conta no Twitter;  
2) Clique na opção "Create New App" e digite os dados obrigatórios (Nome, Descrição e Site). Marque também a opção que você concorda com os termos do serviço;  
3) Concluído o seu aplicativo vai estar disponível na tela principal, clique nele para abrir;  
4) Clique em “Generate My Access Token and Token Secret”;  
5) Na seção “Keys and Access Tokens” você vai encontrar os dados de autenticação (Consumer Key, Consumer Secret, Access Token, Access Token) Secret.  

Lembre-se que estes dados são privados de sua conta no Twitter, nunca divulgue-os.

# Instalação da biblioteca python-twitter

Vamos utilizar a biblioteca [python-twitter](https://github.com/bear/python-twitter), caso precisar você pode ler sua [documentação](https://python-twitter.readthedocs.io/en/latest/). Esta biblioteca é baseada na [API do Twitter](https://developer.twitter.com/en/docs).  

# Criando um arquivo de configuração

Como não podemos manter os tokens diretamente no código, vamos criar um arquivo tokens.json, com a seguinte estrutura:

```json
{
  "consumer_key" : "seu_consumer_key",
  "consumer_secret" : "seu_consumer_secret",
  "access_token_key" : "seu_access_token_key",
  "access_token_secret" : "seu_access_token_secret"
}
```

# Acessando a API do Twitter

1) Crie um arquivo .py e importe a biblioteca do twitter e json:  

```python
import twitter
import json
```

2) Carregue o arquivo de configuração:  

```python
with open('tokens.json') as f:
    data = json.load(f)
```

3) Agora é só carregar a API do Twitter, utilizando os dados do arquivo json:  

```python
api = twitter.Api(**data)
```

Pronto! Agora vamos testar se tudo está certo:  

```python
print(api.VerifyCredentials())
```

Caso tiver alguma credencial errada, o resultado será:  

```python
twitter.error.TwitterError: [{'code': 32, 'message': 'Could not authenticate you.'}]
```

# Realizando buscas no Twitter

A API do Twitter permite fazer diversos tipos de consultas. O retorno dessas consultas pode ser acessado facilmente.
Vamos criar uma função que, a partir de uma lista de status, mostra o nome do usuário e o texto do twitter.

```python
def print_status(status_list):
    for status in status_list:
        print(status.user.name, ':', status.text+'\n')
```

Poderíamos extrair outros dados, porém neste exemplo vamos restringir a apenas estes.  

## Busca na timeline de um usuário

Podemos buscar todos os tweets de um da Timeline de um usuário:

```python
status_list = api.GetUserTimeline(screen_name='RosieDaSerenata')
print_status(status_list=status_list)
```

## Busca por termos

Ou fazer a busca por um termo específico, restringindo a quantidade de tweets, linguagem e mostrando apenas os mais recentes:  

```python
status_list = api.GetSearch(term="Operação Serenata de Amor",
                            lang='pt',
                            count=50,
                            result_type='recent')
print_status(status_list=status_list)
```

## Busca georreferenciada

E ainda buscar tweets que estão georreferenciados:  

```python
status_list = api.GetSearch(geocode=(-27.231700, -52.023781, "2km"))
print_status(status_list=status_list)
```

# Também é possível postar uma atualização

E é bem simples:  

```python
status = api.PostUpdate('Testing python-twitter!!')
```

# E o que eu faço com isso?

As redes sociais são fontes valiosas de dados não estruturados para serem usados em Data Science, sendo um ótimo assunto para um próximo post!

O código completo você pode ver no [GitHub](https://github.com/eliezerfb/python_tests/tree/master/twitter).


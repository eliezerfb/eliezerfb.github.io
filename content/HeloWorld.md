Title: Um blog com Pelican e Github Pages
Date: 2018-03-31 15:00
Modified: 2018-03-31 15:00
Category: Python
Tags: pelican, publishing, web
Slug: blog-python-pelican
Authors: Eliézer
Summary: Como utilizar o Pelican para criar um blog pessoal.

Na necessidade de criar um blog pessoal de maneira prática e barata (no caso, sem custos) encontrei o [Pelican](http://docs.getpelican.com/en/stable/).
O Pelican é um gerador de páginas estáticas feito em Python. Com ele não é necessário utilizar outras ferramentas como Django, Web2Py ou Wordpress. Como não precisa utilizar banco de dados (é apenas HTML estático) o conteúdo do blog fica em documentos de texto, facilitando qualquer futura migração.

Para hospedar o blog optei por utilizar o [GitHub Pages](https://pages.github.com/). É uma opção gratuíta que permite utilizar domínio próprio além de facilitar pois publico meu blog utilizando o git.

Para utilizar o Pelican é recomendado criar um ambiente virtual. Utilizei o [Anaconda](https://www.anaconda.com/) para criar o ambiente virtual (mas pode ser utilizado o virtualenv também):

`$$ conda create -n pelican-env python=3.6`

Ative o ambiente virtual:

`$$ source activate pelican-env`

Com o ambiente virtual ativo instale o Pelican e o Markdown com o pip:

`$$ pip install pelican markdown`

No GitHub é necessário criar um novo projeto e seu nome deve ser **username-do-github.github.io**. No seu diretório de projeto crie um diretório com este mesmo nome.

Dentro deste novo diretório gere o projeto pelo Pelican:

`$$ pelican-quickstart`

Este script realiza algumas perguntas para gerar o website:

1. Título do seu site.
2. Nome do autor.
3. Idioma padrão.
4. Se deseja utilizar uma URL personalizada.
5. URL personalizada (se informado Y na opção acima).
6. Habilitar paginação nos posts.
7. Fuso horário (deixe America/Sao_Paulo)
8. Do you want to generate a Fabfile/Makefile to automate generation and publishing? Y - Esta opção facilita a geração do site, pois automatiza a sua geração e publicação.
9. Recarregamento automático do server em desenvolvimento (informe Y).
10. As próximas perguntas se referem onde você vai deixar hospedado (FTP, SSH, Dropbox, S3, Rackspace e GitHub Pages), responda Y apenas para GitHub Pages.
11. Is this your personal page (username.github.io), informe Y para confirmar.

Pronto! O projeto já está disponível em seu diretório.

### Versionamento

Agora que o projeto está pronto é necessário iniciar o versionamento com git e adicionar o repositório remoto.

`$$ git init`
`$$ git remote add origin git@github.com:username-do-github/username-do-github.github.io.git`

É necessário organizar o projeto em 2 branchs:

* **pelican**: os arquivos e códigos que gerarão o site estático.
* **master**: os arquivos estáticos gerados;

`$$ git checkout -b pelican`
`$$ git add .`
`$$ git commit -m 'iniciando branch pelican'`
`$$ git push origin pelican`

Para publicar o conteúdo estático na branch master é necessário utilizar o **ghp-import**:

`$$pip install ghp-import`

E finalmente para gerar o site estático é só utilizar o **make**:

`$$make github`

### Para configurar um domínio personalizado

Este passo é opcional, caso deseje utilizar um domínio próprio.

Dentro de /content crie um diretório chamado **extra**. Neste diretório crie um arquivo chamado **CNAME** com o nome de seu domínio.

Em **pelicanconf.py** adicione as seguintes linhas:

    STATIC_PATHS = ['extra/CNAME']
    EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}





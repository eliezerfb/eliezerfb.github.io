Title: Um blog com Python, Pelican e Github Pages
Date: 2018-03-31 15:00
Modified: 2018-03-31 15:00
Category: Python
Tags: pelican, publishing, web
Slug: blog-python-pelican
Authors: Eliézer
Summary: Como utilizar o Pelican para criar um blog pessoal.

Na necessidade de criar um blog pessoal de maneira prática e barata (no caso, sem custos) encontrei o Pelican.
O Pelican é um gerador de páginas estáticas feito em Python. Com ele não é necessário utilizar outras ferramentas como Django, Web2Py ou Wordpress. Como não precisa utilizar banco de dados (é apenas HTML estático) o conteúdo do blog fica em documentos de texto, facilitando qualquer futura migração.

Para utilizar o Pelican é recomendado criar um ambiente virtual. Como eu já utilizo o Anaconda (https://www.anaconda.com/) o utilizei para criar o ambiente:

conda create -n pelican-env python=3.6

Title: Controle social da administração pública com inteligência artificial
Date: 2017-08-23 20:23
Modified: 2017-08-23 20:23
Category: Artigos
Tags: data science, serenata, Inteligência Artificial, política
Slug: controle-social-com-ia
Authors: Eliézer
Summary: Como a inteligência artificial pode ser usada para controle social da administração pública

Em 2012 entrou em vigor a [Lei de Acesso à Informação](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm){:target="_blank"} que regulamentou o acesso às informações públicas. Essa lei permite que qualquer pessoa solicite o recebimento de informações públicas, sem apresentar motivos.

A Lei vale para os três Poderes da União, Estados, Distrito Federal e Municípios, inclusive aos Tribunais de Conta e Ministério Público. Entidades privadas sem fins lucrativos também são obrigadas a dar publicidade a informações referentes ao recebimento e à destinação dos recursos públicos por elas recebidos.

Com essa disponibilidade dos dados, o Brasil ficou no topo do ranking da transparência e em contraste também está no topo do ranking da corrupção. Ou seja, as informações estão disponíveis porém as pessoas não conseguem analisar ou não se preocupam com isso.

## Cota para Exercício da Atividade Parlamentar (CEAP)

A CEAP permite que cada deputado federal seja reembolsado por seus gastos relativos a alimentação, transporte e outros gastos. Existem cotas e algumas regras para cada tipo de gasto. Um exemplo é a alimentação, que não permite que o deputado seja reembolsado por gastos de terceiros. O problema é que o deputado é o responsável por indicar no recibo o valor de terceiros, não existe nenhuma fiscalização nesse sentido e cada deputado tem o direito de receber até 40 mil reais mensais a título de atividades parlamentares.

A quantidade enorme de dados impossibilita a auditoria manual, onde um arquivo referente o ano de 2016 possui o tamanho de 5GB. Assim, o cientista de dados Irio Musskopf teve a ideia de usar inteligência artificial para auditar contas públicas e combater a corrupção. Compartilhou sua ideia com amigos, conseguiu montar um time de 8 pessoas e com a ajuda de crowdfunding iniciaram a [Operação Serenata de Amor](https://serenata.ai/){:target="_blank"}.

## É aí que entra a ciência de dados

Eles criaram uma robô, chamada Rosie, que faz a auditoria das contas da CEAP. Com base no histórico de gastos, a Rosie consegue aprender qual é o padrão de gastos para cada fornecedor. Por exemplo, ela consegue identificar que o padrão para um almoço em determinado restaurante é 100 reais. Caso algum deputado gaste um valor maior que isso em um recibo, ela dispara um alerta. Ela também consegue identificar se houve muitos gastos no mesmo dia para o mesmo deputado, principalmente se estes gastos são realizados em cidades geograficamente distantes.

## E já foi descoberto muita coisa

A Rosie já conseguiu descobrir um deputado que gasta todo mês a quantia de 30 tanques de combustível completos. Uma refeição que custou R$ 6.205,00, dois deputados que chegaram a pedir 13 refeições feitas no mesmo dia e um deputado que foi reembolsado por bebida alcoólica em Las Vegas. 

A maioria das descobertas são pequenos valores e é muito comum encontrar o pagamento de refeições para duas ou mais pessoas. As descobertas da Rosie podem ser acompanhadas no Twitter [@RosieDaSerenata](https://twitter.com/rosiedaserenata){:target="_blank"} e também lembre de curtir a [página no facebook](https://www.facebook.com/operacaoSerenataDeAmor/){:target="_blank"}. O site do projeto é https://[serenatadeamor.org].

## Apoie o projeto

Além de ser um projeto **apartidário**, ele é um projeto aberto, ou seja, todos podem ajudar. Há várias formas de ajudar:
* Apoio financeiro - Para manter uma mínima equipe técnica é possível apoiar financeiramente o projeto no [Apoia.se](https://apoia.se/serenata){:target="_blank"}.
* Conhecimento técnico - O projeto está hospedado no [GitHub](https://github.com/okfn-brasil/serenata-de-amor){:target="_blank"} para quem quiser botar a mão na massa e ajudar fazendo análises e melhorias.
* Denúncias - Utilize as redes sociais para cobrar do deputado explicações sobre os gastos.

A continuidade deste projeto é muito importante, pois é uma maneira onde a sociedade consegue automatizar a fiscalização do poder público.

Artigo postado originalmente em meu [Linkedin](https://www.linkedin.com/pulse/controle-social-da-administra%C3%A7%C3%A3o-p%C3%BAblica-com-eli%C3%A9zer-f-bourchardt/){:target="_blank"}

![imagem-ceap-serenata](/images/ceap-serenata.jpeg){:height="90%" width="90%" class="img-responsive"}


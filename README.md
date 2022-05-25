# IR de Ações
Essa ferramenta ajuda a declaração de imposto de renda sobre as operações na bolsa de valores gerando resumos mensais e anuais de acordo com o histórico de transações.
Para determinar qual unidade da ação está sendo vendida, utilizei o sistema FIFO (_First In First Out)_, mas penso em permitir outros critérios futuramente, tal como minimizar lucro ou LIFO.

## Como utilizar
Pensei nesse projeto com dois tipos de uso em mente:
1. Uso anual para declarar o imposto de renda: dado o histório de todas as transações, gerar os relatórios anuais para ajudar na declaração.

2. Uso contínuo ao longo do ano: a cada transação feita, inserir seu registro na carteira e, no final do mês ter o relatório para facilitar a emissão do DARF (em casos em que isso se aplicar). No final do ano, utilizar os métodos de relatório anual para facilitar a declaração anual.

### Uso anual
Um exemplo de uso está no notebook `multi_transaction_example.ipynb`. Nele, um histórico de transações fictícias é carregado e é refletido na carteira.
Para ter essa planilha do histórico, utilizei essa [outra ferramenta](https://leitordenotas.github.io/) que, para notas de corretagem de até R$5000, é gratuita. Uma outra opção para compilar as transações em forma tabular é acessando seu [relatório de negociações na área do investidor no site da B3](https://www.investidor.b3.com.br/relatorios/negociacao)

### Uso contínuo ao longo do ano
Um uso ao longo do ano seria resumido em:
1. Criar a carteira uma vez
2. Carregar o histórico uma única vez (como no uso anual)
3. Durante o ano usar o método de comprar ou vender da carteira para ir registrando uma de cada vez
4. Ao final do ano utilizar os métodos anuais

## Problemas conhecidos e limitações
Em situações de split, bonificação, ou qualquer outro tipo de situação em que a quantidades de determinada ação se altera, o programa pode quebrar por tentar vender algum papel indisponível.
Nesse caso, por enquanto, a solução é o input manual de novas ações compradas ou vendidas a R$0 na planilha ou pelos métodos `buy` ou `sell`.

Por enquanto, o programa só funciona com ações de empresas (ou seja, não funciona para ETFs, BDRs e FIIs) e não lida bem com day trade, pois não indica a necessidade de gerar o DARF, podendo até quebrar a execução quando há day trade nas transações.

## Próximos passos
- Incluir dinstinção dos ativos entre ações, BDRs, FIIs, ETFs, etc para calcular mais precisamente quando a transação deve ser tributada.
- Tratar day trade
- Incluir taxas (corretagem, emolumentos, etc) para calcular o valor do lucro líquido

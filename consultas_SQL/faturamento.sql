/*
Qual foi o faturamento total e o numero de vendas da loja no período?
*/

select 

sum(valor) as "valor total vendido",
count(id) as "nº de vendas"

from

tabela_vendas
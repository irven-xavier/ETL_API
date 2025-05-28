/*
Qual foi a forma de parcelamento por categoria no período?
*/

select 

categoria,
parcelas,
count(parcelas) as qtd

from

tabela_vendas

group by categoria, parcelas
order by categoria
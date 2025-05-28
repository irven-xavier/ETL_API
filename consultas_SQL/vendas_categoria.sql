/*
Quanto cada categoria vendeu?
*/

select

categoria,
sum(valor) as vendas

from 

tabela_vendas

group by categoria
/*
Como foram as vendas por mês e categoria?
*/

select

to_char(data, 'mm/yy'::text) as mes,
categoria,
sum(valor) as vendas,
count(id) as "Nº de vendas"

from 

tabela_vendas

group by mes, categoria
order by mes, categoria
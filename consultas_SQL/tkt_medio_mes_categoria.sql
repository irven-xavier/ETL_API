/*
Qual foi o ticket médio por mês e categoria?
*/

select

to_char(data, 'mm/yy'::text) as mes,
categoria,
sum(valor) / count (id) as ticket_medio

from

tabela_vendas

group by categoria, mes
order by mes, categoria
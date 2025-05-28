/*
Quais foram as 5 últimas vendas?
*/

select 

id,
data,
valor,
data_extracao

from

tabela_vendas

order by data_extracao desc

limit 5
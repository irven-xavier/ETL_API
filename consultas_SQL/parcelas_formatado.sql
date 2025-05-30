/*
Case when para tratar "à vista" como "1x"
*/

select

	categoria,
	case
		when parcelas = 'À vista' then '1x' 
		else parcelas 
	end as parcelas_formatado,
	count(parcelas) as qtd
	
from
tabela_vendas

group by categoria, parcelas_formatado
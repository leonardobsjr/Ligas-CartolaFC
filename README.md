# Ligas-CartolaFC

Dado ao imenso trabalho que dá criar novas ligas baseadas em outras, criei um pequeno script para me auxiliar nessa tarefa.

_convida_ligas.py_ é basicamente um script auxiliar para convidar times pro CartolaFC [2018]. Para utilizá-las, é preciso utilizar suas credenciais para logar no CartolaFC. Para tal, preencha o arquivo _credenciais_ com as informações de seu acesso ao Globo.com: login na primeira linha e senha na segunda. O script **não armazena nem envia suas credenciais para nenhum lugar diferente dos servidores da Globo.com**.


### Informações para Utilização	

O nome da liga que deve ser passado nas funções é o mesmo que aparece na barra de endereços do browser ao clicar no nome de uma liga no site do cartola. Ex: https://cartolafc.globo.com/#!/liga/**liga-do-globo-esporte-pasargada**. De forma similar, o nome do time pode ser coletado https://cartolafc.globo.com/#!/time/**github-fc**.

Outra coisa a salientar é de que não existem diferenças entre ligas-mata-mata e ligas clássicas para efeito das funções dessa API, o que permite, por exemplo, utilizar a função _convidar_times_outra_liga e passar, no primeiro argumento uma liga clássica e no segundo, uma liga-mata-mata.

Por fim, se você quiser convidar os times, suas credenciais devem ter permissão para tal.

### Descrição das funções:

- *informacoes_liga*: Retorna um JSON com todas as informações da liga passada. Útil para filtrar times e criar critérios de convite 
 - *convidar_times*: Convida os times passados como parâmetro, que deve ser uma lista no formato ['time-1','time-2'], por exemplo.
 - *convidar_times_outra_liga*: Convida todos os times de uma liga de origem para uma liga de destino.

### Exemplo de Utilização
	
    #Convidar os 15 melhores times de uma liga (liga_exemplo) para uma outra liga (nova_liga_exemplo)
    api = APICartola()
    infoliga = api.informacoes_liga('liga_exemplo')
    json_times_ordenados = sorted(infoliga['times'], key=lambda  k: k['ranking']['campeonato'])
    times_a_convidar = [x['slug'] for x in json_times_ordenados[:15]]
    api.convidar_times(times_a_convidar, 'nova_liga_exemplo')

### Notas Adicionais e Agradecimentos

- Esse código foi baseado na API em Python do Vicente Neto: https://github.com/vicenteneto/python-cartolafc.
- Agradeço à Globo.com pelo excelente fantasy game e pela API.
- Atesto que não sou afiliado com a Globo.com de nenhuma forma.

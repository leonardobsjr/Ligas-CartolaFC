import requests
import json

API_URL = 'https://api.cartolafc.globo.com'
AUTH_URL = 'https://login.globo.com/api/authentication'
LIGA_URL = API_URL + '/auth/liga/'

class APICartola:
    
    #O arquivo credenciais deve estar na mesma pasta desse scripts, e deve conter o login na primeira linha, e a senha na segunda.
    def __init__(self):
        try:
            with open("credenciais","r") as f:
                credenciais = f.read().splitlines() 
            response = requests.post(AUTH_URL,json=dict(payload=dict(email=credenciais[0],password=credenciais[1],serviceId=438)))
            body = response.json()
            self.headers = {'X-GLB-Token': body['glbId']} 
        except FileNotFoundError:
            print("Arquivo de Credenciais não encontrado.")
        except KeyError:
            print("Credenciais inválidas. Verifique o arquivo de credenciais.")

    #Retorna informações da liga nome_liga. Útil para pegar informações dos times e customizar o critério de convite.
    def informacoes_liga(self,nome_liga):
        return requests.get(API_URL+'/auth/liga/'+nome_liga, headers=self.headers).json()

    #Convida os times passados como parâmetro [lista] e convida para a a liga nome_liga. Lembrando que o dono da liga já está incluso.
    def convidar_times(self, times, nome_liga):
        return requests.post(API_URL+'/auth/liga/'+nome_liga+'/convidar', json=times, headers=self.headers).json()

    #Convida os times de uma liga [liga_origem] para outra liga [liga_destino]
    def convidar_times_outra_liga(self,liga_origem, liga_destino):
        times_liga_origem = [ x['slug'] for x in requests.get(LIGA_URL+liga_origem,headers=self.headers).json()['times'] ]
        return self.convidar_times(times_liga_origem, liga_destino)

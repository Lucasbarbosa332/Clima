import requests
from datetime import datetime
import pytz
import pycountry_convert as pc

# Chave da API e cidade para consulta
chave = '81012de252723c59b26d3bd1e08a8ad9'
cidade = 'Hong Kong'
api_link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}'

# Fazendo a chamada da API usando requests
r = requests.get(api_link)

# Conversão de dados da variável r em dicionário
dados = r.json()

print(dados)

# País e zona
pais_codigo = dados['sys']['country']

# ------- Zona -------
if pais_codigo in pytz.country_timezones:
    zona_fuso = pytz.country_timezones[pais_codigo]
else:
    zona_fuso = ['UTC']  # Default para UTC caso o país não tenha uma zona conhecida

# ------- País -------
pais = pytz.country_names.get(pais_codigo, "Desconhecido")  # Obter o nome do país ou "Desconhecido"

# ------- Data --------
zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

# -------- Tempo --------
tempo = dados['main']['temp']
pressao = dados['main']['pressure']
humidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']

# Exibindo informações
print(f"Zona: {zona}")
print(f"País: {pais}")
print(f"Hora local: {zona_horas}")
print(f"Temperatura: {tempo}K")
print(f"Pressão: {pressao}hPa")
print(f"Humidade: {humidade}%")
print(f"Velocidade do vento: {velocidade} m/s")
print(f"Descrição: {descricao}")

# Função para obter o continente do país
def pais_continente(nome_pais):
    try:
        pais_alpha = pc.country_name_to_country_alpha2(nome_pais, cn_name_format="default")
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
        return pais_continente_nome
    except Exception as e:
        return f"Erro ao obter continente: {e}"

# Exemplo de uso da função
continente = pais_continente(pais)


# Exemplo adicional com país específico


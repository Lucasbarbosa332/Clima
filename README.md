# Clima

# Mini sistema com consumo de API

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

📂 Este projeto não contem deploy e não contem git, então para executar voce tera que baixar o arquivo zip extrai no seus arquivos e abrir em algun IDE assim podemdo executalo 
******************************************************************************************************************************************************************************** 



# Projeto: Sistema de Clima em Python 🌦️

Descrição do Projeto
O projeto é um sistema de clima desenvolvido em Python, que utiliza a API do OpenWeather para fornecer informações meteorológicas em tempo real. O sistema integra várias bibliotecas Python para oferecer uma experiência rica e dinâmica ao usuário. As principais bibliotecas usadas são:

requests: Para fazer chamadas HTTP à API do OpenWeather e obter dados meteorológicos.
pytz: Para lidar com fusos horários e ajustar as informações de tempo de acordo com o local.
pycountry_convert: Para converter códigos de países em continentes e facilitar a exibição de informações geográficas.

# Funcionalidades 📌
 
 Consulta de Clima: O usuário pode inserir o nome de uma cidade e obter informações detalhadas sobre o clima atual, incluindo:

Hora Local: Exibida com base no fuso horário do país da cidade consultada.
Nome do País: Determinado a partir do código do país retornado pela API.
Cidade: Nome da cidade consultada.
Temperatura: Apresentada em graus Celsius, convertida a partir de Kelvin.
Pressão Atmosférica: Medida em hPa.
Umidade: Percentual de umidade no ar.
Velocidade do Vento: Medida em metros por segundo.
Descrição do Tempo: Condições meteorológicas descritas em texto.

 Troca Dinâmica de Imagem e Fundo: O sistema altera a imagem e o fundo da interface com base no horário local da cidade consultada. As imagens e fundos representam diferentes períodos do dia:

Manhã (6:00 - 12:00): Imagem do sol durante o dia e fundo claro.
Tarde (12:00 - 18:00): Imagem do sol à tarde e fundo amarelado.
Noite (18:00 - 00:00): Imagem da lua e fundo escuro.
Madrugada (00:00 - 6:00): Imagem da lua e fundo escuro.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

# Tecnologias Utilizadas 🔙 🔚

API OpenWeather: Fornece dados em tempo real sobre o clima e condições meteorológicas para qualquer cidade do mundo.
Biblioteca requests: Facilitadora de chamadas HTTP para interagir com a API.
Biblioteca pytz: Gerencia fusos horários para garantir que a hora local exibida seja precisa.
Biblioteca pycountry_convert: Converte códigos de países em nomes e continentes para uma exibição mais rica de informações geográficas.
Biblioteca PIL (Pillow): Manipula e exibe imagens no aplicativo.

<img width=100% src="https://github.com/Lucasbarbosa332/Clima/blob/main/Captura%20de%20tela%202024-09-10%20001554.png"></img>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

# Interface do Usuário 📱 

A interface é construída com a biblioteca tkinter, proporcionando um layout simples e funcional:

Campo de Entrada: Permite ao usuário digitar o nome da cidade para consulta.
Botão "Ver clima": Dispara a consulta e atualiza as informações exibidas.
Labels Informativos: Exibem a cidade, data e hora local, umidade, pressão, velocidade do vento e descrição do clima.
Imagem Dinâmica: Mostra uma imagem representativa do período do dia, baseada no horário local da cidade consultada.

<img width=100% src="https://github.com/Lucasbarbosa332/Clima/blob/main/Captura%20de%20tela%202024-09-10%20001659.png"></img>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

# Funcionamento 🔧

O usuário insere o nome da cidade e clica no botão "Ver clima".
O sistema faz uma chamada à API do OpenWeather para obter dados climáticos.
O sistema ajusta a hora local e o fundo da interface de acordo com o horário local da cidade.
Atualiza a interface com as informações meteorológicas e a imagem apropriada para o período do dia.

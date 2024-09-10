import tkinter as tk
from tkinter import RIDGE, Button, Entry, Frame, Label, ttk
from PIL import Image, ImageTk  
import requests
from datetime import datetime
import pytz

############### Cores #############
co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#6f9fbd"  # Azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"

# Janela principal
janela = tk.Tk()
janela.title('Weather App')
janela.geometry('320x350')
janela.configure(bg=fundo_dia)  

# Separador
ttk.Separator(janela, orient=tk.HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Frame superior
frame_top = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0)
frame_top.grid(row=1, column=0)  

frame_corpo = Frame(janela, width=320, height=300, bg=fundo_dia, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky="NW")  

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Função que retorna as informações
def informacao():
    chave = '81012de252723c59b26d3bd1e08a8ad9'
    cidade = e_local.get()
    api_link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}'

    # Fazendo a chamada da API usando requests
    r = requests.get(api_link)
    dados = r.json()

    # Verificação de erros na resposta da API
    if r.status_code != 200:
        l_cidade.config(text="Erro na API")
        return

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
    zona_horas_formatada = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

    # -------- Tempo --------
    tempo = dados['main']['temp'] - 273.15  # Converter de Kelvin para Celsius
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    # Atualizando os labels com as informações obtidas
    l_cidade.config(text=f'{cidade} - {pais}')
    l_data.config(text=zona_horas_formatada)
    l_humidade.config(text=f'{humidade}')
    l_pressao.config(text=f'Pressão: {pressao} hPa')
    l_velocidade.config(text=f'Velocidade do vento: {velocidade} m/s')
    l_descricao.config(text=descricao.capitalize())

    # Lógica para imagens e fundo
    hora_atual = datetime.now().hour
    global imagem 

    if hora_atual < 0:
        imagem = Image.open('img/lua.png')
        fundo = fundo_noite
    elif hora_atual < 12:
        imagem = Image.open('img/sol_dia.png')
        fundo = fundo_dia
    elif hora_atual < 18:
        imagem = Image.open('img/sol_tarde.png')
        fundo = fundo_tarde
    else:
        imagem = Image.open('img/lua.png')
        fundo = fundo_noite
    
    # Atualizando o fundo da janela e dos frames
    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)

    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    # Atualizando a imagem no label
    l_icon.config(image=imagem)
    l_icon.image = imagem  # Manter uma referência à imagem para evitar que seja coletada como lixo

# Configuração do frame_top
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)
b_ver = Button(frame_top, command=informacao, text='Ver clima', bg=co1, fg=co2, font=("Ivy", 9, "bold"), relief='raised', overrelief=RIDGE)
b_ver.place(x=250, y=10)

# Configuração do frame_corpo
l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 14))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 10))
l_data.place(x=10, y=54)

l_humidade = Label(frame_corpo, text='', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 45))
l_humidade.place(x=10, y=100)

l_h_simbolo = Label(frame_corpo, text='%', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 10, "bold"))
l_h_simbolo.place(x=85, y=110)

l_h_nome = Label(frame_corpo, text='Humidade', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 8))
l_h_nome.place(x=85, y=140)
 
l_pressao = Label(frame_corpo, text='', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 10))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 10))
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_corpo, text='', anchor='center', bg=fundo_dia, fg=co1, font=("Arial", 10))
l_descricao.place(x=170, y=190)  

l_icon = Label(frame_corpo, bg=fundo_dia)
l_icon.place(x=162, y=50)

janela.mainloop()

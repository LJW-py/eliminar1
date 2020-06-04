import tkinter as tk  
import requests  
from bs4 import BeautifulSoup
import time
from tkinter import *
import webbrowser



entrada = 0
salida = 0
actual = 0
snapbank = 'https://qrhuntr.weebly.com/'
gmail= 'https://qrhuntr.weebly.com/contacta.html'

def presentación():   #Se innicia una pequeña presentación en el cmd.
    print('  ')
    print('                                                ----------------------<< QR_HUNTER >>-----------------------------')
    print('  ')
    time.sleep(1)
    print('                                                >>> By: Alejandro Cartagena, Joan Castejón, Teo Fructuoso')
    time.sleep(1)
    print('                                                >>> ...')
    time.sleep(1)
    print('                                                >>> Salesianos San José Artesano Elche')
    time.sleep(1)
    print(' ')                                                 

presentación()


def qr_entrada ():  # Esta primera función se encargará de hacer un recuento continuo de los escaneos hechos al qr de la entrada.

    people_in_list = [] # En este array se irá añadiendo el numero de personas que lo escaneen.

    uqr_web_link = 'https://app.uqr.me/panel/211554/qrs/589624/880242/edit-content#qr-stats'  # Url con los datos. Cambiala por la tuya.
    uqr_web_req = requests.get(uqr_web_link)  # Se extrae la información en html de la página.

    uqr_web_html = uqr_web_req.text  # Se convierte la respuesta de la petición en texto plano.
    uqr_web_soup = BeautifulSoup(uqr_web_html, "html.parser")  # Se prepara la págani para el scraping.

    div = uqr_web_soup.find_all('div', {"class": "ibox-content stats-counter text-center"})  # Busca la clase referida.

    number_of_entrance = 0

    for div_block in div:  # Es necesaria la creación de un bucle que intente encontrar los datos dentro de la clase.
        h2 = div_block.find('h2')
        number_of_entrance = h2.get_text()
        if div_block == 3:  # Se menciona que a la terceravulta del bucle, se salga del mismo.
            break
    
    return number_of_entrance

entrada = qr_entrada() #De esta forma conseguiremos manipular cómodamente los datos más adelante.


def qr_salida ():  # Esta segunda función se encargará de hacer un recuento continuo de los escaneos hechos al qr de la salida.

    people_in_list = [] # En este array se irá añadiendo el numero de personas que lo escaneen.

    uqr_web_link = 'https://app.uqr.me/panel/211554/qrs/589678/880327/edit-content#qr-stats'  # Url con los datos.
    uqr_web_req = requests.get(uqr_web_link)  # Se extrae la información en html de la página.

    uqr_web_html = uqr_web_req.text  # Se convierte la respuesta de la petición en texto plano.
    uqr_web_soup = BeautifulSoup(uqr_web_html, "html.parser")  # Se prepara la págani para el scraping.

    div = uqr_web_soup.find_all('div', {"class": "ibox-content stats-counter text-center"})  # Busca la clase referida.

    number_of_exits = 0

    for div_block in div:  # Es necesaria la creación de un bucle que intente encontrar los datos dentro de la clase.
        h2 = div_block.find('h2')
        number_of_exits = h2.get_text()
        if div_block == 3:  # Se menciona que a la tercera vuelta del bucle, se salga del mismo.
            break
    
    return number_of_exits

salida = qr_salida() #De esta forma conseguiremos manipular cómodamente los datos más adelante.

actual = entrada - salida #Es necesario sacar la diferencia de los totales para conocer el aforo.



# Ahora trasladamos toda la información a la aplicación de ordenador.

def aplicación_gráfica():

    #Procedemos a crear la ventana con sus configuraciones correspondientes.
    app = tk.Tk()

    app.geometry('400x300')
    app.resizable(0, 0)
    app.configure(bg='#49A')

    #---------------------------------------------------------------------------------------------
    #Título en la ventana de la aplicación.
    title = tk.Label(text="\n__>> QR_HUNTER <<__", font=('Arial','20'), fg='black', bg='#49A')
    title.pack()

    #Enunciado sobre los datos de entrada totales.
    txt_entrada= tk.Label(text="\n- Datos totales de entradas: ", font=('Times New Roman', '13'), fg='black', bg='#49A')
    txt_entrada.pack()

    #---------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------
    #Se crea un boton que al pulsarlo actualiza los datos.
    def update_datos_entrada():
        datos_entrada.set(entrada)

    datos_entrada = tk.StringVar()
    buttonA = tk.Button(app,  fg='white', bg='black', textvariable=datos_entrada, command=update_datos_entrada)
    buttonA.pack()

    #---------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------
    #Enunciado sobre los datos de salidas totales.
    txt_salida= tk.Label(text="\n- Datos totales de salidas: ", font=('Times New Roman', '13'), fg='black', bg='#49A')
    txt_salida.pack()

    #Se crea un boton que al pulsarlo actualiza los datos.
    def update_datos_salida():
        datos_salida.set(salida)

    datos_salida = tk.StringVar()
    buttonB = tk.Button(app,  fg='white', bg='black', textvariable=datos_salida, command=update_datos_salida)
    buttonB.pack()

    #---------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------
    #Enunciado sobre los datos de salidas totales.
    txt_actual= tk.Label(text="\n- Aforo ahora mismo: ", font=('Times New Roman', '13'), fg='black', bg='#49A')
    txt_actual.pack()

    #Se crea un boton que al pulsarlo actualiza los datos.
    def update_datos_aforo():
        datos_aforo.set(actual)

    datos_aforo = tk.StringVar()
    buttonC = tk.Button(app,  fg='white', bg='black', textvariable=datos_aforo, command=update_datos_aforo)
    buttonC.pack()

    #---------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------

    #Se crea un botón que lleve directamente al snapbank mediante el navegador que el usuario tenga instalado.
    def OpenUrl():
        webbrowser.open_new(snapbank)

    button = Button(app, fg='white', bg='black', text="Snap_Bank", command=OpenUrl)
    button.place(x=300, y=260)

    #---------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------

    def Openmail():
        webbrowser.open_new(gmail)

    button = Button(app, fg='white', bg='black', text="Contacta", command=Openmail)
    button.place(x=25, y=260)

    #---------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------

    #Esto es esencial, ya que es lo que causa que se ejecute todo.
    app.mainloop()

#Llamamos a la función, y empieza a funcionar.
aplicación_gráfica()
import requests  
from bs4 import BeautifulSoup



entrada = 0
salida = 0
actual = 0

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


#No muestra nada, ya que no se han escaneado los qr.
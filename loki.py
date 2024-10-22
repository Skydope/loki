# -*- coding: utf-8 -*-

import time
import subprocess
import random
import logging
import requests
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Lista de User-Agents conocidos
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", # User-Agent 1
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15", # User-Agent 2
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",           # User-Agent 3
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1", # User-Agent 4
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"                                       # User-Agent 5
]

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return resultado.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar el comando '{comando}': {e.stderr.decode().strip()}")
        return None

def verificar_tor():
    try:
        subprocess.check_output('which tor', shell=True)
        logging.info('Tor está instalado.')
    except subprocess.CalledProcessError:
        logging.info('Tor no está instalado. Instalando...')
        ejecutar_comando('sudo apt update && sudo apt install tor -y')
        logging.info('Tor ha sido instalado correctamente.')

def cambiar_ip(user_agent):
    ejecutar_comando("service tor reload")
    ip_actual = obtener_ip(user_agent)
    if ip_actual:
        logging.info(f"[+] Tu IP ha sido cambiada a: {ip_actual}")
    else:
        logging.error("[-] No se pudo obtener la nueva IP.")

def obtener_ip(user_agent):
    try:
        url = 'http://checkip.amazonaws.com'
        headers = {'User-Agent': user_agent} if user_agent else {}
        respuesta = requests.get(url, proxies={"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}, headers=headers)
        return respuesta.text.strip()
    except requests.RequestException as e:
        logging.error(f"Error al obtener la IP: {e}")
        return None

def cambiar_mac(interface):
    nueva_mac = "02:00:%02x:%02x:%02x:%02x" % (
        random.randint(0x00, 0x7f), random.randint(0x00, 0xff),
        random.randint(0x00, 0xff), random.randint(0x00, 0xff)
    )
    ejecutar_comando(f"sudo ifconfig {interface} down")
    resultado = ejecutar_comando(f"sudo macchanger -m {nueva_mac} {interface}")
    ejecutar_comando(f"sudo ifconfig {interface} up")

    if resultado:
        logging.info(f"[+] Dirección MAC para {interface} cambiada a: {nueva_mac}")
    else:
        logging.error(f"[-] No se pudo cambiar la MAC para {interface}")

def mostrar_banner():
    print('''\033[1;32;40m
 _               _      _ 
| |             | |    (_)
| |       ___   | | __  _ 
| |      / _ \  | |/ / | |
| |____ | (_) | |   <  | |
\_____/  \___/  |_|\_\ |_|
                Loki IP/MAC Changer
\033[0m''')

def mostrar_ayuda():
    print('''
Uso del script Loki:
    -h, --help                 Muestra este mensaje de ayuda.
    -t, --time [segundos]      Tiempo en segundos para cambiar la IP. Por defecto, es 60 segundos.
    -l, --loop [número]        Número de veces que se cambiará la IP. Si es 0, cambia indefinidamente.
    -m, --mac                  Cambia la dirección MAC también. Requiere la opción -i.
    -i, --interface [nombre]   Interfaz de red para cambiar la dirección MAC (e.g., eth0, wlan0).
    -u, --user-agent [cadena]  Establece un User-Agent personalizado para las solicitudes HTTP.
    --user-agent-1             Selecciona el User-Agent 1 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36).
    --user-agent-2             Selecciona el User-Agent 2 (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15).
    --user-agent-3             Selecciona el User-Agent 3 (Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36).
    --user-agent-4             Selecciona el User-Agent 4 (Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1).
    --user-agent-5             Selecciona el User-Agent 5 (Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0).

Ejemplos:
    python3 loki.py -t 120 -l 5 --user-agent-1
    python3 loki.py --time 60 --loop 0 -u "MyCustomUserAgent/1.0"
''')

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action="store_true", help="Muestra la ayuda del script")
    parser.add_argument("-t", "--time", type=int, default=60, help="Tiempo para cambiar la IP en segundos (default=60)")
    parser.add_argument("-l", "--loop", type=int, default=0, help="Número de veces para cambiar la IP (default=infinito)")
    parser.add_argument("-m", "--mac", action="store_true", help="Cambiar la dirección MAC")
    parser.add_argument("-i", "--interface", type=str, help="Interfaz de red para cambiar la MAC (e.g., eth0, wlan0)")
    parser.add_argument("-u", "--user-agent", type=str, help="User-Agent personalizado para solicitudes HTTP")
    for i in range(1, 6):
        parser.add_argument(f"--user-agent-{i}", action="store_true", help=f"Selecciona el User-Agent {i}")
    args = parser.parse_args()

    if args.help:
        mostrar_ayuda()
        return

    mostrar_banner()
    verificar_tor()
    ejecutar_comando("service tor start")

    # Determinar el User-Agent a utilizar
    user_agent = args.user_agent
    for i in range(1, 6):
        if getattr(args, f"user_agent_{i}"):
            user_agent = USER_AGENTS[i-1]
            break
    if not user_agent:
        user_agent = "LokiUserAgent/1.0" # User-Agent por defecto

    try:
        tiempo_cambio = args.time
        repeticiones = args.loop
        cambiar_mac_opcion = args.mac
        interface = args.interface

        if cambiar_mac_opcion and not interface:
            logging.error("Debes especificar una interfaz con -i para cambiar la dirección MAC.")
            return

        if repeticiones == 0:
            logging.info("Iniciando cambio infinito de IP. Presiona Ctrl+C para detener.")
            while True:
                try:
                    time.sleep(tiempo_cambio)
                    cambiar_ip(user_agent)
                    if cambiar_mac_opcion:
                        cambiar_mac(interface)
                except KeyboardInterrupt:
                    logging.info('\nLoki IP/MAC Changer se ha cerrado.')
                    break
        else:
            logging.info(f"Iniciando cambio de IP {repeticiones} veces, cada {tiempo_cambio} segundos.")
            for _ in range(repeticiones):
                try:
                    time.sleep(tiempo_cambio)
                    cambiar_ip(user_agent)
                    if cambiar_mac_opcion:
                        cambiar_mac(interface)
                except KeyboardInterrupt:
                    logging.info('\nLoki IP/MAC Changer se ha cerrado antes de completar las repeticiones.')
                    break

    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")
        mostrar_ayuda()

if __name__ == "__main__":
    main()

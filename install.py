import os
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def verificar_root():
    if os.geteuid() != 0:
        logging.error("Este script debe ejecutarse como root.")
        sys.exit(1)

def instalar():
    verificar_root()
    try:
        os.chmod('loki.py', 0o777)
        os.makedirs('/usr/share/loki', exist_ok=True)

        # Verificar si loki.py ya existe
        if os.path.exists('/usr/share/loki/loki.py'):
            logging.warning('loki.py ya existe. Se sobrescribirá.')
        
        subprocess.run(['cp', 'loki.py', '/usr/share/loki/loki.py'], check=True)

        # Crear un script ejecutable en /usr/bin llamado loki
        cmnd = '#! /bin/sh\nexec python3 /usr/share/loki/loki.py "$@"\n'
        with open('/usr/bin/loki', 'w') as file:
            file.write(cmnd)
        
        os.chmod('/usr/bin/loki', 0o755)
        os.chmod('/usr/share/loki/loki.py', 0o755)

        # Instalar macchanger y otras dependencias si no están instaladas
        try:
            subprocess.run(['sudo', 'apt', 'install', 'macchanger', '-y'], check=True)
        except subprocess.CalledProcessError:
            logging.warning("macchanger ya está instalado o hubo un problema durante la instalación.")

        logging.info('¡Felicidades! Loki IP/MAC Changer ha sido instalado exitosamente.')
        logging.info('Escribe "loki" en el terminal para usarlo.')
    except Exception as e:
        logging.error(f'Error durante la instalación: {e}')

def desinstalar():
    verificar_root()
    try:
        if os.path.exists('/usr/share/loki'):
            subprocess.run(['rm', '-rf', '/usr/share/loki'], check=True)
        if os.path.exists('/usr/bin/loki'):
            subprocess.run(['rm', '/usr/bin/loki'], check=True)
        logging.info('Loki IP/MAC Changer ha sido eliminado exitosamente.')
    except Exception as e:
        logging.error(f'Error durante la desinstalación: {e}')

def main():
    if len(sys.argv) < 2:
        print('Uso: python3 install.py [install|uninstall]')
        sys.exit(1)

    if sys.argv[1].lower() == 'install':
        instalar()
    elif sys.argv[1].lower() == 'uninstall':
        desinstalar()
    else:
        print('Opción no válida. Usa "install" o "uninstall".')

if __name__ == "__main__":
    main()

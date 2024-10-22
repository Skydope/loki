
# Loki IP/MAC Changer 🕵️‍♂️🦹‍♂️

Loki es un script en Python para cambiar la dirección IP, la dirección MAC y el User Agent de manera periódica utilizando Tor, brindando una capa adicional de privacidad y anonimato en tus actividades en línea. El script permite elegir diferentes User-Agents para las solicitudes HTTP y tiene opciones de configuración personalizables.

## 🚀 Características

- 🔄 Cambia la dirección IP periódicamente utilizando la red Tor.
- 🖥️ Cambia la dirección MAC de la interfaz de red.
- 🌐 Permite especificar un User-Agent personalizado para las solicitudes HTTP.
- 🧩 Selección de varios User-Agents predefinidos.
- 📜 Documentación de ayuda integrada en el script.
- ⏱️ Configuración de intervalos de tiempo y número de repeticiones para el cambio de IP.

## 📋 Requisitos previos

Para usar Loki, asegúrate de tener los siguientes componentes instalados:

- **Python 3.x**
- **Tor**
- **macchanger** (para cambiar la dirección MAC)
- Permisos de **superusuario** (sudo) para algunos comandos.

### Instalación de dependencias

Si no tienes Tor y macchanger instalados, puedes instalarlos en una distribución basada en Debian con:

```bash
sudo apt update
sudo apt install tor macchanger -y
```

## 📦 Instalación

1. Clona este repositorio en tu máquina local:
   
   ```bash
   git clone https://github.com/skydope/loki.git
   cd loki
   ```

2. Asegúrate de que `loki.py` sea ejecutable:

   ```bash
   chmod +x loki.py
   ```

3. Ejecuta el script:

   ```bash
   python3 loki.py
   ```

## ✨ Uso

```bash
python3 loki.py [opciones]
```

### Opciones

- `-h`, `--help`: Muestra el mensaje de ayuda.
- `-t`, `--time [segundos]`: Tiempo en segundos para cambiar la IP. Por defecto, es 60 segundos.
- `-l`, `--loop [número]`: Número de veces que se cambiará la IP. Si es 0, cambia indefinidamente.
- `-m`, `--mac`: Cambia la dirección MAC también. Requiere la opción `-i`.
- `-i`, `--interface [nombre]`: Interfaz de red para cambiar la dirección MAC (e.g., eth0, wlan0).
- `-u`, `--user-agent [cadena]`: Establece un User-Agent personalizado para las solicitudes HTTP.
- `--user-agent-1`: Selecciona el User-Agent 1 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36).
- `--user-agent-2`: Selecciona el User-Agent 2 (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15).
- `--user-agent-3`: Selecciona el User-Agent 3 (Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36).
- `--user-agent-4`: Selecciona el User-Agent 4 (Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1).
- `--user-agent-5`: Selecciona el User-Agent 5 (Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0).

### Ejemplos de uso

1. **Cambio de IP cada 120 segundos, cinco veces, utilizando el User-Agent 1:**

   ```bash
   python3 loki.py -t 120 -l 5 --user-agent-1
   ```

2. **Cambio de IP indefinidamente cada 60 segundos, con un User-Agent personalizado:**

   ```bash
   python3 loki.py --time 60 --loop 0 -u "MyCustomUserAgent/1.0"
   ```

3. **Cambio de IP y dirección MAC para la interfaz `eth0` cada 180 segundos, indefinidamente:**

   ```bash
   python3 loki.py -t 180 -l 0 -m -i eth0
   ```

## 🧑‍💻 Lista de User-Agents

1. **User-Agent 1:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36`
2. **User-Agent 2:** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15`
3. **User-Agent 3:** `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36`
4. **User-Agent 4:** `Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1`
5. **User-Agent 5:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0`

## ⚠️ Notas de seguridad

- Este script cambia configuraciones de red que pueden afectar la conectividad. Úsalo con precaución.
- El cambio de dirección MAC puede no funcionar en todas las interfaces o sistemas.
- Cambiar la IP y la dirección MAC frecuentemente puede afectar la estabilidad de la conexión.

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si tienes alguna sugerencia o encuentras algún problema, por favor abre un *issue* o envía un *pull request*.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🧙 Autor

Creado con ❤️ por [Skydope](https://github.com/skydope).

## ⚠️ Usar Responsablemente 
El autor no se hace responsable de los usos indebidos o maliciosos de esta herramienta. Cada usuario asume la responsabilidad total de cualquier acción realizada con ella. Esta herramienta ha sido creada con fines educativos y de aprendizaje sobre la manipulación de IP y MAC. Se recomienda encarecidamente su uso ético y legal en entornos controlados y con el consentimiento adecuado.


---

¡Espero que Loki sea útil para mejorar tu privacidad y seguridad en línea! 🔐🚀

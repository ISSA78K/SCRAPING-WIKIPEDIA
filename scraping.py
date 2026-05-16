import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL
url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n"

# Encabezados para evitar bloqueo
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Solicitud
respuesta = requests.get(url, headers=headers)

# Analizar HTML
soup = BeautifulSoup(respuesta.text, "html.parser")

# Buscar TODAS las tablas
tablas = soup.find_all("table")

print("Cantidad de tablas encontradas:", len(tablas))

# Usaremos la primera tabla
tabla = tablas[0]

# Obtener filas
filas = tabla.find_all("tr")

# Lista de datos
datos = []

# Recorrer filas
for fila in filas[1:]:

    columnas = fila.find_all(["td", "th"])

    if len(columnas) >= 3:

        pais = columnas[1].get_text(strip=True)

        poblacion = columnas[2].get_text(strip=True)

        datos.append({
            "País": pais,
            "Población": poblacion
        })

# Crear tabla
df = pd.DataFrame(datos)

# Mostrar resultados
print(df)

# Guardar CSV
df.to_csv("paises_poblacion.csv", index=False)

print("\nArchivo CSV creado correctamente")
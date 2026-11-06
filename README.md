# Herramientas en Python: MP3 de YouTube y consulta de teléfonos

Repositorio con dos scripts de Python independientes:

1. **Descargador de MP3** – descarga el audio de videos de YouTube en formato MP3 a **190 kbps**.
2. **Consulta de teléfonos** – muestra datos públicos de un número telefónico, como el **operador** y la **ubicación**.

---

## Estructura del repositorio

```
.
├── audi.py        # Script 1: YouTube → MP3 (190k)
├── phonumber.py   # Script 2: datos públicos de un teléfono
└── README.md
```

---

## Requisitos

- Python 3.8 o superior
- [FFmpeg](https://ffmpeg.org/download.html) instalado y agregado al PATH
- Librerías de Python:

```bash
pip install yt-dlp 
```

### Instalar FFmpeg

| Sistema | Comando |
|---------|---------|
| Windows | `winget install ffmpeg` o descargarlo desde ffmpeg.org y agregarlo al PATH |
| macOS | `brew install ffmpeg` |
| Ubuntu/Debian | `sudo apt install ffmpeg` |

Verifica la instalación con:

```bash
ffmpeg -version
```

---

## Script 1: Descargador de MP3 

Descarga el audio de un video de YouTube y lo convierte a MP3 con calidad de **190 kbps**, usando **yt-dlp** para la descarga y **FFmpeg** para la conversión.

### Uso

```bash
python audi.py
```

Pega el enlace del video cuando el programa lo solicite:

```
Ingresa el enlace de YouTube: https://www.youtube.com/watch?v=XXXXXXXXXXX
```

El archivo `.mp3` se guardará en la carpeta indicada por el script.

### Cómo funciona

- `yt-dlp` obtiene la mejor pista de audio disponible.
- `FFmpeg` la convierte a MP3 a 190k.

---



## Script 2: Consulta de teléfonos (`phonumber.py`)

Muestra información **pública** de un número telefónico: operador y ubicación (país o región).

### Formato del número

El número debe escribirse **exactamente** en formato internacional, con el signo `+`, el código del país y sin espacios ni guiones:

```
+573121234567
```

| Parte | Significado |
|-------|-------------|
| `+` | Prefijo internacional |
| `57` | Código del país (Colombia) |
| `3121234567` | Número de teléfono |

### Uso

```bash
python phonumber.py
```

```
Ingresa el número: +573121234567
```

### Ejemplo de salida

```
Número:     +573121234567
Operador:   Claro
Ubicación:  Colombia
```

> ## NOTA:
> Los datos corresponden al operador y la región asignados originalmente al número. Si el número fue portado a otra compañía, el operador mostrado podría no ser el actual.

---

## Aviso legal y de uso responsable

- Usa el descargador de MP3 solo con contenido propio, de dominio público o que tengas permiso de descargar. Descargar material protegido por derechos de autor puede violar los términos de servicio de YouTube y las leyes de tu país.
- La consulta de teléfonos solo muestra información pública y general. No debe usarse para acosar, rastrear o vulnerar la privacidad de otras personas.
- El autor no se hace responsable del mal uso de estas herramientas.

---

## Problemas frecuentes

| Problema | Solución |
|----------|----------|
| `ffmpeg not found` | Instala FFmpeg y agrégalo al PATH; reinicia la terminal |
| Error de descarga en yt-dlp | Actualiza: `pip install -U yt-dlp` |
| Número inválido | Revisa que empiece por `+` y el código de país, sin espacios |

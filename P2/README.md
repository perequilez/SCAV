# PRÀCTICA 2: SCAV


## Descripció

Aquest repositori conté un script de Python que utilitza la utilitat ffmpeg per a realitzar diverses operacions en vídeos. Cada exercici es descriu a continuació juntament amb una captura de la solució i instruccions sobre com exacutar-los.

Primer de tot però, importem la funció "convert_to_bw_and_compress" de la pràctica anterior la qual utilitzarem en l'exercici 5:
```python
# Importem la funció per l'exercici 5
from rgb_yuv import convert_to_bw_and_compress
```
I definim el path del video "Big Buck Bunny":
```python
#  Definim el path del video "Big Buck Bunny"
bunny = '/Users/perequilez/Desktop/BigBuckBunny.mp4'
```
Tenint en compte la sea informació la qual es veurà modificada com veurem, en els següents exercicis:

![Vídeo Original](Informació_vídeo_original.png)

## Exercici 1 - Conversió de Vídeo a MP2

Aquest exercici demostra com convertir un fitxer de vídeo a un format MP2 utilitzant `ffmpeg`. La funció `convert_video_to_mpeg` realitza aquesta conversió i guarda la informació del vídeo en un fitxer de text.

```python
def convert_video_to_mpeg(input_video, output_mp2_file, info_file='video_info.txt'):
    try:
        # Utilitzem 'ffmpeg' per convertir el vídeo d'entrada a un fitxer de vídeo MP2
        conversion_command = f'ffmpeg -i "{input_video}" -c:v mpeg2video -q:v 2 -an "{output_mp2_file}"'
        # Executem la comanda 'ffmpeg' per realitzar la conversió
        subprocess.run(conversion_command, shell=True)

        # Utilitzem 'ffmpeg' per analitzar la informació del vídeo i guardar-la en un fitxer de text
        info_command = f'ffmpeg -i "{output_mp2_file}" 2> "{info_file}"'
        # Executem la comanda 'ffmpeg' per obtenir la informació del vídeo
        subprocess.run(info_command, shell=True)

        return True, f"Vídeo convertit a MP2, desat com a {output_mp2_file} i informació desada com a {info_file}"
    except subprocess.CalledProcessError as e:
        # Si hi ha un error en l'execució de les comandes 'ffmpeg', capturem l'excepció i la retornem
        return False, str(e)
```
#### Resultat exercici 1:
Podeu trobar el resultat de l'exercici en el mateix repositori P2/video_info.txt.

En el cas del video haureu d'executar el codi per veure el resultat:

![Resultat EX1](Output_EX1.png)

## Exercici 2 - Modificació de la Resolució del Vídeo

Aquest exercici implica la modificació de la resolució d'un vídeo utilitzant ffmpeg. La funció modify_resolution realitza aquesta operació.
```python
def modify_resolution(input_video, output_video, width, height):
    try:
        # Utilitzem 'ffmpeg' per modificar la resolució del vídeo
        ffmpeg_command = f'ffmpeg -i {input_video} -vf "scale={width}:{height}" {output_video}'
        # Executem la comanda 'ffmpeg' per canviar la resolució del vídeo d'entrada i guardar-lo com a vídeo de sortida
        subprocess.run(ffmpeg_command, shell=True, check=True)

        return True, f"Resolució del vídeo modificada i desada com a {output_video}"
    except subprocess.CalledProcessError as e:
        # Si hi ha un error en l'execució de la comanda 'ffmpeg', capturem l'excepció i la retornem
        return False, str(e)
```
#### Resultat exercici 2:
En el cas del video haureu d'executar el codi per veure el resultat:
![Resultat_EX2](Output_EX2.png)

## Exercici 3 - Canvi de Submostreig de Cromàtica

Aquest exercici implica el canvi de submostreig de cromàtica d'un vídeo utilitzant ffmpeg. La funció change_chroma_subsampling realitza aquesta operació.

```python
def change_chroma_subsampling(input_video, output_video, subsampling):
    try:
        # Utilitzem 'ffmpeg' per canviar el submostreig de croma del vídeo d'entrada
        ffmpeg_command = f'ffmpeg -i {input_video} -vf "format={subsampling}" -c:a copy {output_video}'
        # Executem la comanda 'ffmpeg' per realitzar el canvi de submostreig de croma
        subprocess.run(ffmpeg_command, shell=True, check=True)

        return True, f"Submostreig de croma canviat i desat com a {output_video}"
    except subprocess.CalledProcessError as e:
        # Si hi ha un error en l'execució de la comanda 'ffmpeg', capturem l'excepció i la retornem
        return False, str(e)
```
#### Resultat exercici 3:
En el cas del video haureu d'executar el codi per veure el resultat:
![Resultat_EX2](Output_EX3.png)

## Exercici 4 - Lectura de la Informació del Vídeo

Aquest exercici implica la lectura i impressió de la informació d'un vídeo en format JSON utilitzant ffprobe. La funció read_video_info realitza aquesta operació.

```python
def read_video_info(video_path):
    try:
        # Executem ffprobe per obtenir la informació del vídeo en format JSON
        info_command = f'ffprobe -v error -select_streams v:0 -show_entries stream=codec_type,width,height,r_frame_rate,duration,bit_rate -of json "{video_path}"'
        info_output = subprocess.check_output(info_command, shell=True).decode('utf-8')

        # Analitzem la sortida JSON
        video_info = json.loads(info_output)
        # Guardem les dades rellevants
        stream_info = video_info['streams'][0]

        # Imprimim les dades rellevants
        print("Exercici 4: Informació del vídeo:")
        print(f"Tipus de codec: {stream_info['codec_type']}")
        print(f"Resolució: {stream_info['width']}x{stream_info['height']}")
        print(f"Taxa de quadres: {stream_info['r_frame_rate']}")
        print(f"Durada: {stream_info['duration']} segons")
        print(f"Taxa de bits: {stream_info['bit_rate']} bps")
        return True, f"Dades obtingudes correctament"
    except subprocess.CalledProcessError as e:
        # Si hi ha un error en l'execució de la comanda 'ffmpeg', capturem l'excepció i la retornem
        return False, str(e)
```
#### Resultat exercici 4:
```python
Exercici 4: Informació del vídeo:
Tipus de codec: video
Resolució: 1920x1080
Taxa de quadres: 60/1
Durada: 634.566667 segons
Taxa de bits: 3813575 bps
```
## Exercici 5 - Extracció d'un Marc Aleatori i Conversió a Blanc i Negre

Aquest exercici implica l'extracció d'un marc aleatori d'un vídeo, que posteriorment es converteix a blanc i negre. Aquest exercici fa servir la funció extract_random_frame_and_convert_to_bw i inclou una crida a una funció addicional.

```python
def extract_random_frame_and_convert_to_bw(video_path, output_image_path, quality=2):
    try:
        # Obtenim la durada del vídeo
        info_command = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
        duration = float(subprocess.check_output(info_command, shell=True))

        # Escollim un instant aleatori dins de la durada del vídeo
        random_time = random.uniform(0, duration)

        # Extraiem el frame aleatori i el desem com a imatge
        extract_command = f'ffmpeg -ss {random_time} -i "{video_path}" -vframes 1 "{"random_frame.jpeg"}"'
        subprocess.run(extract_command, shell=True)

        # Apliquem la funció convert_to_bw_and_compress al frame random i el guardem
        convert_to_bw_and_compress("random_frame.jpeg", output_image_path, quality)
        return True, f"Conversió a bw del frame aleatori feta i desat com a {output_image_path}"
    except subprocess.CalledProcessError as e:
        # Si hi ha un error en l'execució de la comanda 'ffmpeg', capturem l'excepció i la retornem
        return False, str(e)
```
#### Resultat exercici 5:
Un exemple de resultat sería:
![Resultat_EX5](Output_EX5.jpeg)

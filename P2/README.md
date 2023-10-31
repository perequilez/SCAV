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

```
#### Resultat exercici 3:
```python

```

## Exercici 4 - Lectura de la Informació del Vídeo

Aquest exercici implica la lectura i impressió de la informació d'un vídeo en format JSON utilitzant ffprobe. La funció read_video_info realitza aquesta operació.

```python

```
#### Resultat exercici 4:
```python

```

## Exercici 5 - Extracció d'un Marc Aleatori i Conversió a Blanc i Negre

Aquest exercici implica l'extracció d'un marc aleatori d'un vídeo, que posteriorment es converteix a blanc i negre. Aquest exercici fa servir la funció extract_random_frame_and_convert_to_bw i inclou una crida a una funció addicional.

```python

```
#### Resultat exercici 5:
```python

```

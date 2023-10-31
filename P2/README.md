# PRÀCTICA 2: SCAV


## Descripció

Aquest repositori conté un script de Python que utilitza la utilitat ffmpeg per a realitzar diverses operacions en vídeos. Cada exercici es descriu a continuació juntament amb una captura de la solució i instruccions sobre com exacutar-los.

Primer de tot però, definim el path del video "Big Buck Bunny":
```python
#  Definim el path del video "Big Buck Bunny"
bunny = '/Users/perequilez/Desktop/BigBuckBunny.mp4'
```
![Imatge Original](image.jpg)


## Exercici 1 - Conversió de Vídeo a MP2

Aquest exercici demostra com convertir un fitxer de vídeo a un format MP2 utilitzant `ffmpeg`. La funció `convert_video_to_mpeg` realitza aquesta conversió i guarda la informació del vídeo en un fitxer de text.

```python
# Definim path de la imatge
img = '/Users/perequilez/Desktop/image.jpg' # Exemple
```
#### Resultat exercici 1:
```python

```

## Exercici 2 - Modificació de la Resolució del Vídeo

Aquest exercici implica la modificació de la resolució d'un vídeo utilitzant ffmpeg. La funció modify_resolution realitza aquesta operació.
```python

```
#### Resultat exercici 1:
```python

```
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

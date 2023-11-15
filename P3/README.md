# PRÀCTICA 3: SCAV


## Descripció

Aquest repositori conté un script de Python amb els diferents exercicis de la tercera pràctica. Els exercicis es descriuran a continuació, amb instruccions sobre com executar-los.

Primer de tot però, importem les funcions "download_and_integrate_subtitles" i "extract_and_show_yuv_histogram" dels fitxers .py auxilars per tal de poder executar els exercicis 5 i 6:
```python
# Importem les dues funcions necessàrries dels fitxers auxiliars per tal de poder realitzar els exercicis 5 i 6:
from python_video_2_Ex4 import download_and_integrate_subtitles
from python_video_2_Ex6 import extract_and_show_yuv_histogram
```
I definim el path dels vídeos "Big Buck Bunny" i "Big Buck Bunny", amb els quals realitzarem els exercicis:
```python
#  Definim el path del video "Big Buck Bunny de 9s"
bunny_9s = '/Users/perequilez/Desktop/BigBuckBunny_9s.mp4'

#  Definim el path del video "Big Buck Bunny"
bunny = '/Users/perequilez/Desktop/BigBuckBunny.mp4'
```
Abans de començar amb els exercicis, tal i com es demana en l'exercici 1 creem una classe "VideoAnalyzer" en la qual hi implementarem alguns dels exercicis de la pràctica:
```python
class VideoAnalyzer:
          .
          .
          .
```


## Exercici 1 - Afegir Overlay de Blocs Macros i Vectors de Moviment

Aquest exercici aplica un overlay al vídeo amb informació sobre els blocs macros i vectors de moviment.

![Exemple de sortida de l'Exercici 1](enllaç_a_la_imatge1)


## Exercici 2 - Crear Nou Contenidor de Vídeo

Aquest exercici crea un nou contenidor de vídeo a partir d'una secció de 50 segons del vídeo d'entrada amb àudios en diferents formats.

![Exemple de sortida de l'Exercici 2](enllaç_a_la_imatge2)

## Exercici 3 - Comptar Pistes de Vídeo

Aquest exercici compta el nombre de pistes de vídeo en el fitxer d'entrada.

![Exemple de sortida de l'Exercici 3](enllaç_a_la_imatge3)

## Exercici 4 - Descarregar i Integrar Subtítols

Aquest exercici descarrega subtítols d'una URL i els integra al fitxer de vídeo d'entrada.


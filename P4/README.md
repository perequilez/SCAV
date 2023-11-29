# PRÀCTICA 4: SCAV

## Descripció

Aquest repositori conté un script de Python amb els diferents exercicis de la quarta pràctica. Els exercicis es descriuran a continuació, amb instruccions sobre com executar-los.

Primer de tot però, importem la funció " export_video_comparison" del fitxer .py auxilar per a realitzar l'exercici 2:

```python
# Importem la funció export_video_comparison del fitxer EX_2.py
from EX_2 import export_video_comparison
```
També definim el path del vídeo "Big Buck Bunny 9s", amb el qual realitzarem els exercicis:
```python
#  Definim el path del video "Big Buck Bunny de 9s"
bunny_9s = '/Users/perequilez/Desktop/BigBuckBunny_9s.mp4'
```

## Exercici 1 - Modificar Resolució i Convertir a VP8, VP9, H.265, AV1

Aquest exercici permet modificar la resolució d'un vídeo i convertir-lo als formats VP8, VP9, H.265 i AV1. Les funcions es troben dins la classe VideoConverter.

Abans de començar doncs, creem una classe "VideoConverter" en la qual hi implementarem les diferents funcions de l'exercici 1:
```python
class VideoConverter:
          .
          .
          .
```
Un cop creada la classe ja hi podem implementar les diferents funcions de l'exercici 1:
```python
# EXERCICI 1
class VideoConverter:
    @staticmethod
    def modify_resolution(input_video, output_video, width, height):
        try:
            # Utilitzem 'ffmpeg' per modificar la resolució del vídeo
            ffmpeg_command = (f'ffmpeg -i {input_video} -vf "scale={width}:{height}" {output_video}_{width}x{height}_.mp4')
            # Executem la comanda 'ffmpeg' per canviar la resolució del vídeo d'entrada i guardar-lo com a vídeo de sortida
            subprocess.run(ffmpeg_command, shell=True, check=True)

            return True, f"Hem modificat la resolució del vídeo i l'hem guardat com a {output_video}"
        except subprocess.CalledProcessError as e:
            # Si hi ha un error en l'execució de la comanda 'ffmpeg', capturem l'excepció i la retornem
            return False, str(e)

    @staticmethod
    def convert_to_vp8(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir a VP8
            command = f"ffmpeg -i {input_file} -c:v libvpx -b:v 1M -c:a libvorbis {output_file}_vp8.webm"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a VP8
            print(f"Error durant la conversió a VP8: {e}")

    @staticmethod
    def convert_to_vp9(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir a VP9
            command = f"ffmpeg -i {input_file} -c:v libvpx-vp9 -b:v 1M -c:a libvorbis {output_file}_vp9.webm"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a VP9
            print(f"Error durant la conversió a VP9: {e}")

    @staticmethod
    def convert_to_h265(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir a H.265
            command = f"ffmpeg -i {input_file} -c:a copy -c:v libx265 {output_file}_h265.mp4"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a H.265
            print(f"Error durant la conversió a H.265: {e}")

    @staticmethod
    def convert_to_av1(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir a AV1
            command = f"ffmpeg -i {input_file} -c:v libaom-av1 -crf 30 {output_file}_av1.mkv"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a AV1
            print(f"Error durant la conversió a AV1: {e}")

```


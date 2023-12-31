# PRÀCTICA 3: SCAV


## Descripció

Aquest repositori conté un script de Python amb els diferents exercicis de la tercera pràctica. Els exercicis es descriuran a continuació, amb instruccions sobre com executar-los.

Primer de tot però, importem les funcions "download_and_integrate_subtitles" i "extract_and_show_yuv_histogram" dels fitxers .py auxilars per a realitzar els exercicis 4,5 i 6:
```python
# Importem les dues funcions necessàrries dels fitxers auxiliars per tal de poder realitzar els exercicis 5 i 6:
from python_video_2_Ex4 import download_and_integrate_subtitles
from python_video_2_Ex6 import extract_and_show_yuv_histogram
```
També definim el path dels vídeos "Big Buck Bunny" i "Big Buck Bunny", amb els quals realitzarem els exercicis:
```python
#  Definim el path del video "Big Buck Bunny de 9s"
bunny_9s = '/Users/perequilez/Desktop/BigBuckBunny_9s.mp4'

#  Definim el path del video "Big Buck Bunny"
bunny = '/Users/perequilez/Desktop/BigBuckBunny.mp4'
```
Abans de començar amb els exercicis, tal i com es demana en l'exercici 1 creem una classe "VideoAnalyzer" en la qual hi implementarem els exercicis 1,2,3 de la pràctica:
```python
class VideoAnalyzer:
          .
          .
          .
```


## Exercici 1 - Afegir Overlay de Blocs Macros i Vectors de Moviment

Aquest exercici utilitza la biblioteca 'ffmpeg' per afegir un overlay al vídeo d'entrada, mostrant els blocs macro i vectors de moviment.
```python
 # EXERCICI 1
    @staticmethod
    def display_macroblocks_and_vectors(input_video, output_video):
        try:
            # Utilitzem ffmpeg per afegir l'overlay amb els blocs macro i vectors de moviment
            overlay_command = f'ffmpeg -flags2 +export_mvs -i {input_video} -vf codecview=mv=pf+bf+bb {output_video}'
            subprocess.run(overlay_command, shell=True)
            return True, f"Overlay aplicat i desat com a {output_video}"
        except subprocess.CalledProcessError as e:
            # Si hi ha un error en l'execució de la comanda 'ffmpeg', capturem l'excepció i la retornem
            return False, str(e)
```
#### Resultat exercici 1:
Per tal de veure el vídeo haureu d'executar el codi. Tot seguit podeu veure una captura del vídeo resultant:

<img src='Output_EX1.png' width='300'>


## Exercici 2 - Crear Nou Contenidor de Vídeo

Aquest exercici crea un nou contenidor de vídeo a partir d'una secció de 50 segons del vídeo d'entrada amb àudios en diferents formats.

```python
 # EXERCICI 2
    @staticmethod
    def create_new_video_container(input_video, output_video):
        try:
            # Utilitzem ffmpeg per tallar el vídeo d'entrada als primers 50 segons
            cut_video_command = f'ffmpeg -i {input_video} -ss 00:00:00 -t 00:00:50 -c:a copy {"temp_cut.mp4"}'
            subprocess.run(cut_video_command, shell=True)

            # Utilitzem ffmpeg per exportar l'àudio del vídeo tallat com a MP3 mono
            export_mp3_mono_command = f'ffmpeg -i {"temp_cut.mp4"} -vn -ar 44100 -ac 1 -ab 192k -f mp3 {"temp_mono.mp3"}'
            subprocess.run(export_mp3_mono_command, shell=True)

            # Utilitzem ffmpeg per exportar l'àudio del vídeo tallat com a MP3 estèreo amb bitrate més baix
            export_mp3_stereo_low_bitrate_command = f'ffmpeg -i {"temp_cut.mp4"} -vn -ar 44100 -ac 2 -ab 128k -f mp3 {"temp_stereo_low.mp3"}'
            subprocess.run(export_mp3_stereo_low_bitrate_command, shell=True)

            # Utilitzem ffmpeg per exportar l'àudio del vídeo tallat en format AAC
            export_aac_command = f'ffmpeg -i {"temp_cut.mp4"} -vn -c:a aac -strict -2 -b:a 128k {"temp_aac.aac"}'
            subprocess.run(export_aac_command, shell=True)

            # Utilitzem ffmpeg per combinar el vídeo tallat amb els tres fitxers d'àudio exportats
            combine_video_audio_command = f'ffmpeg -i {"temp_cut.mp4"} -i {"temp_mono.mp3"} -i {"temp_stereo_low.mp3"} -i {"temp_aac.aac"} -map 0 -map 1 -map 2 -map 3 -c:v copy -c:a copy {output_video}'
            subprocess.run(combine_video_audio_command, shell=True)

            # Eliminem els fitxers temporals utilitzats en els processos anteriors
            subprocess.run('rm temp_cut.mp4 temp_mono.mp3 temp_stereo_low.mp3 temp_aac.aac', shell=True)

            return True, f'Creat un nou contenidor de vídeo com a {output_video}'
        except subprocess.CalledProcessError as e:
            return False, str(e)
```
#### Resultat exercici 2:
Per tal de veure el vídeo haureu d'executar el codi. En aquest cas el vídeo de sortida en si és el mateix però retallat 50s i amb els contenidors que hem creat.

## Exercici 3 - Comptar Pistes de Vídeo

Aquest exercici fa servir la comanda ffprobe per obtenir informació detallada sobre les pistes d'un vídeo. 
```python
# EXERCICI 3
    @staticmethod
    def count_tracks(input_video):
        # Creem una llista amb la comanda ffprobe i els paràmetres necessaris per obtenir informació detallada sobre les pistes
        info_command = ["ffprobe", input_video, "-print_format", "json", "-show_streams"]

        # Executem la comanda i capturem la sortida
        result = subprocess.run(info_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # La sortida exitosa conté informació detallada sobre les pistes
        tracks_info = json.loads(result.stdout)

        # Imprimim la informació sobre cada pista
        for i, track in enumerate(tracks_info["streams"], start=1):
            print(f"Pista {i}:\n"
                  f"  Tipus: {track['codec_type']}\n"
                  f"  Format: {track.get('codec_name', '-')}\n"
                  f"  Resolució: {track.get('width', '-')}x{track.get('height', '-')}\n")

        # Retornem informació de les pistes
        return tracks_info["streams"]
```

#### Resultat exercici 3:
Si executem l'exercici passant-li d'entrada el vídeo de sortida de l'exercici 2 obtenim:

```python
Pista 1:
  Tipus: video
  Format: h264
  Resolució: 1920x1080

Pista 2:
  Tipus: audio
  Format: aac
  Resolució: -x-

Pista 3:
  Tipus: audio
  Format: mp3
  Resolució: -x-

Pista 4:
  Tipus: audio
  Format: mp3
  Resolució: -x-

Pista 5:
  Tipus: audio
  Format: aac
  Resolució: -x-
```

## Exercici 4 - Descarregar i Integrar Subtítols

Aquest exercici descarrega subtítols d'una URL (dirigida al mateix repositori, "subtitles.str") i utilitza la comanda ffmpeg per integrar subtítols al vídeo d'entrada, creant així un nou fitxer de vídeo amb els subtítols inclosos.

```python
# EXERCICI 4
def download_and_integrate_subtitles(video_file, url, output_video_file, output_file):
    try:
        # Realitzem una sol·licitud HTTP per obtenir els subtítols
        response = requests.get(url)

        # Verifiquem si la sol·licitud s'ha completat amb èxit
        if response.status_code == 200:
            # Convertim la resposta a format JSON i extraiem "blob" i "rawLines"
            content_info = json.loads(response.text)
            blob_content = content_info["payload"]["blob"]["rawLines"]

            # Guardem el contingut en un fitxer local
            with open("subtitles.srt", "w", encoding="utf-8") as file:
                file.write("\n".join(blob_content))

        # Integrem els subtítols al vídeo
        integration_command = f'ffmpeg -i "{video_file}" -vf "subtitles={output_file}" -c:a copy "{output_video_file}"'
        subprocess.run(integration_command, shell=True)

        print(f'Subtítols integrats a "{video_file}" i desats com a "{output_video_file}"')

    except Exception as e:
        print(f"S'ha produït un error: {e}")
```


## Exercici 5 - Descarregar i Integrar Subtítols

En aquest exercici, es realitza una herència (explicat al pricnipi del fitxer README) del nou script creat en l'exercici anterior. Després, es crida a aquesta funció heretada per executar-la, en la funió principal main().
```python
# EXERCICI 5
    elif args.exercici == 5:
        # Executem l'Exercici 4 per processar un vídeo amb subtítols
        download_and_integrate_subtitles(bunny_9s, "https://github.com/perequilez/SCAV/blob/main/P3/subtitles.srt","output_video_EX5.mp4", "subtitles.srt")
        print("Operació completada. Subtítols integrats i vídeo desat.")
```
#### Resultat exercici 5:
Per tal de veure el vídeo haureu d'executar el codi. Tot seguit podeu veure una captura del vídeo resultant:

<img src='Output_EX5.png' width='300'>

## Exercici 6 - Descarregar i Integrar Subtítols

Aquest exercici fa servir la comanda ffplay per mostrar l'histograma YUV d'un vídeo. 
```python
# EXERCICI 6
def extract_and_show_yuv_histogram(input_video, output_video):
    try:
        # Utilitzem la comanda ffplay per extreure i mostrar l'histograma YUV
        yuv_histogram_command = [
            'ffplay', input_video, '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay',
            '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay',
            '-vf', f'scale=1280:720,setsar=1,format=yuv420p -y {output_video}'
        ]
        # Executem la comanda
        subprocess.run(yuv_histogram_command)

        return True, f"YUV histogram extracted and saved as {output_video}"

    except subprocess.CalledProcessError as e:
        return False, str(e)
```
#### Resultat exercici 6:
Per tal de veure el vídeo haureu d'executar el codi. Tot seguit podeu veure una captura del viídeo resultant:

<img src='Output_EX6.png' width='300'>

## Com executar l'script

Per a executar l'script i provar els diversos exercicis, utilitzem la funció `main()`, a través de la terminal i especificant el número d'exercici com a argument. Podem veure els exercicis definits a la funció principal, `main()`:

```python

if __name__ == "__main__":
    # Creem un analitzador d'arguments de línia de comandes
    parser = argparse.ArgumentParser(
        description='Executa un exercici específic')  # Creem un objecte d'analitzador d'arguments amb una descripció
    parser.add_argument('exercici', type=int,
                        help="Número de l'exercici (1-3,5 o 6)")  # Afegim un argument que espera un número d'exercici
    args = parser.parse_args()  # Analitzem els arguments de la línia de comandes

    if args.exercici == 1:
        # Executem l'Exercici 1 per afegir l'overlay de macroblocs i vectors de moviment
        success, message = VideoAnalyzer.display_macroblocks_and_vectors(bunny_9s, 'output_EX1.mp4')
        if success:
            print(f"Operació completada amb èxit: {message}")
        else:
            print(f"Error: {message}")

    elif args.exercici == 2:
        # Executem l'Exercici 2 per crear un nou contenidor de vídeo
        success, message = VideoAnalyzer.create_new_video_container(bunny, 'output_EX2.mp4')
        if success:
            print(f"Operació completada amb èxit: {message}")
        else:
            print(f"Error: {message}")

    elif args.exercici == 3:
        # Executem l'Exercici 3 per comptar les pistes del vídeo d'entrada
        VideoAnalyzer.count_tracks("output_EX2.mp4")
    # EXERCICI 5
    elif args.exercici == 5:
        # Executem l'Exercici 4 per processar un vídeo amb subtítols
        download_and_integrate_subtitles(bunny_9s, "https://github.com/perequilez/SCAV/blob/main/P3/subtitles.srt","Output_EX5.mp4", "Subtitles.srt")
        print("Operació completada. Subtítols integrats i vídeo desat.")

    elif args.exercici == 6:
        # Executem l'Exercici 6 per extreure l'histograma YUV
        success, message = extract_and_show_yuv_histogram(bunny, "output_EX6.mp4")
        if success:
            print(f"Operació completada amb èxit: {message}")
        else:
            print(f"Error: {message}")

    else:
        print("Número d'exercici no vàlid. Si us plau, trieu un exercici entre 1,2,3,5,6.")


if __name__ == "__main__":
    main()
```

Per tal d'executar un exercici:
Exemple: `python3 python_video_2.py 1`
Això executarà l'exercici 1 amb els valors indicats en el `main()` i proporcionarà els resultats. 

Canviant el número "1" de la comanda podràs executar els diferents exercicis, introduïnt un número entre 1,2,3,5,6.

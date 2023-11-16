import json
import subprocess
import argparse

# Importem les dues funcions necessàrries dels fitxers auxiliars per tal de poder realitzar els exercicis 5 i 6:
from python_video_2_Ex4 import download_and_integrate_subtitles
from python_video_2_Ex6 import extract_and_show_yuv_histogram

#  Definim el path del video "Big Buck Bunny de 9s"
bunny_9s = '/Users/perequilez/Desktop/BigBuckBunny_9s.mp4'

#  Definim el path del video "Big Buck Bunny"
bunny = '/Users/perequilez/Desktop/BigBuckBunny.mp4'


class VideoAnalyzer:
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

    # EXERCICI 3
    @staticmethod
    def count_tracks(input_video):
        # Creem una llista amb la comanda ffprobe i els paràmetres necessaris per obtenir informació detallada sobre les pistes
        info_command = ["ffprobe", input_video, "-print_format", "json", "-show_streams"]

        # Executem la comanda i capturem la sortida
        result = subprocess.run(info_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # La sortida exitosa conté informació detallada sobre les pistes
        tracks_info = json.loads(result.stdout)

        # Imprimim informació sobre cada pista
        for i, track in enumerate(tracks_info["streams"], start=1):
            print(f"Pista {i}:\n"
                  f"  Tipus: {track['codec_type']}\n"
                  f"  Format: {track.get('codec_name', '-')}\n"
                  f"  Resolució: {track.get('width', '-')}x{track.get('height', '-')}\n")

        # Retornem informació de les pistes
        return tracks_info["streams"]


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

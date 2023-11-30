import subprocess
import argparse

from EX_2 import export_video_comparison

input_video = '/Users/perequilez/Desktop/BigBuckBunny_9s.mp4'


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
            # Utilitzem 'ffmpeg' per convertir el vídeo a VP8
            command = f"ffmpeg -i {input_file} -c:v libvpx -b:v 1M -c:a libvorbis {output_file}_vp8.webm"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a VP8
            print(f"Error durant la conversió a VP8: {e}")

    @staticmethod
    def convert_to_vp9(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir el vídeo a VP9
            command = f"ffmpeg -i {input_file} -c:v libvpx-vp9 -b:v 1M -c:a libvorbis {output_file}_vp9.webm"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a VP9
            print(f"Error durant la conversió a VP9: {e}")

    @staticmethod
    def convert_to_h265(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir el vídeo a H.265
            command = f"ffmpeg -i {input_file} -c:a copy -c:v libx265 {output_file}_h265.mp4"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a H.265
            print(f"Error durant la conversió a H.265: {e}")

    @staticmethod
    def convert_to_av1(input_file, output_file):
        try:
            # Utilitzem 'ffmpeg' per convertir el vídeo a AV1
            command = f"ffmpeg -i {input_file} -c:v libaom-av1 -crf 30 {output_file}_av1.mkv"
            subprocess.call(command, shell=True)
        except Exception as e:
            # Capturem qualsevol excepció que pugui produir-se durant la conversió a AV1
            print(f"Error durant la conversió a AV1: {e}")


def main():
    # Creem un analitzador d'arguments de línia de comandes
    parser = argparse.ArgumentParser(description='Executa un exercici')  # Creem un objecte d'analitzador d'arguments amb una descripció
    parser.add_argument('exercici', type=int, help='Número de l\'exercici (1-8)')  # Afegim un argument que espera un número d'exercici
    args = parser.parse_args()  # Analitzem els arguments de la línia de comandes

    # Cridem als exercicis basats en l'argument 'exercici'
    if args.exercici == 1:  # Si l'argument 'exercici' és igual a 1
        # Executem la funció de modificar resolució
        VideoConverter.modify_resolution(input_video, f"output_video_EX1", 360, 240)
    elif args.exercici == 2:  # Si l'argument 'exercici' és igual a 2
        # Executem la funció de convertir a VP8
        VideoConverter.convert_to_vp8(input_video, f"output_video_EX1")
    elif args.exercici == 3:  # Si l'argument 'exercici' és igual a 3
        # Executem la funció de convertir a VP9
        VideoConverter.convert_to_vp9(input_video, f"output_video_EX1")
    elif args.exercici == 4:  # Si l'argument 'exercici' és igual a 4
        # Executem la funció de convertir a H.265
        VideoConverter.convert_to_h265(input_video, f"output_video_EX1")
    elif args.exercici == 5:  # Si l'argument 'exercici' és igual a 5
        # Executem la funció de convertir a AV1
        VideoConverter.convert_to_av1(input_video, f"output_video_EX1")
    elif args.exercici == 6:  # Si l'argument 'exercici' és igual a 6
        # Executem la funció de comparar vídeos
        export_video_comparison("output_video_EX1_vp8.webm", "output_video_EX1_vp9.webm", "output_EX2")
    elif args.exercici == 7:  # Si l'argument 'exercici' és igual a 7
        # Ruta al script que desitgem executar
        script_EX_3_path = 'EX_3_GUI.py'
        # Executem el script
        subprocess.run(['python', script_EX_3_path])
    elif args.exercici == 8:  # Si l'argument 'exercici' és igual a 8
        pass
    else:  # Si l'argument 'exercici' no coincideix amb cap dels valors anteriors
        print("Número d'exercici no vàlid. Si us plau, trieu un número entre 1 i 8")  # Mostrem un missatge d'error


if __name__ == "__main__":
    main()
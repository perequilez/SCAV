import subprocess


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
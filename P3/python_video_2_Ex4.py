import subprocess
import requests
import json


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
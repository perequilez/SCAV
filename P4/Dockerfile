# Usa una imatge base amb FFMPEG
FROM jrottenberg/ffmpeg:4.2-ubuntu

# Estableix el directori de treball
WORKDIR /app

# Copia l'script o els arxius de vídeo que vols processar dins el contenidor
COPY BigBuckBunny_9s.mp4 /app/
COPY BigBuckBunny_9s_vp8.webm /app/

# Comanda per defecte que s'executarà quan el contenidor comenci
CMD ["ffmpeg"]

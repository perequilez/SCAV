# PRÀCTICA 1: SCAV


## Descripció

Aquest repositori conté un script de Python amb els diferents exercicis de la primera pràctica. Els exercicis es descriuran a continuació, amb instruccions sobre com executar-los.

Primer de tot però, definim el path de la nostra imatge:
```python
# Definim path de la imatge
img = '/Users/perequilez/Desktop/image.jpg' # Exemple
```
![Imatge Original](image.jpg)

## Exercici 1 - Conversió RGB a YUV

Aquest exercici implica la conversió de valors RGB a YUV utilitzant una matriu de conversió específica. La funció `rgb2yuv` realitza la conversió i la funció `yuv2rgb` fa la conversió inversa.

```python
def rgb2yuv(rgb):
    # Convertim els valors RGB a YUV aplicant els valors de la matriu de conversió a cada element corresponent

    # Calculem el valor Y (Lluminància)
    y = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

    # Calculem el valor U (Crominància U)
    u = -0.14713 * rgb[0] - 0.288862 * rgb[1] + 0.436 * rgb[2]

    # Calculem el valor V (Crominància V)
    v = 0.615 * rgb[0] - 0.51498 * rgb[1] - 0.10001 * rgb[2]

    # Retornem els valors YUV com una tupla
    return y, u, v


def yuv2rgb(yuv):
    # Convertim els valors YUV a RGB aplicant els valors de la matriu de conversió a cada element corresponent

    # Calculem el valor de R (Vermell)
    r = yuv[0] + 1.13983 * yuv[2]

    # Calculem el valor de G (Verd)
    g = yuv[0] - 0.39465 * yuv[1] - 0.58060 * yuv[2]

    # Calculem el valor de B (Blau)
    b = yuv[0] + 2.03211 * yuv[1]

    # Retornem els valors RGB com una tupla
    return r, g, b
```
#### Resultat exercici 1:
```python
RGB a YUV: (4.744, 1.6023, -1.5299800000000001)
YUV a RGB: (3.0000828965999995, 4.999958693, 8.000049853)
```
## Exercici 2 - Redimensionar i Comprimir una Imatge

En aquest exercici, redimensionem una imatge utilitzant la comanda `ffmpeg` per especificar l'amplada i l'altura desitjades. També es pot ajustar la qualitat de la imatge.

```python
def resize_image(input_file, output_file, width, height):
    try:
        # Construïm la comanda ffmpeg per redimensionar i reduir la qualitat de la imatge
        ffmpeg_command = f'ffmpeg -i {input_file} -vf "scale={width}:{height}" -q:v 2 {output_file}'

        # Executem la comanda ffmpeg
        subprocess.run(ffmpeg_command, shell=True, check=True)
        
        # Imprimim un missatge d'èxit
        print(f"Imatge redimensionada i qualitat reduïda. Sortida guardada com a {output_file}")
    
    except subprocess.CalledProcessError as e:
        # En cas d'error, imprimim un missatge d'error amb detalls
        print(f"Error: {e}")
```
#### Resultat exercici 2:
![Imatge Original](output.jpg)
## Exercici 3 - Patró de Ziga-Zaga

En aquest exercici, llegeixem els bytes d'un arxiu d'entrada i els organitzem en un patró de ziga-zaga.

```python
def serpentine(file_path):
    # Creem una llista per emmagatzemar els bytes llegits en patró de ziga-zaga
    zigzag_bytes = []

    with open(file_path, 'rb') as file:
        byte = file.read(1)
        count = 0
        row, col = 0, 0
        reverse = False

        while byte:
            # Afegim el byte al patró de ziga-zaga
            zigzag_bytes.append(byte)

            # Determinem la següent posició en el patró de ziga-zaga
            if not reverse:
                if col == 0:
                    reverse = True
                    row += 1
                elif row == 0:
                    reverse = True
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == 0:
                    reverse = False
                    col += 1
                elif col == 0:
                    reverse = False
                    row += 1
                else:
                    row += 1
                    col -= 1

            # Llegim el següent byte
            byte = file.read(1)

            count += 1

    return zigzag_bytes
```
#### Resultat exercici 3:
```python
[b'\xff', b'\xd8', b'\xff', b'\xe1', b'0', b'\x02', b'E', b'x', b'i', b'f']
```
## Exercici 4 - Conversió a B/N i Compressió

En aquest exercici, es converteix una imatge a blanc i negre i es pot especificar el nivell de compressió utilitzant ffmpeg.

```python
def convert_to_bw_and_compress(input_image, output_image, compression_quality=0):
    try:
        # Construïm la comanda ffmpeg amb els paràmetres
        ffmpeg_command = f'ffmpeg -i {input_image} -vf format=gray -q:v {compression_quality} {output_image}'

        # Executem la comanda ffmpeg
        subprocess.run(ffmpeg_command, shell=True, check=True)
        print(
            f"Imatge convertida a B/N i comprimida amb qualitat {compression_quality}. Sortida guardada com a {output_image}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
```
#### Resultat exercici 4:
![Imatge Original](output_bw.jpg)

## Exercici 5 - Codificació d'Execució de Longitud

En aquest exercici, es realitza la codificació de longitud d'execució d'una llista de dades.

```python
def run_length_encode(data):
    # Comprovem si la llista d'entrada està buida. Si ho és, retornem una llista buida.
    if not data:
        return []

    # Ordenem la llista d'entrada per assegurar que els elements repetits estiguin adjacents.
    data.sort()

    # Creem una llista buida per emmagatzemar la seqüència codificada.
    encoded_data = []

    # Inicialitzem les variables per fer seguiment de l'element actual i el seu comptador.
    current_value = data[0]
    count = 1

    # Recorrem la llista d'entrada des del segon element fins a l'últim.
    for value in data[1:]:
        # Comparem l'element actual amb l'anterior. Si són iguals, incrementem el comptador.
        if value == current_value:
            count += 1
        else:
            # Si trobem un element diferent, afegim l'element actual i el seu comptador a la seqüència codificada.
            encoded_data.extend([current_value, count])
            # Actualitzem l'element actual i reiniciem el comptador a 1.
            current_value = value
            count = 1

    # Afegim l'últim element i el seu comptador a la seqüència codificada.
    encoded_data.extend([current_value, count])

    # Retornem la seqüència codificada.
    return encoded_data

```
#### Resultat exercici 5:
```python
[1, 3, 2, 3, 3, 2, 4, 2]
```
## Exercici 6 - Transformada de Cosinus Discretes (DCT)

Aquest exercici implica l'ús de la Transformada de Cosinus Discretes (DCT) per a processar imatges. Es mostra com aplicar les funcions DCT i IDCT a una imatge.

```python

# Creem la classe per processar imatges mitjançant la Transformada de Cosinus Discretes (DCT)
class DCTProcessor:
    def __init__(self):
        pass

    # Definim la funció que aplica la DCT a la matriu d'entrada
    def dct2(self, a):
        return dct(dct(a.T, norm='ortho').T, norm='ortho')

    # Definim la funció que aplica la IDCT a la matriu d'entrada
    def idct2(self, a):
        return idct(idct(a.T, norm='ortho').T, norm='ortho')

```
#### Resultat exercici 6:
![Imatge Original](figure_ex6.png)
## Com executar l'script

Per a executar l'script i provar els diversos exercicis, pots utilitzem la funció main() a través de la terminal i especificant el número d'exercici com a argument.

```python
def main():
    # Creem un analitzador d'arguments de línia de comandes
    parser = argparse.ArgumentParser(description='Executa un exercici específic')
    parser.add_argument('exercici', type=int, help='Número de l\'exercici (1-6)')
    args = parser.parse_args()

    # Exemple EX_1
    if args.exercici == 1:
        rgb = (3, 5, 8)
        yuv = rgb2yuv(rgb)
        print(f"RGB a YUV: {yuv}")

        rgb_result = yuv2rgb(yuv)
        print(f"YUV a RGB: {rgb_result}")

    # Exemple EX_2
    elif args.exercici == 2:
        input_image = img
        output_image = "output.jpg"
        width = 640
        height = 480
        resize_image(input_image, output_image, width, height)

    # Exemple EX_3
    elif args.exercici == 3:
        file_path = img  
        zigzag_bytes = serpentine(file_path)
        print(zigzag_bytes[:10])  # Imprimim els primers 10 bytes llegits en un patró de ziga-zaga com a exemple

    # Exemple EX_4
    elif args.exercici == 4:
        input_image = img  
        output_image = 'output_bw.jpg'  # Definim el nom del fitxer de sortida
        compression_quality = 0  # Nivell de compressió (0 és el més alt)
        convert_to_bw_and_compress(input_image, output_image, compression_quality)

    # Exemple EX_5
    elif args.exercici == 5:
        data = [1, 2, 2, 3, 4, 1, 1, 4, 3, 2]
        encoded_data = run_length_encode(data)
        print(encoded_data)

    # Exemple EX_6
    elif args.exercici == 6:

        dct_processor = DCTProcessor()  # Creem una instància de la classe 'DCTProcessor'
        im = rgb2gray(imread(img))  # Llegim una imatge RGB i la convertim a escala de grisos
        imf = dct_processor.dct2(im)
        im1 = dct_processor.idct2(imf)
        np.allclose(im, im1)  # Comprovem si la imatge reconstruïda és gairebé igual a la imatge original
        plt.gray()  # Mostrem les imatges original i reconstruïda amb matplotlib.pylab
        plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Imatge Original', size=10)
        plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('Imatge Reconstruïda (DCT+IDCT)', size=10)
        plt.show()
    else:
        print("Número d'exercici no vàlid. Si us plau, introduïu un número d'exercici entre 1 i 6.")


if __name__ == "__main__":
    main()
```

Per tal d'executar un exercici:
Exemple: `python3 rgb_yuv.py 1`
Això executarà l'exercici 1 amb els valors indicats en el main i proporcionarà els resultats. 

Canviant el número "1" de la comanda podràs executar els diferents exercicis, introduïnt un número de (1-6).



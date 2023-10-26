# SCAV

Descripció curta o resum del teu projecte.

## Descripció

Aquest repositori conté un script de Python amb diversos exercicis per a processament d'imatges i altres operacions. Els exercicis es descriuran a continuació, juntament amb instruccions sobre com executar-los.

## Exercici 1 - Conversió RGB a YUV

Aquest exercici implica la conversió de valors RGB a YUV utilitzant una matriu de conversió específica. La funció `rgb2yuv` realitza la conversió i la funció `yuv2rgb` fa la conversió inversa.

**Captura de Pantalla (opcional):**

![Exercici 1](imatge_exercici1.png)

**Instruccions per a l'Usuari:**

Per a executar aquest exercici, pots cridar les funcions `rgb2yuv` i `yuv2rgb` amb els valors RGB o YUV desitjats.

```python
rgb = (3, 5, 8)
yuv = rgb2yuv(rgb)
print(f"RGB a YUV: {yuv}")

rgb_result = yuv2rgb(yuv)
print(f"YUV a RGB: {rgb_result}")
```
## Exercici 2 - Redimensionar i Comprimir una Imatge

En aquest exercici, redimensionem una imatge utilitzant la comanda `ffmpeg` per especificar l'amplada i l'altura desitjades. També es pot ajustar la qualitat de la imatge.

![Captura de Pantalla de l'Exercici 2](imatge_exercici2.png)  <!-- Afegir la vostra captura de pantalla aquí si és necessari -->

**Instruccions per a l'Usuari:**

Per a executar aquest exercici, crida la funció `resize_image` amb l'arxiu d'entrada, l'arxiu de sortida, l'amplada i l'altura desitjades.

```python
input_image = 'imatge.jpg'
output_image = 'imatge_redimensionada.jpg'
width = 640
height = 480
resize_image(input_image, output_image, width, height)
```
## Exercici 3 - Patró de Ziga-Zaga

En aquest exercici, llegeixem els bytes d'un arxiu d'entrada i els organitzem en un patró de ziga-zaga.

**Instruccions per a l'Usuari:**

Per a executar aquest exercici, crida la funció `serpentine` amb la ruta de l'arxiu d'entrada. Després, pots processar el resultat com ho desitgis.

```python
file_path = 'arxiu.bin'
zigzag_bytes = serpentine(file_path)
```
## Exercici 4 - Conversió a B/N i Compressió

En aquest exercici, es converteix una imatge a blanc i negre i es pot especificar el nivell de compressió utilitzant ffmpeg.

**Instruccions per a l'Usuari:**

Per a executar aquest exercici, crida la funció `convert_to_bw_and_compress` amb l'arxiu d'entrada, l'arxiu de sortida i el nivell de compressió desitjat.

```python
input_image = 'imatge.jpg'
output_image = 'imatge_bn.jpg'
compression_quality = 0  # Ajusta el nivell de compressió
convert_to_bw_and_compress(input_image, output_image, compression_quality)
```
## Exercici 5 - Codificació d'Execució de Longitud

En aquest exercici, es realitza la codificació de longitud d'execució d'una llista de dades.

**Instruccions per a l'Usuari:**

Per a executar aquest exercici, proporciona una llista de dades i crida la funció `run_length_encode` per a codificar-les.

```python
data = [1, 2, 2, 3, 4, 1, 1, 4, 3, 2]
encoded_data = run_length_encode(data)
```
## Exercici 6 - Transformada de Cosenides Discretes (DCT)

Aquest exercici implica l'ús de la Transformada de Cosenides Discretes (DCT) per a processar imatges. Es mostra com aplicar les funcions DCT i IDCT a una imatge.

**Instruccions per a l'Usuari:**

Per a executar aquest exercici, crea una instància de la classe `DCTProcessor` i utilitza les funcions `dct2` i `idct2` per a processar imatges.

```python
dct_processor = DCTProcessor()
im = rgb2gray(imread('imatge.jpg'))
imf = dct_processor.dct2(im)
im1 = dct_processor.idct2(imf)
```
## Com executar l'script

Per a executar l'script i provar els diversos exercicis, pots utilitzar la funció `main`. Executa l'script mitjançant la línia de comandes i especifica el número d'exercici com a argument.

Exemple: `python script.py 1`

Això executarà l'exercici 1 amb les instruccions i proporcionarà els resultats.

Ara tens tota la informació necessària per a compartir el teu script i els exercicis associats en un repositori de GitHub. Afegeix les captures de pantalla i ajusta les instruccions segons les necessitats del teu projecte.

```vbnet
Recorda substituir els noms d'arxius i les descripcions dels exercicis amb la informació real del teu projecte. També pots afegir enllaços a altres recursos o documentació relacionada amb el teu projecte si és necessari.


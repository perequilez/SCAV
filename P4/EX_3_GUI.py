import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QTabWidget, \
    QMessageBox

# Importem la funció export_video_comparison del script EX_2
from EX_2 import export_video_comparison

# Importem la classe VideoConverter del script final_exercices
from final_exercices import VideoConverter

# Creem una instància de VideoConverter
Vid_Conv = VideoConverter()


# Definim la classe VideoConverterGUI que hereta de QWidget
class VideoConverterGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialitzem la interfície d'usuari
        self.init_ui()

    def init_ui(self):
        # Creem un objecte QTabWidget
        self.tabs = QTabWidget()

        # Creem una pestanya per a la conversió i comparació de vídeos
        self.tab1 = QWidget()
        self.init_tab1()
        self.tabs.addTab(self.tab1, 'Conversió i Comparació de Vídeos')

        # Creem una pestanya per a modificar la resolució
        self.tab2 = QWidget()
        self.init_tab2()
        self.tabs.addTab(self.tab2, 'Modificar Resolució')

        # Creem un disseny vertical i afegim les pestanyes
        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        # Establim el disseny pel widget principal
        self.setLayout(vbox)

    def init_tab1(self):
        # Creem etiquetes i elements d'entrada per a la pestanya 1
        self.input_label_tab1 = QLabel('Input Video:')
        self.input_entry_tab1 = QLineEdit()
        self.input_button_tab1 = QPushButton('Browse')
        self.input_button_tab1.clicked.connect(self.browse_input_tab1)

        self.output_label_tab1 = QLabel('Output Video:')
        self.output_entry_tab1 = QLineEdit()
        self.output_button_tab1 = QPushButton('Browse')
        self.output_button_tab1.clicked.connect(self.browse_output_tab1)

        self.vp8_button_tab1 = QPushButton('Convert to VP8')
        self.vp8_button_tab1.clicked.connect(self.convert_to_vp8_tab1)

        self.vp9_button_tab1 = QPushButton('Convert to VP9')
        self.vp9_button_tab1.clicked.connect(self.convert_to_vp9_tab1)

        self.h265_button_tab1 = QPushButton('Convert to H.265')
        self.h265_button_tab1.clicked.connect(self.convert_to_h265_tab1)

        self.av1_button_tab1 = QPushButton('Convert to AV1')
        self.av1_button_tab1.clicked.connect(self.convert_to_av1_tab1)

        self.compare_label_tab1 = QLabel('Video to Compare:')
        self.compare_entry_tab1 = QLineEdit()
        self.compare_button_tab1 = QPushButton('Browse')
        self.compare_button_tab1.clicked.connect(self.browse_compare_tab1)

        self.compare_videos_button_tab1 = QPushButton('Compare Videos')
        self.compare_videos_button_tab1.clicked.connect(self.compare_videos_tab1)

        # Creem un disseny vertical i afegim els elements
        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label_tab1)
        vbox.addWidget(self.input_entry_tab1)
        vbox.addWidget(self.input_button_tab1)
        vbox.addWidget(self.output_label_tab1)
        vbox.addWidget(self.output_entry_tab1)
        vbox.addWidget(self.output_button_tab1)
        vbox.addWidget(self.vp8_button_tab1)
        vbox.addWidget(self.vp9_button_tab1)
        vbox.addWidget(self.h265_button_tab1)
        vbox.addWidget(self.av1_button_tab1)
        vbox.addWidget(self.compare_label_tab1)
        vbox.addWidget(self.compare_entry_tab1)
        vbox.addWidget(self.compare_button_tab1)
        vbox.addWidget(self.compare_videos_button_tab1)

        # Establim el disseny a la pestanya 1
        self.tab1.setLayout(vbox)

    def init_tab2(self):
        # Creem etiquetes i elements d'entrada per a la pestanya 2
        self.input_label_tab2 = QLabel('Input File:')
        self.input_entry_tab2 = QLineEdit()
        self.input_button_tab2 = QPushButton('Browse')
        self.input_button_tab2.clicked.connect(self.browse_input_tab2)

        self.output_label_tab2 = QLabel('Output File:')
        self.output_entry_tab2 = QLineEdit()
        self.output_button_tab2 = QPushButton('Browse')
        self.output_button_tab2.clicked.connect(self.browse_output_tab2)

        self.width_label_tab2 = QLabel('Width:')
        self.width_entry_tab2 = QLineEdit()

        self.height_label_tab2 = QLabel('Height:')
        self.height_entry_tab2 = QLineEdit()

        # Corregim el nom de l'atribut aquí
        self.modify_resolution_button_tab2 = QPushButton('Modify Resolution')
        self.modify_resolution_button_tab2.clicked.connect(self.modify_resolution_tab2)

        # Creem un disseny vertical i afegim els elements
        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label_tab2)
        vbox.addWidget(self.input_entry_tab2)
        vbox.addWidget(self.input_button_tab2)
        vbox.addWidget(self.output_label_tab2)
        vbox.addWidget(self.output_entry_tab2)
        vbox.addWidget(self.output_button_tab2)
        vbox.addWidget(self.width_label_tab2)
        vbox.addWidget(self.width_entry_tab2)
        vbox.addWidget(self.height_label_tab2)
        vbox.addWidget(self.height_entry_tab2)

        # Corregim el nom de l'atribut aquí
        vbox.addWidget(self.modify_resolution_button_tab2)

        # Establim el disseny a la pestanya 2
        self.tab2.setLayout(vbox)

    def browse_input_tab1(self):
        # Naveguem pel sistema de fitxers per seleccionar el vídeo d'entrada a la pestanya 1
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Input Video', '', 'All files (*.*);;Video files')
        self.input_entry_tab1.setText(file_path)

    def browse_output_tab1(self):
        # Naveguem pel sistema de fitxers per seleccionar la ubicació de sortida del vídeo a la pestanya 1
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Output Video', '', 'Video files')
        self.output_entry_tab1.setText(file_path)

    def browse_input_tab2(self):
        # Naveguem pel sistema de fitxers per seleccionar el fitxer d'entrada a la pestanya 2
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Input Video', '', 'All files (*.*);;Video files')
        self.input_entry_tab2.setText(file_path)

    def browse_output_tab2(self):
        # Naveguem pel sistema de fitxers per seleccionar la ubicació de sortida del fitxer a la pestanya 2
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Output Video', '', 'Video files')
        self.output_entry_tab2.setText(file_path)

    def modify_resolution_tab2(self):
        # Modifiquem la resolució del vídeo a la pestanya 2
        input_video = self.input_entry_tab2.text()
        output_video = self.output_entry_tab2.text()
        width = self.width_entry_tab2.text()
        height = self.height_entry_tab2.text()

        if input_video and output_video and width and height:
            success, message = Vid_Conv.modify_resolution(input_video, output_video, width, height)
            if success:
                QMessageBox.information(self, 'Success', message)
            else:
                QMessageBox.critical(self, 'Error', message)
        else:
            QMessageBox.critical(self, 'Error', 'Please provide input, output, width, and height.')

    def browse_compare_tab1(self):
        # Naveguem pel sistema de fitxers per seleccionar el vídeo de comparació a la pestanya 1
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Video to Compare', '', 'All files (*.*);;Video files')
        self.compare_entry_tab1.setText(file_path)

    def compare_videos_tab1(self):
        # Comparem dos vídeos a la pestanya 1
        input_video = self.input_entry_tab1.text()
        compare_video = self.compare_entry_tab1.text()
        output_file = self.output_entry_tab1.text()

        if input_video and compare_video and output_file:
            export_video_comparison(input_video, compare_video, output_file)
            QMessageBox.information(self, 'Success', 'Video comparison completed successfully.')
        else:
            QMessageBox.critical(self, 'Error', 'Please provide input, video to compare, and output video files.')

    def convert_to_vp8_tab1(self):
        # Convertim el vídeo a VP8 a la pestanya 1
        input_file = self.input_entry_tab1.text()
        output_file = self.output_entry_tab1.text() + "_vp8.webm"

        try:
            command = f"ffmpeg -i {input_file} -c:v libvpx -b:v 1M -c:a libvorbis {output_file}"
            subprocess.call(command, shell=True)
            print(f"Conversion to VP8 successful: {input_file} -> {output_file}")
        except Exception as e:
            print(f"Error during VP8 conversion: {e}")

    def convert_to_vp9_tab1(self):
        # Convertim el vídeo a VP9 a la pestanya 1
        input_file = self.input_entry_tab1.text()
        output_file = self.output_entry_tab1.text() + "_vp9.webm"

        try:
            command = f"ffmpeg -i {input_file} -c:v libvpx-vp9 -b:v 1M -c:a libvorbis {output_file}"
            subprocess.call(command, shell=True)
            print(f"Conversion to VP9 successful: {input_file} -> {output_file}")
        except Exception as e:
            print(f"Error during VP9 conversion: {e}")

    def convert_to_h265_tab1(self):
        # Convertim el vídeo a H.265 a la pestanya 1
        input_file = self.input_entry_tab1.text()
        output_file = self.output_entry_tab1.text() + ".mp4"

        try:
            command = f"ffmpeg -i {input_file} -c:a copy -c:v libx265 {output_file}"
            subprocess.call(command, shell=True)
            print(f"Conversion to H.265 successful: {input_file} -> {output_file}")
        except Exception as e:
            print(f"Error during H.265 conversion: {e}")

    def convert_to_av1_tab1(self):
        # Convertim el vídeo a AV1 a la pestanya 1
        input_file = self.input_entry_tab1.text()
        output_file = self.output_entry_tab1.text() + ".mkv"

        try:
            command = f"ffmpeg -i {input_file} -c:v libaom-av1 -crf 30 {output_file}"
            subprocess.call(command, shell=True)
            print(f"Conversion to AV1 successful: {input_file} -> {output_file}")
        except Exception as e:
            print(f"Error during AV1 conversion: {e}")

    def convert_video_tab1(self, conversion_function):
        # Convertim vídeos a la pestanya 1 amb la funció de conversió proporcionada
        input_file = self.input_entry_tab1.text()
        output_file = self.output_entry_tab1.text()

        if input_file and output_file:
            conversion_function(input_file, output_file)
            QMessageBox.information(self, 'Success', 'Video conversion completed successfully.')
        else:
            QMessageBox.critical(self, 'Error', 'Please provide input and output video files.')


# Punt d'entrada del programa
if __name__ == '__main__':
    # Creem una aplicació PyQt
    app = QApplication(sys.argv)

    # Creem una instància de la classe VideoConverterGUI
    window = VideoConverterGUI()

    # Configurem el títol de la finestra
    window.setWindowTitle('Interfície de Conversió de Vídeos')

    # Mostrem la finestra
    window.show()

    # Executem l'aplicació
    sys.exit(app.exec_())

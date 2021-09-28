# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:16:18 2021

@author: junob
"""
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, sip

import nabitools
import filesort


import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def load_config():
    try:
        with open("Axion.conf", "r", -1, 'utf-8') as f:
            size, colors, path = f.readlines()
    except: 
        return 16, 16, ''
    return int(size), int(colors), path

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Axion.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config.triggered.connect(self.configure_dialog_open)
        self.log.triggered.connect(self.log_dialog_open)
        self.information.triggered.connect(self.information_dialog_open)
        self.path_btn.clicked.connect(lambda: self.showDialog(self.fileline))
        self.path_btn_2.clicked.connect(lambda: self.showDialog(self.fileline_2))
        self.path_btn_3.clicked.connect(lambda: self.showDialog(self.fileline_3))
        self.path_btn_4.clicked.connect(lambda: self.showDialog(self.fileline_4))
        self.path_btn_5.clicked.connect(lambda: self.showDialog(self.fileline_5))
        self.path_btn_6.clicked.connect(lambda: self.showDialog(self.fileline_6))
        self.path_btn_7.clicked.connect(lambda: self.showDialog(self.fileline_7))
        self.path_btn_8.clicked.connect(lambda: self.showDialog(self.fileline_8))
        self.path_btn_9.clicked.connect(lambda: self.showDialog(self.fileline_9))
        self.path_btn_10.clicked.connect(lambda: self.showDialog(self.fileline_10))
        self.start_btn.clicked.connect(self.search_duplicate_images)
        self.files = []
        #self.th = None
        self.progressBar.setValue(0)
        self.log_text = 'Hello!!\n\n'
        self.statusBar.showMessage(' 검사 대기 중...')
    
    def showDialog(self, line):
        size, colors, path = load_config()
        try:
            folder_path = QFileDialog.getExistingDirectory(self, 'Open Folder', path + '/..')
        except:
            folder_path = QFileDialog.getExistingDirectory(self, 'Open Folder', '')
        if not folder_path == '':
            path = folder_path
        with open("Axion.conf", "w", -1, 'utf-8') as f:
            f.write(str(size) + '\n' + str(colors) + '\n' + path)
        line.setText(folder_path)
        
    def search_duplicate_images(self):
        self.start_btn.setEnabled(False)
        self.statusBar.showMessage(' 파일 찾는 중...')
        path = self.fileline.text()
        path_2 = self.fileline_2.text()
        path_3 = self.fileline_3.text()
        path_4 = self.fileline_4.text()
        path_5 = self.fileline_5.text()
        path_6 = self.fileline_6.text()
        path_7 = self.fileline_7.text()
        path_8 = self.fileline_8.text()
        path_9 = self.fileline_9.text()
        path_10 = self.fileline_10.text()
        
        recursive = self.checkBox.isChecked()
        recursive_2 = self.checkBox_2.isChecked()
        recursive_3 = self.checkBox_3.isChecked()
        recursive_4 = self.checkBox_4.isChecked()
        recursive_5 = self.checkBox_5.isChecked()
        recursive_6 = self.checkBox_6.isChecked()
        recursive_7 = self.checkBox_7.isChecked()
        recursive_8 = self.checkBox_8.isChecked()
        recursive_9 = self.checkBox_9.isChecked()
        recursive_10 = self.checkBox_10.isChecked()
        
        self.files = nabitools.all_files_path([path, path_2, path_3, path_4, path_5, path_6, path_7, path_8, path_9, path_10], 
                                              [recursive, recursive_2, recursive_3, recursive_4, recursive_5, recursive_6, recursive_7, recursive_8, recursive_9, recursive_10])
        self.statusBar.showMessage(' ' + str(len(self.files)) + '개의 파일을 검사 중...')
        self.th = Thread(self.files)
        
        self.th.change_value.connect(self.progressbar_set)
        self.th.change_text.connect(self.logging)
        
        # size, colors = load_config()
        # nabi = nabitools.Nabi((size, size), colors)
        # result = nabi.find_duplicate_images(self.files, self.progressbar_set, self.logging)
        self.th.change_result.connect(self.result_)
        self.th.start()
        

    def result_(self, result):
        
        self.start_btn.setEnabled(True)
        duplicate_img_group_num = len(result)
        duplicate_img_num = len([y for x in result for y in x]) - duplicate_img_group_num
        self.statusBar.showMessage(' 검사 완료, ' + str(duplicate_img_group_num) + '개의 중복 이미지 그룹과 ' + 
                                   str(duplicate_img_num) + '개의 중복 이미지 발견')
        self.result_dialog_open(result)
        self.statusBar.showMessage(' 검사 대기 중...')
        # print(result)
        
    def logging(self, msg):
        self.log_text += str(msg) + '\n\n'
        
    def progressbar_set(self, value):
        try:
            self.progressBar.setValue(value*100//len(self.files))
        except:
            pass
        
    def result_dialog_open(self, result):
        dialog = ResultDialog(result)
        dialog.exec_()
        
    def configure_dialog_open(self):
        dialog = ConfigureDialog()
        dialog.exec_()   
        
    def log_dialog_open(self):
        dialog = LogDialog(self.log_text)
        
        def log_dialog_update(msg):
            dialog.logBrowser.append(msg+'\n')
        try:
            self.th.change_text.connect(log_dialog_update)
        except:
            pass
        dialog.exec_()
        
    def information_dialog_open(self):
        dialog = InformationDialog()
        dialog.exec_()
 
    
class Thread(QThread):
    # 사용자 정의 시그널 선언
    change_value = pyqtSignal(int)
    change_text = pyqtSignal(str)
    change_result = pyqtSignal(list)
    
    def __init__(self, files):
        QThread.__init__(self)
        self.files = files

    def run(self):
        size, colors, path = load_config()
        nabi = nabitools.Nabi((size, size), colors)
        result = nabi.find_duplicate_images(self.files, self.change_value.emit, self.change_text.emit)
        self.change_result.emit(result)
        self.change_value.emit(0)

class MLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

    def enterEvent(self, event):
        self.movie().start()

    def leaveEvent(self, event):
        self.movie().stop()
        
result_dialog = uic.loadUiType("Result.ui")[0]
class ResultDialog(QDialog, result_dialog):
    def __init__(self, result):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        self.del_btn.clicked.connect(self.delete)
        self.image_widgets = []
        if result == []:
            lbl = QLabel('겹치는 이미지가 없습니다.')
            lbl.setAlignment(Qt.AlignCenter)
            self.graph_verticalLayout.addWidget(lbl)
        else:
            self.graph_verticalLayout.setAlignment(Qt.AlignTop)
        for image_group in result:
            image_hash = image_group[0]
            image_group = filesort.file_size_sort(image_group[1:])
            lbl_hash = QLabel('이미지 해쉬: ' + image_hash)
            lbl_hash.setAlignment(Qt.AlignCenter)
            lbl_hash.setMinimumHeight(60)
            lbl_hash.setMaximumHeight(60)
            lbl_hash.setStyleSheet('border-bottom: 1px solid lightgray; border-top: 1px solid lightgray;')
            self.graph_verticalLayout.addWidget(lbl_hash)
            for image in image_group:
                #print(image)
                sublayout = QHBoxLayout()
                self.graph_verticalLayout.addLayout(sublayout)
                
                # pixmap = QPixmap(image)
                # pixmap = pixmap.scaledToWidth(256, Qt.SmoothTransformation)
                # lbl_img = QLabel()
                # lbl_img.setPixmap(pixmap)
                # sublayout.addWidget(lbl_img)
                
                movie = QMovie(image)
                width = 256
                height = self.resize_height(image, width)
                movie.setScaledSize(QSize(width, height))
                lbl_img = MLabel()
                lbl_img.setMovie(movie)
                lbl_img.setAlignment(Qt.AlignCenter)
                movie.start()
                movie.stop()
                lbl_img.leaveEvent
                lbl_img.enterEvent
                
                sublayout.addWidget(lbl_img)
                tb = QTextBrowser()
                tb.setMaximumHeight(height)
                tb.setOpenExternalLinks(True)
                tb.append(image)
                tb.append('\n' + filesort.convert_date(os.path.getmtime(image)) +
                          '\n\n' + str(filesort.get_img_size(image)) +
                          '\n\n' + str(filesort.get_dpi(image)) + ' dpi' +
                          '\n\n' + filesort.convert_size(os.path.getsize(image)))
                sublayout.addWidget(tb)
                
                cb = QCheckBox('삭제')
                sublayout.addWidget(cb)
                
                self.image_widgets.append([lbl_img, tb, cb, image])

    # def resize_height(self, img, width):
    #     pixmap = QPixmap(img)
    #     try:
    #         return int(pixmap.height()/pixmap.width()*width)
    #     except:
    #         return 256
          
    def resize_height(self, img, width):
        img_width, img_height = filesort.get_img_size(img)
        try:
            return int(img_height/img_width*width)
        except:
            return width
        
    def delete(self):
        #print('delete')
        for i in range(len(self.image_widgets)):
            try:
                if self.image_widgets[i][2].isChecked():
                    for j in range(3):
                        self.image_widgets[i][j].deleteLater()
                        self.image_widgets[i][j] = None
                    if os.path.isfile(self.image_widgets[i][3]):
                        os.remove(self.image_widgets[i][3])
            except:
                pass

configure_dialog = uic.loadUiType("Configure.ui")[0]
class ConfigureDialog(QDialog, configure_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        size, colors, path = load_config()
        self.sizeSlider.setValue(size)
        self.colorsSlider.setValue(colors)
        self.sizeLabel.setText(str(size))
        self.colorsLabel.setText(str(colors))
        self.sizeSlider.valueChanged.connect(self.save_config)
        self.colorsSlider.valueChanged.connect(self.save_config)
        self.exam_img = 'ax_icon.png'
        
        fig = plt.Figure()
        self.ax = fig.add_subplot(111)
        self.ax.axes.xaxis.set_visible(False)
        self.ax.axes.yaxis.set_visible(False)
        self.canvas = FigureCanvas(fig)
        self.graph_verticalLayout.addWidget(self.canvas)
        
        nabi = nabitools.Nabi((size, size), colors)
        simple_img = nabi.image_simplification(self.exam_img)
        self.ax.imshow(simple_img, interpolation='nearest')
        self.canvas.draw()
        self.hash_text.setText(nabi.image_to_hash(self.exam_img))
        
    def save_config(self):
        size = self.sizeSlider.value()
        colors = self.colorsSlider.value()
        path = load_config()[2]
        with open("Axion.conf", "w", -1, 'utf-8') as f:
            f.write(str(size) + '\n' + str(colors) + '\n' + path)
        nabi = nabitools.Nabi((size, size), colors)
        simple_img = nabi.image_simplification(self.exam_img)
        self.ax.imshow(simple_img, interpolation='nearest')
        self.canvas.draw()
        self.hash_text.setText(nabi.image_to_hash(self.exam_img))
            
        
log_dialog = uic.loadUiType("Log.ui")[0]
class LogDialog(QDialog, log_dialog):
    def __init__(self, msg):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window) # | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        self.logBrowser.setTextColor(QColor(0,255,0))
        self.logBrowser.append(msg)
        
information_dialog = uic.loadUiType("Information.ui")[0]
class InformationDialog(QDialog, information_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
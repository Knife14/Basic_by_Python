"""
title：版本更新提示
writer：山客
date：2022.4.15
content：根据软件自身哈希值，与远端存储的哈希值副本进行比较
tips：
① 目前每次更新发布版都需自己打包后手动生成哈希值
② 哈希值生成可以使用除了md5以外更多的哈希算法
③ 暂不支持自动更新，热更新
"""

from PyQt5.QtNetwork import *
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont

import hashlib

class UpdateReminder(QObject):
    ____manager__: QNetworkAccessManager = None
    
    def __init__(self):
        super().__init__()
        
        self.____manager__ = QNetworkAccessManager(self)
        self.____manager__.finished.connect(self.replyFinished)
        
    def CompareVersion(self):
        request = QNetworkRequest()
        
        request.setUrl(QUrl(
            "https://webattr/filename.yml"
        ))
        request.setHeader(
            QNetworkRequest.UserAgentHeader, "RT-Thread ART"
        )
        
        self.____manager__.get(request)
    
    @pyqtSlot(QNetworkReply)
    def replyFinished(self, reply: QNetworkReply):
        import sys
        with open(sys.argv[0], 'rb') as file:
            data = file.read()
        
        file_md5= hashlib.md5(data).hexdigest()
        
        reply_str = str(reply.readAll())[2: -1]
        
        if file_md5 != reply_str:
            msgBox = QMessageBox()
            msgBox.setFont(QFont("Times", 11))
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Update Reminder")
            msgBox.setText(
                "New version detected. You can go to "
                "<u>https://webattr/</u> to download.")
            msgBox.exec()
   
        
if __name__ == '__main__':
    with open('./filepath/filename.bin', 'rb') as file:
        data = file.read()
    
    file_md5 = hashlib.md5(data).hexdigest()
    
    with open('./filepath/filename.bin', 'w') as file:
        file.write(file_md5)

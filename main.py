from PySide2 import QtWidgets,QtCore,QtGui
import numpy as np
import pythonping,sys,pickle,time,os
InnerPingList=np.array([])
OutPingList=np.array([])
class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 320)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.7)
        self.move(1500,10)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 400, 300))
        self.frame.setStyleSheet(".QFrame{border: 10px solid red ;border-radius: 10px;background-color: white;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ExitButton = QtWidgets.QPushButton(self.frame)
        self.ExitButton.setGeometry(QtCore.QRect(10, 260, 30, 30))
        self.ExitButton.setIcon(QtGui.QIcon("./close.png"))
        self.ExitButton.setText("")
        self.ExitButton.setObjectName("ExitButton")
        self.innerpingtip = QtWidgets.QLabel(self.frame)
        self.innerpingtip.setGeometry(QtCore.QRect(70, 30, 100, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.innerpingtip.setFont(font)
        self.innerpingtip.setObjectName("innerpingtip")
        self.innerping = QtWidgets.QLabel(self.frame)
        self.innerping.setGeometry(QtCore.QRect(30, 70, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.innerping.setFont(font)
        self.innerping.setObjectName("innerping")
        self.outpingtip = QtWidgets.QLabel(self.frame)
        self.outpingtip.setGeometry(QtCore.QRect(70, 150, 100, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.outpingtip.setFont(font)
        self.outpingtip.setObjectName("outpingtip")
        self.outping = QtWidgets.QLabel(self.frame)
        self.outping.setGeometry(QtCore.QRect(30, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.outping.setFont(font)
        self.outping.setObjectName("outping")
        self.ExitButton_2 = QtWidgets.QPushButton(self.frame)
        self.ExitButton_2.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.ExitButton_2.setStyleSheet(".QPushButton{background-image: url(./setting.png);}")
        self.ExitButton_2.setText("")
        self.ExitButton_2.setObjectName("ExitButton_2")
        self.ExitButton_2.setIcon(QtGui.QIcon("./setting.png"))
        self.innerping_2 = QtWidgets.QLabel(self.frame)
        self.innerping_2.setGeometry(QtCore.QRect(250, 70, 111, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.innerping_2.setFont(font)
        self.innerping_2.setObjectName("innerping_2")
        self.outping_2 = QtWidgets.QLabel(self.frame)
        self.outping_2.setGeometry(QtCore.QRect(250, 200, 111, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.outping_2.setFont(font)
        self.outping_2.setObjectName("outping_2")
        self.ExitButton.clicked.connect(lambda _:app.exit())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.innerpingtip.setText(_translate("Form", "内网延迟"))
        self.innerping.setText(_translate("Form", ""))
        self.outpingtip.setText(_translate("Form", "外网延迟"))
        self.outping.setText(_translate("Form", ""))
        self.innerping_2.setText(_translate("Form", "()"))
        self.outping_2.setText(_translate("Form", "()"))
class MyObject(QtCore.QObject):
    global InnerPingList,OutPingList
    def __init__(self):
        super(MyObject,self).__init__()

    def ping(self):
        global InnerPingList,OutPingList
        def pinging():
            global InnerPingList,OutPingList
            try:
                PING=round(pythonping.ping("192.168.1.1",8,1,32)._responses[0].time_elapsed*1000,2)
                ui.innerping.setText(str(PING)+'ms')
                InnerPingList=np.append(InnerPingList,PING)
                if PING<5:
                    ui.innerping_2.setText("(很好)")
                elif PING<10:
                    ui.innerping_2.setText("(好)")
                elif PING<50:
                    ui.innerping_2.setText("(中)")
                elif PING<100:
                    ui.innerping_2.setText("(差)")
                else:
                    ui.innerping_2.setText("(极差)")
                PING=round(pythonping.ping("114.114.114.114",8,1,32)._responses[0].time_elapsed*1000,2)
                ui.outping.setText(str(PING)+'ms')
                OutPingList=np.append(OutPingList,PING)
                if PING<15:
                    ui.outping_2.setText("(很好)")
                elif PING<33:
                    ui.outping_2.setText("(好)")
                elif PING<77:
                    ui.outping_2.setText("(中)")
                elif PING<200:
                    ui.outping_2.setText("(差)")
                else:
                    ui.outping_2.setText("(极差)")
            except:
                InnerPingList=np.append(InnerPingList,8000)
                OutPingList=np.append(OutPingList,8000)
                ui.innerping.setText("--ms")
                ui.innerping_2.setText("(错误!)")
                ui.outping.setText("--ms")
                ui.outping_2.setText("(错误!)")
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(pinging)
        self.timer.start(3000)
app=QtWidgets.QApplication(sys.argv)
ui=MainWindow()
ui.setupUi(ui)
mo=MyObject()
th=QtCore.QThread()
mo.moveToThread(th)
th.started.connect(mo.ping)
ui.show()
th.start()
status=app.exec_()
th.exit()
if not os.path.exists("./logs"):
    os.mkdir("./logs")
with open("./logs/"+str(int(time.time()))+".inner","wb") as f:
    pickle.dump(InnerPingList,f)
with open("./logs/"+str(int(time.time()))+".out","wb") as f:
    pickle.dump(OutPingList,f)
sys.exit(status)

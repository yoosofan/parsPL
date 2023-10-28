from PyQt4 import QtGui, QtCore

class Window(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self._offset = 200
        self._closed = False
        self._maxwidth = self.maximumWidth()
        self.widget = QtGui.QWidget(self)
        self.listbox = QtGui.QListWidget(self.widget)
        self.button = QtGui.QPushButton('Slide', self.widget)
        self.button.clicked.connect(self.handleButton)
        self.editor = QtGui.QTextEdit(self)
        self.editor.setMaximumWidth(self._offset)
        #self.editor.setAlignment(QtCore.Qt.AlignRight)
        vbox = QtGui.QVBoxLayout(self.widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.listbox)
        vbox.addWidget(self.button)
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.widget)
        layout.addWidget(self.editor)
        layout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.animator = QtCore.QParallelAnimationGroup(self)
        for item in (self, self.editor):
            animation = QtCore.QPropertyAnimation(item, 'maximumWidth')
            animation.setDuration(800)
            animation.setEasingCurve(QtCore.QEasingCurve.OutCubic)
            self.animator.addAnimation(animation)
        self.animator.finished.connect(self.handleFinished)

    def handleButton(self):
        for index in range(self.animator.animationCount()):
            animation = self.animator.animationAt(index)
            width = animation.targetObject().width()
            animation.setStartValue(width)
            if self._closed:
                self.editor.show()
                animation.setEndValue(width + self._offset)
            else:
                animation.setEndValue(width - self._offset)
        self._closed = not self._closed
        self.widget.setMinimumSize(self.widget.size())
        self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.animator.start()

    def handleFinished(self):
        if self._closed:
            self.editor.hide()
        self.layout().setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.widget.setMinimumSize(0, 0)
        self.setMaximumWidth(self._maxwidth)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.move(500, 300)
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt4 import QtCore, QtGui
from gui1 import Ui_MainWindow
from os.path import isfile
# pyuic4 gui1.ui > gui1.py

class StartQT4(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.filename = False
    self.watcher = QtCore.QFileSystemWatcher(self)
    # here we connect signals with our slots
    QtCore.QObject.connect(self.ui.OpenFile,QtCore.SIGNAL("clicked()"), self.file_dialog)
    QtCore.QObject.connect(self.ui.Exit,QtCore.SIGNAL("clicked()"), self.ExitFunction)
    QtCore.QObject.connect(self.ui.plainTextEdit,QtCore.SIGNAL("textChanged()"), self.enable_save)
    QtCore.QObject.connect(self.watcher,QtCore.SIGNAL("fileChanged(const QString&)"), self.file_changed)
  def file_dialog(self):
    response = False
    # buttons texts
    SAVE = 'Save'
    DISCARD = 'Discard Changes'
    CANCEL = 'Cancel'
    # if we have changes then ask about them
    if self.ui.button_save.isEnabled():
      message = QtGui.QMessageBox(self)
      message.setText('Changes haven\'t been saved')
      message.setWindowTitle('Notepad')
      message.setIcon(QtGui.QMessageBox.Question)
      message.addButton(SAVE, QtGui.QMessageBox.AcceptRole)
      message.addButton(DISCARD, QtGui.QMessageBox.DestructiveRole)
      message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
      message.setDetailedText('Unsaved Changes in: ' + str(self.filename))
      message.exec_()
      response = message.clickedButton().text()
      # save  file
      if response == SAVE:
        self.file_save()
        self.ui.button_save.setEnabled(False)
      # discard changes
      elif response == DISCARD:
        self.ui.button_save.setEnabled(False)
    # if we didn't canceled show the file dialog
    if response != CANCEL:
      fd = QtGui.QFileDialog(self)
      # remove old file from watcher
      if self.filename:
        self.watcher.removePath(self.filename)
      self.filename = fd.getOpenFileName()
      if isfile(self.filename):
        s = open(self.filename,encoding='utf-8').read()
        self.ui.plainTextEdit.setPlainText(s)
        self.ui.button_save.setEnabled(False)
        # add file to watcher
        self.watcher.addPath(self.filename)
  def ExitFunction(self):
    exit()
  def enable_save(self):
    self.ui.button_save.setEnabled(True)
    
  def file_changed(self, path):
    response = False
    # buttons texts
    SAVE = 'Save As'
    RELOAD = 'Reload File'
    CANCEL = 'Cancel'
    message = QtGui.QMessageBox(self)
    message.setText('Open file have been changed !')
    message.setWindowTitle('Notepad')
    message.setIcon(QtGui.QMessageBox.Warning)
    message.addButton(SAVE, QtGui.QMessageBox.AcceptRole)
    message.addButton(RELOAD, QtGui.QMessageBox.DestructiveRole)
    message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
    message.setDetailedText('The file "' + str(path) + '" have been changed or removed by other application. What do you want to do ?')
    message.exec_()
    response = message.clickedButton().text()
    # save current file under a new or old name
    if response == SAVE:
      fd = QtGui.QFileDialog(self)
      newfile = fd.getSaveFileName()
      if newfile:
        s = codecs.open(newfile,'w','utf-8')
        s.write(unicode(self.ui.editor_window.toPlainText()))
        s.close()
        self.ui.button_save.setEnabled(False)
        # new file, remove old and add the new one to the watcher
        if self.filename and str(newfile) != str(self.filename):
          self.watcher.removePath(self.filename)
          self.watcher.addPath(newfile)
          self.filename = newfile
    # reload the text in the editor
    elif response == RELOAD:
      s = codecs.open(self.filename,'r','utf-8').read()
      self.ui.editor_window.setPlainText(s)
      self.ui.button_save.setEnabled(False)
    
  def file_save(self):
    # save changes to existing file
    if self.filename and isfile(self.filename):
      # don't react on our changes
      self.watcher.removePath(self.filename)
      s = codecs.open(self.filename,'w','utf-8')
      s.write(unicode(self.ui.editor_window.toPlainText()))
      s.close()
      self.ui.button_save.setEnabled(False)
      self.watcher.addPath(self.filename)
    # save a new file
    else:
      fd = QtGui.QFileDialog(self)
      newfile = fd.getSaveFileName()
      if newfile:
        s = codecs.open(newfile,'w','utf-8')
        s.write(unicode(self.ui.editor_window.toPlainText()))
        s.close()
        self.ui.button_save.setEnabled(False)

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = StartQT4()
  myapp.show()
  sys.exit(app.exec_())

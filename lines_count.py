
import sys
from PyQt5.QtWidgets import QFileDialog ,QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from functools import reduce

class counting_lines(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Counter'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.countL()
        self.show()
    
    def countL(self):
        get_dirs, _ = QFileDialog.getOpenFileNames(self, 'Open files','')
        nlintot = 0
        nesimofile = []
                
        for ndirs in get_dirs:
            with open(ndirs, 'r') as fdir:
                get_lines = fdir.read()
        
            for lines in get_lines.splitlines():
                a = lines.strip()
                if a != '':
                    nlintot += 1
          
            nesimofile.append(nlintot)
            nlintot = 0
        #print(nesimofile)
        somar = lambda a,b: a+ b       
        
        cnt2 = 1
        lstnames = []
        for name in get_dirs:
            lst = [kkk for kkk in name.split('/')]
            lstnames.append(lst[-cnt2])
        #print(lstnames)
        
        for item in range(0,len(lstnames)):
            print('{} = {}'.format(lstnames[item], nesimofile[item]))
        print('Total lines = {}'.format(reduce(somar, nesimofile)))    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    counterCalss = counting_lines()
    counterCalss.show()
    sys.exit()

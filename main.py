import calendar
from datetime import datetime
from PyQt5.QtWidgets import *

import sys

now = datetime.now()

days = calendar.monthrange(now.year,now.month)[1]



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Begin app')
window.setGeometry(100,100,280,80)
window.move(60,15)

grid = QGridLayout()
counter = 0
for i in range(0,5):
    for j in range(0, 7):
        counter += 1
        if(counter <= days):
            grid.addWidget(QPushButton(str(counter)), i, j + 1)
window.setLayout(grid)



window.show()
sys.exit(app.exec_())

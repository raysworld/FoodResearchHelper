# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:58:49 2018

@author: raysw
"""

import sys, os
#from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow
from ui_test import Ui_MainWindow


class mywindow(QMainWindow, Ui_MainWindow):
    flag_create_state = 0 # 0 - normal state | 1 - editable state    
    
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        
        self.BasicInit()
        
        
    def BasicInit(self):
        cur_path = os.path.dirname("./")
        dat_path = '%s/data' % cur_path
        
        isExists=os.path.exists(dat_path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(dat_path) 
            self.le_query_name.setText("目录创建成功")
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            self.le_query_name.setText("目录已存在")
            print(os.listdir(dat_path))
            for i in os.listdir(dat_path):
#                print(i)
                self.cb_leader_name.addItem(i)
                sub_path = "%s%s%s" % (dat_path, '/', i)
                for j in os.listdir(sub_path):
#                    print(j)
                    self.cb_researcher_name.addItem(j)            
            
            return False        
        
    def func_create_researcher_data(self):
        if self.flag_create_state == 0:        
            print("请在组长、调查员下拉框内分别填入要增加的组长、调查员姓名，然后再次点击按钮")
            self.cb_leader_name.setEditable(True)
            self.cb_researcher_name.setEditable(True)
            self.pb_create_data.setText("确认创建数据")
            self.flag_create_state = 1
        else:            
            new_leader_name = self.cb_leader_name.currentText()
            new_researcher_name = self.cb_researcher_name.currentText()

            print(new_leader_name)
            print(new_researcher_name)

            if new_leader_name == "" or new_researcher_name == "":
                print("组长、调查员名字不可为空")
                return
            else:
                cur_path = os.path.dirname("./")
                new_path = "%s%s%s%s%s" % (cur_path, '/data/', new_leader_name, '/', new_researcher_name)
                print(new_path)
                isExists=os.path.exists(new_path)
                if not isExists:
                    os.makedirs(new_path) 
                    print("%s%s" % (new_path,"目录创建成功"))
                self.cb_leader_name.addItem(new_leader_name)

            self.cb_leader_name.setEditable(False)
            self.cb_researcher_name.setEditable(False)
            self.pb_create_data.setText("创建调查员数据")
            self.flag_create_state = 0
        
    def func_load_researcher_data(self):
        self.le_query_name.setText("func_load_researcher_data")
        
    def func_add_to_B0(self):
        self.le_query_name.setText("func_add_to_B0")
        
    def func_save_B0(self):
        self.le_query_name.setText("func_save_B0")

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
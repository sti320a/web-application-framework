import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import dao

dao.create()
dao.insert()
dao.selectAll()
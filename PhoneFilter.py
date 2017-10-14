from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import xlrd
import xlwt
# import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter


# 打开网页
browser = webdriver.Chrome('/home/tom/developkit/chromedriver')
browser.get('http://www.1234i.com/p.php')

# 读取excel文件，获取手机号码
data = xlrd.open_workbook('phone.xls')
# 打开第一张表
table = data.sheets()[0]
# 获取表的行数
nrows = table.nrows
# 循环逐行打印
for i in range(nrows):
    # 获取输入手机号码的位置
    text = browser.find_element_by_xpath("/html/body/center/center/form/textarea")
    text.send_keys(table.col_values(0)[i+1]+ "\n")
    if nrows == i + 2 or (i+1) % 100 == 0 :
        button = browser.find_element_by_xpath("/html/body/center/center/form/input")
        button.click()
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('phone')
        for j in range(100) :
            # 获取手机号码元素，归属地元素并进行异常处理
            try:
                phone = browser.find_element_by_xpath("/html/body/center/p/u"+ "[" + str(j + 1) + "]")
            except NoSuchElementException as msg:
                phone = browser.find_element_by_xpath("/html/body/center/p/u" + "[" + str(1) + "]")

            try:
                address = browser.find_element_by_xpath("/html/body/center/p/font"+ "[" + str(j + 1) + "]")
            except NoSuchElementException as msg:
                address = browser.find_element_by_xpath("/html/body/center/p/font" + "[" + str(1) + "]")

            #　筛选广州的号码，并存入ｅｘｃｅｌ文件
            if(address.text.find("广州") != -1):
                print( phone.text, ' ' ,address.text);
                # row0 = [u'手机号码', u'归属地']
                worksheet.write(j, 0, phone.text)
                worksheet.write(j, 1, address.text)
                workbook.save("/home/tom/source/phone/phone" + str(i) + ".xls")
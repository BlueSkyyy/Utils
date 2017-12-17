#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import xlrd
import xlwt
import pymysql
# from openpyxl.workbook import Workbook
# from openpyxl.writer.excel import ExcelWriter

# 打开网页
browser = webdriver.Chrome('E:\chromedriver_win32\chromedriver.exe')
browser.get('http://www.1234i.com/p.php')

# 创建数据库连接
conn = pymysql.connect(
        host='192.168.223.10',
        port=3306,
        user='root',
        passwd='TomLee4!',
        db='big_data',
        charset='utf8'
        )
sql = "INSERT INTO phone_detail  VALUES (NULL , '%s', '%s', '%s')"

# 读取excel文件，获取手机号码
data = xlrd.open_workbook('E:\phone\phone1.xls')
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

            # 测试数据库连接
            cur = conn.cursor()
            data = (phone.text, address.text, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            cur.execute(sql % data)
            cur.close()
            conn.commit()

            #　筛选广州的号码，并存入ｅｘｃｅｌ文件
            # if(address.text.find("广州") != -1):
            #     print( phone.text, ' ' ,address.text);
            #     # row0 = [u'手机号码', u'归属地']
            #     worksheet.write(j, 0, phone.text)
            #     worksheet.write(j, 1, address.text)
            #     workbook.save("E:\phone\phone" + str(i) + ".xls")

# 关闭数据库连接
conn.close()
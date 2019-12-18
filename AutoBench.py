import io
import os
import sys
import csv
import requests
from time import sleep
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import socket
import platform

def send_email():
    ip = socket.gethostbyname(socket.getfqdn())
    _os = platform.platform()
    _os_processor = platform.processor()
    msg = MIMEText("IP: "+ip+ "\n운영체제: " + _os + "\n프로세서: " + _os_processor + "\n-------------------\n원본사이트 구조 변경에 따른 에러 예상\n개발자는 확인바랍니다.\n\nhttps://www.cpubenchmark.net/\nhttps://www.videocardbenchmark.net/")
    msg['Subject'] = "Auto Bench Error Email"
    msg['From'] = "email@google.com"
    msg['To'] = "email@google.com"
    
    try:
        with smtplib.SMTP_SSL("smtp.google.com") as smtp:
            smtp.login('email', 'pw')
            smtp.send_message(msg)
            smtp.quit()
    except:
        print("\n")

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

_format = 0
# _format 0 : .csv
# _format 1 : .xlsx
# _format 2 : .xls

c_rank = 1
g_rank = 1

# 진행율 출력함수
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, length=100, fill='#'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

# 사용법 출력 함수
def help_print():
    print("\nUsage: AutoBench [--help] [--version] <csv|xlsx|xls> <command> [<args>]")
    print("         <csv|xlsx|xls>\tExport to csv, xlsx or xls files.(default .csv)")
    print("         blank(cpu&gpu)\tExtract both CPU and GPU Data")
    print("         cpu\t\t\tExtract Only CPU Data")
    print("         gpu\t\t\tExtract Only GPU Data")

# 임시 파일 제거 함수
def file_delete(find):
    if find == "cpu":
        os.remove("tmp/1_cpu.csv")
        os.remove("tmp/2_cpu.csv")
        os.remove("tmp/3_cpu.csv")
        os.remove("tmp/4_cpu.csv")
    else:
        os.remove("tmp/1_gpu.csv")
        os.remove("tmp/2_gpu.csv")
        os.remove("tmp/3_gpu.csv")
        os.remove("tmp/4_gpu.csv")

# 파일 확장자 선택 함수
def convert_extention(find):
    filename = ''+find+'.xlsx'
    _filename = ''+find+'.csv'
    
    xlsx = openpyxl.load_workbook(filename)
    csv = open(_filename, "w+")
    for sheet_name in xlsx:
        sheet = sheet_name
        data = sheet.rows
        for row in data:
            l = list(row)
            for i in range(len(l)):
                if i == len(l) - 1:
                    csv.write(str(l[i].value))
                    csv.write('\n')
                else:
                    csv.write(str(l[i].value) + ',')
    csv.close()
    os.remove(filename)

# xlsx 파일 변환기
def convert_excel(find):
    global _format
    wb = Workbook()
    ws1 = wb.active
    ws2 = wb.create_sheet()
    ws3 = wb.create_sheet()
    ws4 = wb.create_sheet()
    
    if find == "cpu":
        ws1.title = '최상위 CPU'
        ws2.title = '중상위 CPU'
        ws3.title = '중하위 CPU'
        ws4.title = '하위 CPU'
    else:
        ws1.title = '최상위 GPU'
        ws2.title = '중상위 GPU'
        ws3.title = '중하위 GPU'
        ws4.title = '하위 GPU'
    
    if _format == 0:
        savefile = "" + find + ".xlsx"
    elif _format == 1:
        savefile = "" + find + ".xlsx"
    elif _format == 2:
        savefile = "" + find + ".xls"

    CSV_SEPARATOR = ","
    
    if find == "cpu":
        with open("tmp/1_cpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws1.cell(r+1,c+1,val)

        with open("tmp/2_cpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws2.cell(r+1,c+1,val)

        with open("tmp/3_cpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws3.cell(r+1,c+1,val)

        with open("tmp/4_cpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws4.cell(r+1,c+1,val)
    else:
        with open("tmp/1_gpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws1.cell(r+1,c+1,val)

        with open("tmp/2_gpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws2.cell(r+1,c+1,val)

        with open("tmp/3_gpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws3.cell(r+1,c+1,val)

        with open("tmp/4_gpu.csv") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        ws4.cell(r+1,c+1,val)
    wb.save(savefile)
    
    if _format == 0:
        convert_extention(find)

# CPU Crawling
def extract_cpu():
    items = list(range(0,100))
    l = len(items)
    printProgress(0, 1, prefix = 'Progress:', suffix = 'CPU Data Extract Ready', length = 50)
    res = requests.get('https://www.cpubenchmark.net/high_end_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/1_cpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('1_cpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '1)Progress:', suffix = 'CPU Data Extracting', length = 50)
    res = requests.get('https://www.cpubenchmark.net/mid_range_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/2_cpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('2_cpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '2)Progress:', suffix = 'CPU Data Extracting', length = 50)
    res = requests.get('https://www.cpubenchmark.net/midlow_range_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/3_cpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('3_cpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '3)Progress:', suffix = 'CPU Data Extracting', length = 50)
    res = requests.get('https://www.cpubenchmark.net/low_end_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/4_cpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('4_cpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '4)Progress:', suffix = 'CPU Data Extracting', length = 50)
    print('CPU Data Extract Complete!!!')
    convert_excel("cpu")
    file_delete("cpu")

# GPU Crawling
def extract_gpu():
    items = list(range(0,100))
    l = len(items)
    printProgress(0, 1, prefix = 'Progress:', suffix = 'GPU Data Extract Ready', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/high_end_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/1_gpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('1_gpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '1)Progress:', suffix = 'GPU Data Extracting', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/mid_range_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/2_gpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('2_gpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '2)Progress:', suffix = 'GPU Data Extracting', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/midlow_range_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/3_gpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('3_gpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '3)Progress:', suffix = 'GPU Data Extracting', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/low_end_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    try:
        data = soup.find("ul",{"class": "chartlist"}).get_text()
    except:
        send_email()
        print("\n죄송합니다. 원본사이트에 접근 할 수 없습니다.\n확인 후 다음 업데이트에 적용하겠습니다.")
        return
    f = open("tmp/4_gpu.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('4_gpu')
    for i, item in enumerate(items):
        sleep(0.001)
        printProgress(i+1, l, prefix = '4)Progress:', suffix = 'GPU Data Extracting', length = 50)
    print('GPU Data Extract Complete!!!')
    
    convert_excel("gpu")
    file_delete("gpu")

def extract_all():
    extract_cpu()
    extract_gpu()

# 인자 처리기
def input_command(args):
    global _format
    
    if len(args) > 2:
        help_print()
        return
    
    for i in args:
        if i == "--help":
            help_print()
            return
        elif i == "--version":
            print("0.2.1")
            return
        elif i == "csv":
            if args[i.find("-f") + 1] == "csv":
                _format = 0
        elif i == "xlsx":
            if args[i.find("-f") + 1] == "xlsx":
                _format = 1
        elif i == "xls":
            if args[i.find("-f") + 1] == "xls":
                _format = 2

        if i == "cpu":
            extract_cpu()
            return
        elif i == "gpu":
            extract_gpu()
            return
        
        if len(args) == 1:
            if args[0] == "csv":
                _format = 0
                extract_cpu()
                extract_gpu()
            elif args[0] == "xlsx":
                _format = 1
                extract_cpu()
                extract_gpu()
            elif args[0] == "xls":
                _format = 2
                extract_cpu()
                extract_gpu()

# Make CPU Data
def make_csv_new(name):
    str = []
    tmp = []
    test = ""
    global c_rank
    
    f = open("tmp/"+name+".csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines[5:-2]:
        str.append(line)
    f.close()

    for i in str:
        i = i.replace(",","").strip()
        if "NA" in i:
            i = i[:i.find("NA")]
            if i[i.find('%') - 2] != '(':#두자리 수
                str_rank = repr(c_rank)
                tmp.append(str_rank + "," + i[:i.index('%') - 3] + "," + i[i.index('%') + 2:])
                c_rank+=1
            elif i[i.find('%') - 2] == '(':#한자리 수
                str_rank = repr(c_rank)
                tmp.append(str_rank + "," + i[:i.index('%') - 2] + "," + i[i.index('%') + 2:])
                c_rank+=1
        elif "$" in i:
            i = i[:i.find('$')]
            if i[i.find('%') - 2] != '(':#두자리 수
                str_rank = repr(c_rank)
                tmp.append(str_rank + "," + i[:i.index('%') - 3] + "," + i[i.index('%') + 2:])
                c_rank+=1
            elif i[i.find('%') - 2] == '(':#한자리 수
                str_rank = repr(c_rank)
                tmp.append(str_rank + "," + i[:i.index('%') - 2] + "," + i[i.index('%') + 2:])
                c_rank+=1
                

    f = open("tmp/"+name+".csv", 'w+', encoding='UTF8')
    for i in tmp:
        f.write(i)
        f.write("\n")

    f.close()

# Make GPU Data
def make_csv_new_g(name):
    str = []
    tmp = []
    count = 1
    global g_rank
    
    f = open("tmp/"+name+".csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines[:]:
        str.append(line)
    f.close()
    
    for i in str:
        if len(i) > 1:
            i = i.replace(",","").strip()
            if count%3 == 1:
                str_rank = repr(g_rank)
                tmp.append(str_rank + "," + i)
                g_rank+=1
                count+=1
            elif count%3 == 2:
                tmp.append(i[i.find(')') + 2:])
                count+=1
            elif count%3 == 0:
                count+=1

    count = 1

    f = open("tmp/"+name+".csv", 'w+', encoding='UTF8')
    for i in tmp:
        if count%2 == 0:
            f.write(i)
            f.write("\n")
            count+=1
        else:
            f.write(i + ",")
            count+=1
    f.close()       

# 시작 지점
if __name__ == "__main__":
    if len(sys.argv) == 1:
        if not os.path.exists("tmp"):
            os.mkdir("tmp")
        extract_all()
        os.rmdir("tmp")
    else:
        if not os.path.exists("tmp"):
            os.mkdir("tmp")
        input_command(sys.argv[1:])
        os.rmdir("tmp")

import io
import sys
import requests
from time import sleep
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, length=100, fill='#'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

def help_print():
    print("\nUsage: AutoBench [-h] [-v]")
    print("         [all]<Print All Info>")
    print("         [high_end_cpus]<Print CPU Info for 1st>")
    print("         [mid_range_cpus]<Print CPU Info for 2st>")
    print("         [midlow_range_cpus]<Print CPU Info for 3st>")
    print("         [low_end_cpus]<Print CPU Info for 4st>")
    print("         [high_end_gpus]<Print GPU Info for 1st>")
    print("         [mid_range_gpus]<Print GPU Info for 2st>")
    print("         [midlow_range_gpus]<Print GPU Info for 3st>")
    print("         [low_end_gpus]<Print GPU Info for 4st>")

def input_url(url):
    if '-h' == url:
        help_print()
    elif '-v' == url:
        print("1.0.0")
    elif 'all' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.cpubenchmark.net/high_end_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("high_end_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('high_end_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '1)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.cpubenchmark.net/mid_range_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("mid_range_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('mid_range_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '2)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.cpubenchmark.net/midlow_range_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("midlow_range_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('midlow_range_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '3)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.cpubenchmark.net/low_end_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("low_end_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('low_end_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '4)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/high_end_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("high_end_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('high_end_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '5)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/mid_range_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("mid_range_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('mid_range_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '6)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/midlow_range_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("midlow_range_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('midlow_range_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '7)Progress:', suffix = 'Running', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/low_end_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("low_end_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('low_end_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = '8)Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'high_end_cpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.cpubenchmark.net/high_end_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("high_end_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('high_end_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'mid_range_cpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.cpubenchmark.net/mid_range_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("mid_range_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('mid_range_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'midlow_range_cpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.cpubenchmark.net/midlow_range_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("midlow_range_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('midlow_range_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'low_end_cpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.cpubenchmark.net/low_end_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("low_end_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_c('low_end_cpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'high_end_gpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/high_end_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("high_end_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('high_end_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'mid_range_gpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/mid_range_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("mid_range_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('mid_range_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'midlow_range_gpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/midlow_range_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("midlow_range_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('midlow_range_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')
    elif 'low_end_gpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.videocardbenchmark.net/low_end_gpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("table",{"class": "chart"}).get_text()
        f = open("low_end_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('low_end_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')

def make_csv(name):
    str = []
    tmp = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    tmp5 = []

    f = open(name+".csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines[5:-2]:
        str.append(line)
    f.close()

    for i in str:
        if "," in i:
            tmp.append(i.replace(',',''))
        else:
            tmp.append(i)
    for i in tmp:
        if "NA" in i:
            tmp2.append('')
        else:
            tmp2.append(i)
    for i in tmp2:
        if "$" in i:
            tmp3.append('')
        else:
            tmp3.append(i)
    for i in tmp3:
        if "   " in i:
            tmp4.append(i.replace('   ', ', '))
        else:
            tmp4.append(i)
    for i in tmp4:
        if "  " in i:
            tmp5.append(i.replace('  ', ''))
        else:
            tmp5.append(i)

    f = open(name+".csv", 'w+', encoding='UTF8')
    for i in tmp4:
        f.write(i)

    f.close()

def make_csv_c(name):
    str = []
    tmp = []
    tmp2 = []
    tmp3 = []
    tmp4 = []

    f = open(name+".csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines[5:-2]:
        str.append(line)
    f.close()

    for i in str:
        if "," in i:
            tmp.append(i.replace(',',''))
        else:
            tmp.append(i)
    for i in tmp:
        if "       " in i:
            tmp2.append(i.replace('       ', ', '))
        else:
            tmp2.append(i)
    for i in tmp2:
        if "    " in i:
            tmp3.append(i.replace('    ', ', '))
        else:
            tmp3.append(i)
    for i in tmp3:
        if "  " in i:
            tmp4.append(i.replace('  ', ''))
        else:
            tmp4.append(i)
    f = open(name+".csv", 'w+', encoding='UTF8')
    for i in tmp4:
        f.write(i)
    f.close()

if len(sys.argv) == 1:
    help_print()
else:
    input_url(sys.argv[1])

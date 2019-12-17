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
    print("         [high_end_cpus]<Print the 1st CPU Info>")
    print("         [mid_range_cpus]<Print the 2st CPU Info>")
    print("         [midlow_range_cpus]<Print the 3st CPU Info>")
    print("         [low_end_cpus]<Print the 4st CPU Info>")
    print("         [high_end_gpus]<Print the 1st GPU Info>")
    print("         [mid_range_gpus]<Print the 2st GPU Info>")
    print("         [midlow_range_gpus]<Print the 3st GPU Info>")
    print("         [low_end_gpus]<Print the 4st GPU Info>")

def all_print():
    items = list(range(0,100))
    l = len(items)
    printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
    res = requests.get('https://www.cpubenchmark.net/high_end_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("high_end_cpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('high_end_cpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '1)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.cpubenchmark.net/mid_range_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("mid_range_cpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('mid_range_cpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '2)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.cpubenchmark.net/midlow_range_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("midlow_range_cpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('midlow_range_cpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '3)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.cpubenchmark.net/low_end_cpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("low_end_cpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new('low_end_cpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '4)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/high_end_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("high_end_gpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('high_end_gpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '5)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/mid_range_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("mid_range_gpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('mid_range_gpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '6)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/midlow_range_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("midlow_range_gpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('midlow_range_gpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '7)Progress:', suffix = 'Running', length = 50)
    res = requests.get('https://www.videocardbenchmark.net/low_end_gpus.html')
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find("ul",{"class": "chartlist"}).get_text()
    f = open("low_end_gpus.csv", 'w+', encoding='UTF8')
    f.write(data)
    f.close()
    make_csv_new_g('low_end_gpus')
    for i, item in enumerate(items):
        sleep(0.01)
        printProgress(i+1, l, prefix = '8)Progress:', suffix = 'Running', length = 50)
    print('Complete!!!')
def input_url(url):
    if '-h' == url:
        help_print()
    elif '-v' == url:
        print("0.2.0")
    elif 'all' == url:
        all_print()
    elif 'high_end_cpus' == url:
        items = list(range(0,100))
        l = len(items)
        printProgress(0, 1, prefix = 'Progress:', suffix = 'Wait...', length = 50)
        res = requests.get('https://www.cpubenchmark.net/high_end_cpus.html')
        soup = BeautifulSoup(res.content, 'lxml')
        data = soup.find("ul",{"class": "chartlist"}).get_text()
        f = open("high_end_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_new('high_end_cpus')
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
        f = open("mid_range_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_new('mid_range_cpus')
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
        f = open("midlow_range_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_new('midlow_range_cpus')
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
        f = open("low_end_cpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv_new('low_end_cpus')
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
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
        data = soup.find("ul",{"class": "chartlist"}).get_text()
        f = open("low_end_gpus.csv", 'w+', encoding='UTF8')
        f.write(data)
        f.close()
        make_csv('low_end_gpus')
        for i, item in enumerate(items):
            sleep(0.01)
            printProgress(i+1, l, prefix = 'Progress:', suffix = 'Running', length = 50)
        print('Complete!!!')

def make_csv_new(name):
    str = []
    tmp = []
    test = ""
    
    f = open(name+".csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines[5:-2]:
        str.append(line)
    f.close()

    for i in str:
        i = i.replace(",","").strip()
        if "NA" in i:
            i = i[:i.find("NA")]
            if i[i.find('%') - 2] != '(':#두자리 수
                tmp.append(i[:i.index('%') - 3] + "," + i[i.index('%') + 2:])
            elif i[i.find('%') - 2] == '(':#한자리 수
                tmp.append(i[:i.index('%') - 2] + "," + i[i.index('%') + 2:])
        elif "$" in i:
            i = i[:i.find('$')]
            if i[i.find('%') - 2] != '(':#두자리 수
                tmp.append(i[:i.index('%') - 3] + "," + i[i.index('%') + 2:])
            elif i[i.find('%') - 2] == '(':#한자리 수
                tmp.append(i[:i.index('%') - 2] + "," + i[i.index('%') + 2:])
                

    f = open(name+".csv", 'w+', encoding='UTF8')
    for i in tmp:
        f.write(i)
        f.write("\n")

    f.close()
     
def make_csv_new_g(name):
    str = []
    tmp = []
    count = 1
    
    f = open(name+".csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines[:]:
        str.append(line)
    f.close()
    
    for i in str:
        if len(i) > 1:
            i = i.replace(",","").strip()
            if count%3 == 1:
                tmp.append(i)
                count+=1
            elif count%3 == 2:
                tmp.append(i[i.find(')') + 2:])
                count+=1
            elif count%3 == 0:
                count+=1

    count = 1

    f = open(name+".csv", 'w+', encoding='UTF8')
    for i in tmp:
        if count%2 == 0:
            f.write(i)
            f.write("\n")
            count+=1
        else:
            f.write(i + ",")
            count+=1
    f.close()       

if len(sys.argv) == 1:
    all_print()
else:
    input_url(sys.argv[1])

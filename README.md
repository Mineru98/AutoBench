# AutoBenchMark

**Version 1.1.1**<br>
이 프로그램은 벤치 마크 사이트로부터 최신 CPU, GPU,Drive 와 RAM 성능 점수와 순위를 추출 프로그램입니다.<br>
csv, xlsx, xls 확장자로 결과를 보여줍니다.<br>
CPU 정보는 모델 이름, 점수로 작성됩니다.<br>
GPU 정보는 모델 이름, 점수로 작성됩니다.<br>
RAM 정보는 모델 이름, 점수로 작성됩니다.<br>
RAM 정보는 모델 이름, 점수로 작성됩니다.<br>

This program is a program that extracts the latest CPU, GPU, Drive and RAM performance scores and rankings from benchmark sites.<br>
The Output Data is saved as a csv, xlsx and xls file.<br>
CPU information is written by model name and score.<br>
GPU information is written by model name and score.<br>
Drive information is written by model name and score.<br>
RAM information is written by model name and score.<br>

## 다운로드(Download)
|  | ![Windows](https://icongr.am/devicon/windows8-original.svg) Windows | ![Linux](https://icongr.am/devicon/linux-original.svg) Linux |
|-|-|-|
| x64 | [![Download AutoBench](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/autobench/files/v1.1.1/Windows%28x64%29/AutoBench.v1.1.1_win_x64/download) | [![Download AutoBench](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/autobench/files/v1.1.1/Linux%28x64%29/AutoBench.v1.1.1_linux_x64/download) |
| x86 | [![Download AutoBench](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/autobench/files/v1.1.1/Windows%28x32%29/AutoBench.v1.1.1_win_x64/download) | X |



## 사용법(Usage)
```
usage: AutoBench [-h] [-v] [-f F [F ...]] [-o O [O ...]]

AutoBench 사용설명서

optional arguments:
  -h, --help    show this help message and exit
  -v            버전 확인
  -f F [F ...]  포맷 형식 지정. (단, 하나만 선택 가능. 기본 xlsx)
  -o O [O ...]  추출물 지정(기본 전부)
```

```
usage: AutoBench [-h] [-v] [-f F [F ...]] [-o O [O ...]]

AutoBench Usage

optional arguments:
  -h, --help    show this help message and exit
  -v            check version
  -f F [F ...]  select file format. (only one. default xlsx)
  -o O [O ...]  select export(default all of)
```

## 사용 예시(for example)
```
1) AutoBench.exe
2) AutoBench.exe -f csv
3) AutoBench.exe -f xls -o cpu
4) AutoBench.exe -o drive cpu ram
```

## 빌드 방법(How To Build)
[PyInstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html)
```
pip install pytinstaller
pyinstaller -D -F -n AutoBench.v1.1.1_ -i icon.ico AutoBench.py
```

## Git Release
```
git tag -a vz.x.y -m ""
git push origin vz.x.y
```

# 원본 사이트(Source Site)

[CPU Benchmark Site](https://www.cpubenchmark.net/)<br>
[GPU Benchmark Site](https://www.videocardbenchmark.net/)<br>
[Drive Benchmark Site](https://www.harddrivebenchmark.net/)<br>
[RAM Benchmark Site](https://www.memorybenchmark.net/)
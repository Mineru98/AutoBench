# AutoBenchMark

Version 0.2.0<br>
이 프로그램은 벤치 마크 사이트로부터 최신 CPU와 GPU 성능 점수와 순위를 추출 프로그램입니다.<br>
csv 확장자로 결과를 보여줍니다.<br>
CPU 정보는 모델 이름, 점수로 작성됩니다.<br>
GPU 정보는 모델 이름, 점수로 작성됩니다.<br>

Version 0.2.0<br>
This program is a program that extracts the latest CPU and GPU performance scores and rankings from benchmark sites.<br>
The Output Data is saved as a csv file.<br>
CPU information is written by model name and score.<br>
GPU information is written by model name and score.<br>

## 사용법(Usage)
```
사용법: AutoBench.exe [-h] [-v]
         [all]<CPU&GPU의 모든 범주에 해당하는 파일 추출>
         [high_end_cpus]<최상위 CPU 범주에 해당하는 파일 추출>
         [mid_range_cpus]<중상위 CPU 범주에 해당하는 파일 추출>
         [midlow_range_cpus]<중하위 CPU 범주에 해당하는 파일 추출>
         [low_end_cpus]<하위 CPU 범주에 해당하는 파일 추출>
         [high_end_gpus]<최상위 GPU 범주에 해당하는 파일 추출>
         [mid_range_gpus]<중상위 GPU 범주에 해당하는 파일 추출>
         [midlow_range_gpus]<중하위 GPU 범주에 해당하는 파일 추출>
         [low_end_gpus]<하위 GPU 범주에 해당하는 파일 추출>
```

```
Usage: AutoBench.exe [-h] [-v]
         [all]<Print All Info>
         [high_end_cpus]<Print the 1st CPU Info>
         [mid_range_cpus]<Print the 2st CPU Info>
         [midlow_range_cpus]<Print the 3st CPU Info>
         [low_end_cpus]<Print the 4st CPU Info>
         [high_end_gpus]<Print GPU the 1st Info>
         [mid_range_gpus]<Print GPU the 2st Info>
         [midlow_range_gpus]<Print GPU the 3st Info>
         [low_end_gpus]<Print GPU the 4st Info>
```

## 빌드 방법(How To Build)
[PyInstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html)
```
pip install pytinstaller
pyinstaller -D -F -n AutoBench -i icon.ico AutoBench.py
```

## Git Release
```Java
git tag -a vz.x.y -m ""
git push origin vz.x.y
```

# 원본 사이트(Source Site)

[CPU Benchmark Site](https://www.cpubenchmark.net/)<br>
[GPU Benchmark Site](https://www.videocardbenchmark.net/)

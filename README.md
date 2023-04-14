# simg-convert
***
## what .simg
1. ESP32 Arduino SMT32와 같은 소형 MCU의 이미지코덱입니다. 
2. RGB565를 사용하여 MCU의 디스플레이 입출력에 유용합니다. 
3. 복잡한 패턴이없는 이미지를 주로 사용할때 효율적입니다.
5. 무손실 압축방식으로 연속된 색상값을 압축합니다.
6. 런타임에서 디코딩을 하지않아 빠릅니다. (PNG, JPEG, BMP의 디코딩시간 많이소모)
***
## .simg 데이터 구성
1. format1 : [ 2byte:width ] [ 2byte:height ] [ 1byte:00000001 ] [ 2byte: RGB565 ][ 2byte: RGB565 ]  ...
2. format2 : [ 2byte:width ] [ 2byte:height ] [ 1byte:00000010 ] [ 2byte: RGB565 ][ 1byte: count  ]  ...
3. format1 과 format2 중에 용량이 작은 방식으로 선택적으로 사용가능
***
## How to use (Arduino IDE)
#### Downlaod this : https://github.com/Fluoritee/simg-Sprite
#### install zip lib
#### install TFT_eSPI or LovyanGFX
```c
#include <TFT_eSPI.h>
#include <SimgSprite.h>

TFT_eSPI tft;
TFT_eSprite* sprites;
SimgSprite simg(&tft);

void setup() {
  tft.init();
  tft.fillScreen(TFT_BLACK);
  
  sprites = simg.load("/1.simg");
  sprites->pushSprite(0,0,simg.TRANS);
```

# 컨버터 사용법
***

```shell
% python simg.sh -h
(base) laptop@fluoritesims-MacBook-Pro ~ % simg.sh -h
usage: simg.py [-h] [-r RESIZE RESIZE] [-b BACKGROUND BACKGROUND BACKGROUND] [-t THRESHOLD] file

입력인자를 설명해드립니다.

positional arguments:
  file                  변경할 이미지파일이나, 이미지파일들이있는 폴더의 전체 경로

optional arguments:
  -h, --help            show this help message and exit
  -r RESIZE RESIZE, --resize RESIZE RESIZE
                        변경될 이미지 사이즈 입력 (default: 변경 안함)
  -b BACKGROUND BACKGROUND BACKGROUND, --background BACKGROUND BACKGROUND BACKGROUND
                        배경색 R G B 입력 (default: 255 255 255)
  -t THRESHOLD, --threshold THRESHOLD
                        threshold 이하의 알파값은 투명으로 간주(-1 일때, 전부 불투명) (default: 0)
```
```shell
$ simg.sh /Users/laptop/Desktop/weathericon -r 50 50 -b 255 0 0 -t 0
```

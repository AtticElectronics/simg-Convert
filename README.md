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


## 컨버터 사용법
***


```shell
$ git clone https://github.com/Fluoritee/simg-convert.git
$ cd simg-convert
$ pip install -r requirements.txt
$ python simg.py [이지지파일] -w [출력 이미지 넓이] -h [출력 이미지 높이] -t [투명도 임계값]
$ python simg.sh -h 
 [매개변수 설명 ...]
$ simg.sh /Users/PC/Desktop/ImageFolder -r 50 50 -b 255 0 0 -t 0
 /Users/PC/Desktop 경로에 simg날짜xxxxx이미지 s생성됨
```

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

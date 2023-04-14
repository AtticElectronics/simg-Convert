# simg-convert
#### 이미지 파일을 .simg로 변환해주는 프로그램
#### Program to convert image files to .simg


## 요약
```shell
$ python simg.py ./image.png
$ cd simgXXXXX && ls
 image.simg
```

## 컨버터 사용법
1. 변환 가능 이미지 : BMP (Windows 비트맵)
DIB (Windows 기기 독립형 비트맵)
EPS (Encapsulated PostScript)
GIF (Graphics Interchange Format)
IM (ImageMagick)
JPEG (Joint Photographic Experts Group)
MSP (Microsoft Paint)
PCX (ZSoft IBM PC Paintbrush)
PNG (Portable Network Graphics)
PPM (Portable Pixel Map)
PSD (Adobe Photoshop)
TGA (Truevision Targa)
TIFF (Tagged Image File Format)
WEBP (WebP image format)
XBM (X Window System bitmap)
2. 여러개 동시변환 : 이미지 파일 이름 대신, 이미지 파일들이 있는 폴더를 입력

## 설치(Install)
```shell
$ git clone https://github.com/Fluoritee/simg-convert.git
$ cd simg-convert
$ pip install -r requirements.txt

```
## 간단 설명(Simple explanation)
```shell
$ python simg.py [이지지파일] -w [출력 이미지 넓이] -h [출력 이미지 높이] -t [투명도 임계값]
$ python simg.py -h 
 [매개변수 설명 ...]
$ simg.py /Users/PC/Desktop/img.png -r 50 50 -b 255 0 0 -t 0
  /Users/PC/Desktop 경로에 simgXXXXX 폴더가 생성되고 그안에 img.simg가생성됨
$ simg.py /Users/PC/Desktop/ImageFolder -r 50 50 -b 255 0 0 -t 0
  /Users/PC/Desktop 경로에 simgXXXXX 폴더가 생성되고 그안에 .simg 이미지로 변환됨
```

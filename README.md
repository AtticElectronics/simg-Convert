# simg-convert
## Why .simg
1. ESP32 Arduino SMT32와 같은 소형 MCU의 이미지코덱입니다. 
2. RGB565를 사용하여 MCU의 디스플레이 입출력에 유용합니다. 
3. 복잡한 패턴이없는 이미지를 주로 사용할때 효율적입니다.
5. 무손실 압축방식으로 연속된 색상값을 압축합니다.
6. 런타임에서 디코딩을 하지않아 빠릅니다. (PNG, JPEG, BMP의 디코딩시간 많이소모)

## 구성
[ 2byte:width ] [ 2byte:height ] [ 1byte:00000001 ] [ 2byte: RGB565 ][ 2byte: RGB565 ]  ...
[ 2byte:width ] [ 2byte:height ] [ 1byte:00000010 ] [ 2byte: RGB565 ][ 1byte: count  ]  ...

파일 시스템(SPIFFS, LittleFS, FATFS, SD)에서 
 포멧으로 
https://github.com/Fluoritee/simg-Sprite

'''cpp
//테스트
#include <stdio.h>
왜 내키보드에 코드블록 키가없다...
'''
```c
//테스트
#include <stdio.h>
복사해왔다.
```

```python
//테스트
#include <stdio.h>
복사해왔다.
```


```shell
% simg.sh /Users/laptop/Desktop/weathericon -r 50 50 -b 255 0 0 -t 0
$ simg.sh /Users/laptop/Desktop/weathericon -r 50 50 -b 255 0 0 -t 0
```
ode><pre>hello world</pre></code>

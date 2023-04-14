import os
import argparse
from PIL import Image
import struct
import datetime

def convert_RGBApixel_to_rgb565(pixel, bg_color, trans_th):
    r, g, b, a = pixel
    if a <= trans_th:
        return 65503
    else:
        # 배경색(bg_color)이 투명도만큼 비치는 픽셀값 생성.
        alpha_ratio = a / 255.0
        inv_alpha_ratio = 1 - alpha_ratio
        r = int(r * alpha_ratio + bg_color[0] * inv_alpha_ratio)
        g = int(g * alpha_ratio + bg_color[1] * inv_alpha_ratio)
        b = int(b * alpha_ratio + bg_color[2] * inv_alpha_ratio)

    result = ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)
    if result == 65503:
        result = 65535
    # 픽셀의 알파값 삭제 후 RGB565로 변환
    return result




def process_image(input_file, simg_folder_path,  new_width=-1, new_height=-1, bg_color=(255, 255, 255), trans_th=0):
    filename, _ = os.path.splitext(input_file)
    img = Image.open(input_file)
    if new_width == -1 and new_height == -1:
        new_width, new_height = img.size
    else:
        img = img.resize((new_width, new_height))

    img = img.convert('RGBA')

    pixel_data1 = b''
    for y in range(new_height):
        for x in range(new_width):
            pixel_data1 += struct.pack('<H', convert_RGBApixel_to_rgb565(img.getpixel((x, y)),bg_color,trans_th))

    len1 = len(pixel_data1)

    pixel_data2 = b''
    previous_pixel = None
    count = 0

    for y in range(new_height):
        for x in range(new_width):
            pixel = convert_RGBApixel_to_rgb565(img.getpixel((x, y)),bg_color,trans_th)

            if previous_pixel is None:
                previous_pixel = pixel
                count = 1
            elif previous_pixel == pixel and count < 256:
                count += 1
            else:
                pixel_data2 += struct.pack('<H', previous_pixel) + struct.pack('B', count - 1)
                previous_pixel = pixel
                count = 1

    pixel_data2 += struct.pack('<H', previous_pixel) + struct.pack('B', count - 1)

    len2 = len(pixel_data2)

    pixel_data = pixel_data1 if len2 >= len1 else pixel_data2

    output_file = os.path.join(simg_folder_path, os.path.basename(filename) + '.simg')
    with open(output_file, 'wb') as f:
        f.write(struct.pack('<HHB', new_width, new_height, 1 if len2 >= len1 else 2))
        f.write(pixel_data)

    print( 'file: ',output_file, '1 : ',len1,' 2 :',len2, ' w,h : ',new_width, 'x',new_height,' format :',1 if len2 >= len1 else 2 , ' bg_color :',bg_color)


def main():


    parser = argparse.ArgumentParser(description='입력인자를 설명해드립니다.')
    # 필수 인자 추가
    parser.add_argument('file', help='변경할 이미지파일이나, 이미지파일들이있는 폴더의 전체 경로')
    # 선택적 옵션 추가
    parser.add_argument('-r', '--resize',  nargs=2 , type=int, default=(-1,-1), help='변경될 이미지 사이즈 입력 (default: 변경 안함)')
    parser.add_argument('-b', '--background', nargs=3, type=int, default=(255,255,255), help='배경색 R G B 입력 (default: 255 255 255)')
    parser.add_argument('-t', '--threshold', nargs=1, type=int, default=0, help='threshold 이하의 알파값은 투명으로 간주(-1 일때, 전부 불투명) (default: 0)')
    args = parser.parse_args()
    # 결과 출력
    print(args.file)
    print(tuple(args.resize))
    print(tuple(args.background))
    print(args.threshold)


    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:17]
    input_path = args.file
    new_width, new_height  = args.resize
    bg_color = args.background
    trans_th = args.threshold[0]
    print(type(trans_th))

    simg_folder_path = os.path.join(os.path.dirname(input_path), "simg" + timestamp)
    os.makedirs(simg_folder_path)
    extensions = ['.png', '.jpg', '.jpeg', '.bmp']
    if os.path.isfile(input_path) and any(input_path.lower().endswith(ext) for ext in extensions):
        process_image(input_path, simg_folder_path, new_width, new_height , bg_color, trans_th)
    elif os.path.isdir(input_path):
        in_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if any(f.lower().endswith(ext) for ext in extensions)]
        for input_file in in_files:
            process_image(input_file, simg_folder_path, new_width, new_height, bg_color, trans_th)
    else:
        print("Invalid input. Please provide a valid image file or directory.")


if __name__ == '__main__':
    main()

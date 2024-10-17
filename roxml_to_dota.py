import os
import xml.etree.ElementTree as ET
import math

def totxt(xml_path, out_path):
    # 想要生成的txt文件保存的路径，这里可以自己修改

    files = os.listdir(xml_path)
    for file in files:

        tree = ET.parse(xml_path + os.sep + file)
        root = tree.getroot()

        name = file.strip('.xml')
        output = out_path + name + '.txt'
        file = open(output, 'w')

        

        objs = tree.findall('object')

        objsize = tree.findall('size')

        for i in objsize:
            img_width = int(float(i.find('width').text))
            img_height = int(float(i.find('height').text))
        

        for obj in objs:
            cls = obj.find('name').text
            box = obj.find('rotated_bndbox')
            x0 = int(float(box.find('x1').text)) / img_width
            y0 = int(float(box.find('y1').text)) / img_height
            x1 = int(float(box.find('x2').text)) / img_width
            y1 = int(float(box.find('y2').text)) / img_height
            x2 = int(float(box.find('x3').text)) / img_width
            y2 = int(float(box.find('y3').text)) / img_height
            x3 = int(float(box.find('x4').text)) / img_width
            y3 = int(float(box.find('y4').text)) / img_height

            if x0<0:
                x0=0

            if x1<0:
                x1=0

            if x2<0:
                x2=0
            if x3<0:
                x3=0

            if y0<0:
                y0=0

            if y1<0:
                y1=0

            if y2<0:
                y2=0
                
            if y3<0:
                y3=0

            file.write("0 {} {} {} {} {} {} {} {}\n".format(x0, y0, x1, y1, x2, y2, x3, y3))
        file.close()
        print(output)


if __name__ == '__main__':
    dotaxml_path = r'D:\learn\zuhui\shiyan\240118Work\ultralytics-8.1.0\ultralytics\dataset\SSDDR\labels\val\Annotations_test'
    out_path = r'D:/learn\zuhui\shiyan\240118Work\ultralytics-8.1.0\ultralytics\dataset\SSDDR\labels\val\txt_val/'

    totxt(dotaxml_path, out_path)
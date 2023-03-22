from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import json,sys
filename = sys.argv[1]
img=np.array(Image.open(filename))  #打开图像并转化为数字矩阵
#plt.figure("dog")
#plt.imshow(img)
#plt.axis('off')
#plt.show()

#print (img.shape) 

#print (img.dtype) 
#print (img.size) 
#print(type(img))

#for x in img:
  #print(x)


hex_colors = [[('%02x%02x%02x' % tuple(rgb)) for rgb in sublist] for sublist in img]


# 创建一个空的列表用于保存处理结果
result = []

def format_color(color, threshold=255):
    r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if brightness >= threshold:
        return False
    else:
        return f"{color[0:2]}:{color[2:4]}{color[4:]}"
  
for sublist in hex_colors:
    # 创建一个空的列表用于保存该行的处理结果
    row = []
    for color in sublist:
        formatted_color = format_color(color)
        # 将处理结果保存为一个字典对象
        item = {}
        if formatted_color == False:
            item = False
        else:
            item = formatted_color
        # 将字典对象添加到该行的列表中
        row.append(item)
    # 将该行的列表添加到结果列表中
    result.append(row)


# 将结果列表转换为 JSON 字符串
json_data = json.dumps(result)

#print(json_data)
with open(filename +".json", "w") as f:
    f.write(json_data)
    
    
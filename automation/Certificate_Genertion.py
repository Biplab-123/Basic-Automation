import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


df=pd.read_cecel(r,'')  ##read the excel sheet 

name_list = data["Name"].tolist()    ##Name is Heading of excel sheet

for i in name_list:
    im = Image.open(r'C:\Users\Rahul sinha\certificate_img.jpg')
    d = ImageDraw.Draw(im)
    #location = (100, 398)  ##need to calculate
    
    #text_color = (0, 137, 209)  ##need to decide
    
    #font = ImageFont.truetype("arial.ttf", 120) ##need to decide
    
    d.text(location, i, fill = text_color, font = font)
    
    im.save("certificate_" + i + ".pdf") ##save all the pdf file

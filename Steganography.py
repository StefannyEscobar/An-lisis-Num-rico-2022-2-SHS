from PIL import Image
from collections import deque
import base64



def binary_to_string(message):
    b64 = message.encode("utf8")
    bytes_ = base64.encodebytes(b64)
    bytestring = "".join(["{:08b}".format(x) for x in bytes_])
    bytestring += EOM
    return bytestring

def string_to_binary(bytestring):
    bytestring = bytestring.split(EOM)[0]
    binaryTemp=int(bytestring, 2)
    binary=binaryTemp.to_bytes(len(bytestring) // 8, byteorder='big')
    binary = base64.decodebytes(binary).decode("utf8")
    return binary



def printSample(image, n):
    for i in range (1):  ##width
        for j in range(n): ##height
            pixelx= image.getpixel((i,j))
            print (pixelx)
        
    print('--------------')
    # Altura y ancho de la imagen



    #Recorrer Imagen por pixel y volver los LSB de cada color en 0
def setImage(image1):
    for i in range (width):  ##width
        for j in range(height): ##height
        
            pixel = image1.getpixel((i,j))
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
           
            if (R%2!=0):
                image1.putpixel((i,j), (R-1,G,B))
                R=R-1
                
            if (G%2!=0):
                image1.putpixel((i,j), (R,G-1,B))
                G=G-1
                
            if (B%2!=0):
                image1.putpixel((i,j), (R,G,B-1))
                B=B-1
    return image1
       
#Mostrar valor pixeles    
'''   
for i in range (3):  ##width
    for j in range(3): ##height
        pixelx= image1.getpixel((i,j))
        print (pixelx)     
'''           
##print('--------------')
##print (text)


## Meter mensaje en la imagen    
def hideText(image1, text):    
    while(text):
        for i in range(width):
            for j in range (height):
                
                if len(text)==0:
                        break
                    
                pixel = image1.getpixel((i,j))
                R = pixel[0]
                G = pixel[1]
                B = pixel[2]
                
                for k in range(3):
                    
                    if len(text)==0:
                        break
                    elif text[0]=='1':
                        
                        text.pop(0)
                        if k==0:
                            image1.putpixel((i,j), (R+1,G,B))
                            R=R+1
                        if k==1:
                            image1.putpixel((i,j), (R,G+1,B))
                            G=G+1
                        if k==2:
                            image1.putpixel((i,j), (R,G,B+1))
                            B=B+1      
                    else:
                        text.pop(0)
    return image1
                

#Descifrar imagen
def readImage(image1):
    stack=deque()
   # digitos=10000
    for i in range(width):
        for j in range (height):
            #if digitos==0:
                  #  break
            
            pixel = image1.getpixel((i,j))
            
            for k in range (3):
                #if digitos==0:
                    #break
                
                if pixel[k]%2==1:
                    stack.append(1)
                   # digitos-=1
                else:
                    stack.append(0)
                    #digitos-=1
    return stack
   
         

##image1.show()  




    #Imagen a ingresar 
image1= Image.open('2257-paisajes.jpg') 
#image1= Image.open('Encrypted.jpg')

width , height = image1.size

    #fin del mensaje
EOM= "010101010100011101101100011101010101100100110010011010000110110001001001010001110100111000110001011000110110110101101100011101100110001100110010001110000011110100001010"

#'''   

    #Mensaje a esconder
message='Hola terricolas' 

    #pasar el mensaje a binario y luego convertirlo en lista
binary= binary_to_string(message)
text=[]
text[:0]= binary

    #Preparar imagen cambiando los LSB por 0
##printSample(image1 , 20)
image1=setImage(image1)
##printSample(image1 , 20)

    #Esconder texto en la imagen y guardarla
image1=hideText(image1 , text)

#printSample(image1,20)


    # Se debe guardar el archivo en .tif para no tener perdida de informacion al guardar la imagen
image1.save('Encrypted.tif')
##'''


#Descifrar
#'''
image2= Image.open('Encrypted.tif')


    #Extraer texto de la imagen e imprimir
#print('sample img2')
#printSample(image2 , 20)
stack=readImage(image2)
txt= ''.join([str(x) for x in stack])
#print(txt[:20])
print(string_to_binary(txt))

##'''
#message= ""
#binary= binary_to_string(message)
print('-------------------------------')

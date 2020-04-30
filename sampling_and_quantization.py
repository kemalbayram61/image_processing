import  numpy,cv2

#allows to bring the values in the line specified on the picture
def GetValues(image,image_line):
    values=[]
    for i in range(image.shape[1]): 
        values.append(image[image_line,i,0])
    return values


#creates and shows the sampling picture according to the received values
def CreateSamplingImage(sampling_values):
    sampling_image=numpy.zeros((256,len(values),1),dtype=numpy.uint8)
    for i in range(len(sampling_values)):
        sampling_image[255-sampling_values[i],i]=255
    cv2.imshow("Sampling Image",sampling_image)
    cv2.waitKey(0)
    return sampling_image

#takes the values that come to it in the specified range
def MapValue(value,last_max_value,new_max_value):
      new_value=new_max_value*value/last_max_value
      return int(new_value)
  
#takes the values that come to it in the range 0-255
def Map255(value,last_max_value):
    new_value=255*value/last_max_value
    return int(new_value)

#quantizes the values
def QuantizationValues(last_values,last_quantization_bit,new_quantization_bit):
    for i in range(len(last_values)):
        new_value=MapValue(last_values[i],2**last_quantization_bit,2**new_quantization_bit)
        last_values[i]=Map255(new_value,2**new_quantization_bit)
    return last_values

#quantities at the officially determined bit level
def QuantizationImage(image,last_quantization_bit,new_quantization_bit):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_value=MapValue(image[i,j,0],2**last_quantization_bit,2**new_quantization_bit)
            new_value=Map255(new_value,2**new_quantization_bit)
            image[i,j,0]=new_value
            image[i,j,1]=new_value
            image[i,j,2]=new_value
    cv2.imshow("QuantizationImage",image)
    cv2.waitKey(0)
    return image

image=cv2.imread("gray_image.png")#imports the picture
print("Line number:",image.shape[0])#the shape[0] property returns the line number of the image
print("Column number:",image.shape[1])#the shape[1] property returns the column number of the image


#values=GetValues(image,400)
#print(values)

#CreateSamplingImage(values)

#new_values=QuantizationValues(values,8,4)
#CreateSamplingImage(new_values)
QuantizationImage(image,8,4)#Image quantized with 8 bits Quantities with 4 bits

values=GetValues(image,400)
print(values)
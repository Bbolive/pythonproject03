#กล่องขนาดกว้าง ?? เมตร ยาว ?? เมตร สูง ?? เมตร ใช้สีจำนวน ?? แกลอน
#ทั้งนี้สี 1 แกลอนทาได้ 5 ตารางเมตร ทั้งนี้แกลอนที่คำนวณได้หากเป็นเลขทศนิยมให้ปัดขึ้นให้เป็นเลขจำนวนเต็ม
def line():print('..................................................')
width = float(input("ป้อนความกว้าง : "))
length = float(input("ป้อนความยาว : "))
height = float(input("ป้อนความสูง : "))
area = ((width*height)+(height*length)+(length*width))*2
if area%5 == 0 :
    Color = int(area/5)
else :
    Color = int((area/5)+1)
line()
print (f"ต้องใช้สี {Color} แกลอน")
line()
print ('ต้องใช้สี',Color,'แกลอน')
line()
print ('ต้องใช้สี '+str(Color)+' แกลอน')
line()
print ('ต้องใช้สี {} แกลอน'.format(Color))
line()
print ('ต้องใช้สี %d แกลอน'%(Color))
line()
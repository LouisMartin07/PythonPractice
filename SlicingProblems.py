#The goal is to use the string msg to create a new string that reads 
# 1 Welcome Ring To Tyler using slicing

msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())

#now print the string backwards

print(msg1[::-1].title())
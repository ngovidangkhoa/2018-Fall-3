fobject = open('important.txt','w')
fobject.write('go go go stop')
fobject.close()

fobject = open('important.txt','r')
print(fobject.read(5))
print(fobject.read())
fobject.close()

fobject = open('important.txt','w')
fobject.write('line1\nline2\nline3\nline4')
fobject.close()

fobject = open('important.txt','r')
print (fobject.readline())
print (fobject.readlines())
fobject.close()





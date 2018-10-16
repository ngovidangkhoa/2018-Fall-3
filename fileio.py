fobject = open('important.txt','w')
fobject.write('go go go')
fobject.close()

fobject = open('important.txt','r')
fobject.read(5)
fobject.read()
fobject.close()

fobject = open('important.txt','r')
print fobject.readline()
print fobject.readlines()
fobject.close()

fobject = open('important.txt','r')
fobject.write('line1\nline2\nline3\nline4')
fobject.close()


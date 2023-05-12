f = open("PROJI-DNSRS.txt")
f1 = open("PROJI-HNS.txt")
line = f1.readline()
new = line.strip('\n')
print(new)
list =f.readlines()
#for i in range(len(list)):
dict = set()
dd = {}
for item in list:
    s = item.split()
    dict.add(s[0].strip('\n'))
    hostname = s[0].strip('\n')
    dd[hostname] = item
    print(hostname)
    print(dd[hostname])
  #dict.add(list[i].split())'true
for i in range(len(list)):
   if new in dict:
      print(dd[new])
      break
   else:
      print('false')







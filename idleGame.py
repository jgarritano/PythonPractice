import json
import investments

myfile = open('savefile.txt')
myCashStr= myfile.readline()
myfile.close()
myCash = int(myCashStr)

#investments = {'lemons': 0, 'newspapers':0}
#Q = json.dumps(investments)

#myJFile = open('savefile2.txt','w')
#json.dump(investments,myJFile, indent =4 )

Q = json.load(open('savefile2.txt'))

income= Q['lemons'] * 1 + Q['newspapers'] *2

income = investments.computeLemons(Q['lemons'])
myCash += income

#print(Q)
print(myCash)


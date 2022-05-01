import xml.sax
from xml.sax import make_parser
dataset = []
arr = []
plus100 = []
class GroupHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.record = ""
        self.cases = ""
        self.deaths = ""
        self.countriesAndTerritories = ""
        self.continentExp = ""
        self.barrier = []
        self.records = []
        self.plus100 = []
    def startElement(self, name, attrs):
        self.current = name
        if name == "record":
            pass
        elif name == "cases":
            self.cases = attrs.get('cases')
        elif name == "deaths":
            self.deaths = attrs.get('deaths')


    def characters(self, content):
        if self.current == "record":
            self.record == content
        elif self.current == "cases":
            self.cases = content
        elif self.current == "deaths":
            self.deaths = content
        elif self.current == "countriesAndTerritories":
            self.countriesAndTerritories = content
        elif self.current == "continentExp":
            self.continentExp = content

             
    def endElement(self, name):
        
       # if(name == "cases")  and (int(self.cases) >= 100)  :
        if(name == "cases"):
         #   self.barrier.append(" record ")
            self.barrier.append(str(self.cases))
            dataset.append(str(self.cases+";"))
        if(name == "deaths"):
            self.barrier.append(";"+self.deaths+";")
            dataset.append(self.deaths+";")
        if(name == "countriesAndTerritories"):
            self.barrier.append(self.countriesAndTerritories+";")
            dataset.append(self.countriesAndTerritories+";")
        if(name == "continentExp"):
            self.barrier.append(self.continentExp)
            dataset.append(self.continentExp+" ;")
            #self.barrier.append(" end ")
        

            
           # print("cases = %s - deaths =  %s" % (self.cases, self.deaths))  
        #print(len(self.barrier))
        #56968
       # print(self.barrier)

      #  with open('sax.txt', 'w') as f:
        #    for item in self.barrier:
           #     f.write(" %s " % item)
        
        def makeResult(self): 
            print(len(self.barrier))
            for i in range(0,len(self.barrier),4):
                if i == len(self.barrier) or i+4 ==  len(self.barrier):
                    break
                print(i)  
        
        
         #   if int(int(self.barrier[i]) >= 100):
         #       self.plus100.append(self.barrier[i]+str(self.barrier[i+1])+self.barrier[i+2]+self.barrier[i+3])
       # print(self.plus100)
       # print(*self.plus100, sep = "\n")

     #   for i in range(0,len(self.barrier)-6,6):
        #    self.records.append(self.barrier[i]+str(self.barrier[i+1])+self.barrier[i+2]+self.barrier[i+3]+self.barrier[i+4]+self.barrier[i+5])

        #print(self.records)

       
   ###    if self.current == "cases" and int(self.cases) >= 100 :
    #        print("-----COL----")  
    ##        print("cases: {} ".format(self.cases))
      ###     print("continentExp: {} ".format(self.continentExp))


       

        
handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('covid19.xml')
saxparser = make_parser()

datasource = open('covid19.xml',"r")
saxparser.parse(datasource)

#done writing
#with open('sax3.txt', 'w') as f:
#    for item in dataset:
 #       f.write(" %s " % item)

#with open('sax.txt') as f:
 #   lines = f.readlines()
#    print(lines)

f = open('sax3.txt', 'r+')
my_file_data = f.read()
f.close()

#print(my_file_data)
foo = ''
foo = my_file_data
arr = foo.split(';');
#print(arr) 


#print(len(arr))
for i in range(0,len(arr)-4,4):
    #if i == len(arr) or i+4 ==  len(arr):
    #    break
    if int(arr[i]) >= 100 :
        print(arr[i]+";"+str(arr[i+1])+";"+arr[i+2]+";"+arr[i+3])
        element = arr[i]+";"+str(arr[i+1])+";"+arr[i+2]+";"+arr[i+3]
        plus100.append(element)
        
# writing to sax.txt is Done , task is Done!
with open('sax.txt', 'w') as f:
    for item in plus100:
      f.write(" %s\n " % item)
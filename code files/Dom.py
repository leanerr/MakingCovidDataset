from calendar import day_abbr, month
from xml.dom import minidom

doc = minidom.parse("covid19.xml")

dates = []

#Done making a time format and save it to an array
#IT DOES NOT WORK WHEN U ARE DELETING DAY MONTH YEAR
dateRep = doc.getElementsByTagName("dateRep")
#print(dateRep)
for date in dateRep:
   day = date.getElementsByTagName("day")[0]
   months = date.getElementsByTagName("month")[0]
   year = date.getElementsByTagName("year")[0]
   res = str(day.firstChild.data)+"/"+str(months.firstChild.data)+"/"+str(year.firstChild.data)
   dates.append(str(res))
#print(day.firstChild.data)

#print(dates)


country_code = doc.getElementsByTagName("countryterritoryCode")
for code in country_code:
  #  print(code.parentNode.child(code))
    parent = code.parentNode
    #done deleting it !
    parent.removeChild(code) 
days = doc.getElementsByTagName("day")
month = doc.getElementsByTagName("month")
years = doc.getElementsByTagName("year")
 
for day in days:
    parent = day.parentNode
    #done deleting it !
    parent.removeChild(day) 

for mnt in month:
    parent = mnt.parentNode
    #done deleting it !
    parent.removeChild(mnt)

for yr in years:
    parent = yr.parentNode
    #done deleting it !
    parent.removeChild(yr) 

#print(doc.toxml())

#Done making first try and deleting done.
#with open("dom.xml","w") as fs:
#    fs.write(doc.toxml())
#    fs.close()




#Done writing dates with right format
#with open('dates.txt', 'w') as f:
#    for item in dates:
#        f.write(" %s\n " % item)


i = 0
for tag_type in doc.getElementsByTagName('dateRep'):
    #while tag_type.hasChildNodes():
        #tag_type.removeChild(tag_type.firstChild)
    if i == len(dates):
        break
    tag_type.appendChild(doc.createTextNode(str(dates[i])))
    i=i+1

#print(doc.toxml())

#Done task , Done !
with open("dom.xml","w") as fs:
    fs.write(doc.toxml())
    fs.close()
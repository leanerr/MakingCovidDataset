import lxml.html
from lxml import etree

xslt_doc = etree.parse("dom.xsl")
xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse("dom.xml")
output_doc = xslt_transformer(source_doc)
 
#print(str(output_doc))
#first HTML page with All data is Done!
#the task is completed and its Done 100% !
output_doc.write("transformed.html", pretty_print=True)
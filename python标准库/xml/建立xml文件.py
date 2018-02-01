from xml.dom import minidom, Node

doc = minidom.Document()
doc.appendChild(doc.createComment("Sample XML Document - Chapter 8"))

#
book=doc.createElement("book")
doc.appendChild(book)
#
title=doc.createElement("title")
title.appendChild(doc.createTextNode("Sample XML Thing"))
book.appendChild(title)



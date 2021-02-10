#!C:\Users\lumbo\AppData\Local\Programs\Python\Python38\python.exe


import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value

openfile = open('script/'+pageId, 'w', encoding='utf-8')
openfile.write(description)
openfile.close()

os.rename('script/'+pageId, 'script/'+title)


#Redirection
print("Location: index.py?id="+title)
print()

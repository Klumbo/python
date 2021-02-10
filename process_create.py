#!C:\Users\lumbo\AppData\Local\Programs\Python\Python38\python.exe


import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

openfile = open('script/'+title, 'w', encoding='utf-8')
openfile.write(description)
openfile.close()

#Redirection
print("Location: index.py?id="+title)
print()

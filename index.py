#!C:\Users\lumbo\AppData\Local\Programs\Python\Python38\python.exe

print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('script')
list = ''
for k in files:
    list += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=k)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    sc = open('script/'+pageId, 'r', encoding='utf-8').read()
    updatelink = '<a href="update.py?id={}"><font color=red size=5px>update</font></a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId="Food"
    sc="인간이 먹음으로써 활동에 필요한 영양분을 얻는 것. 대부분 불이나 도구를 사용해불필요한 부위를 제거하거나 먹기 쉽게 가공한 것을 의미한다. 먹을 수 있는 것 자체를의미하는 식량과는 포괄하는 범위가 다르다. 생존에 직결되는 만큼 과거부터 매우 중하게 생각됐으며 인간이 살아가는 데 있어 꼭 필요한 3요소인 의식주 중 하나로 꼽다."
    updatelink = ''
    delete_action = ''
print('''
<!DOCTYPE html>
<html>
  <head>
    <title>푸드 북</title>
    <meta charset="euc-kr">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1><a href="index.py">패스트푸드 3대장</a></h1>
    <div id="grid">
      <ol>
      {list}
      <a href="create.py"><font color=blue size=5px>create</font></a>
      {updatelink}
      {delete}
      </ol>
      <div id="gridtext">
        <h2>{title}</h2>
        <p>{script}</p>
      </div>
    </div>
  </body>
</html>
'''.format(title=pageId, script=sc, list=list, updatelink=updatelink, delete=delete_action))

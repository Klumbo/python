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
else:
    pageId="Food"
    sc="인간이 먹음으로써 활동에 필요한 영양분을 얻는 것. 대부분 불이나 도구를 사용해불필요한 부위를 제거하거나 먹기 쉽게 가공한 것을 의미한다. 먹을 수 있는 것 자체를의미하는 식량과는 포괄하는 범위가 다르다. 생존에 직결되는 만큼 과거부터 매우 중하게 생각됐으며 인간이 살아가는 데 있어 꼭 필요한 3요소인 의식주 중 하나로 꼽다."
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
      <a href="script_update.py"><font clor=green size=5px>update</font></a>

      </ol>
      <div id="gridtext">
        <h2>글 내용 변경</h2>
        <form action="process_update.py" method="post">
            <input type="hidden" name="pageId" value="{bringtitle}">
            <p><input type="text" size=100 name="title" placeholder="title" value="{bringtitle}" maxlength=9></p>
            <p><textarea rows="4" cols=91 name="description" placeholder="description">{bringdc}</textarea></p>
            <p><input type="submit"></p>
        </form>
      </div>
    </div>
  </body>
</html>
'''.format(title=pageId, script=sc, list=list, bringtitle=pageId, bringdc=sc))

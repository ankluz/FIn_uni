from os import getcwd
import socket 
import datetime

sock = socket.socket() 

try: 
  sock.bind(('',80)) 
except OSError: 
  sock.bind(('', 8080)) 

sock.listen(5)
conn, addr = sock.accept() 
print("Connected", addr)

while 1:
  data = conn.recv(8192)
  msg=data.decode()
  msg = msg.split('\n')
  get = msg[0].replace('GET','',1).replace('HTTP/1.1','',1).strip()

  try:
    if get == '/':
      with open(getcwd()+"\\workDir\\index.html",'r+',encoding='utf-8') as f:
        file = f.read()
    elif get != '':
      with open(getcwd()+"\\workdir"+get,'r+',encoding='utf-8') as f:
        file = f.read()
    else:
      file = 'Ошибка в запросе'
  except FileNotFoundError:
    print('Запрошенный файл отсутствует. ',msg[0])
    conn.send("""HTTP/1.1 404""".encode())
    conn.close()
    continue

  resp=f"""HTTP/1.1 200 OK
  Date: {datetime.datetime.now()}
  Connection: close

  {file}"""

  conn.send(resp.encode())  
  conn.close()
  conn, addr = sock.accept() 

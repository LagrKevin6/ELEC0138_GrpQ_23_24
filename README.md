# ELEC0138_GrpQ_23_24
Created for documenting the codes generated while completing ELEC0138 final assignment by Group Q.
Involving with designing a security and privacy threat model (ideally regarding of a market online database), relevant attack set-ups and code implementations
and concludes by a video presentation. 
4 of us would devote about 1/2 month contributing to this.

A Django based website is built for simulating a database access terminal.
Main functions of code files:
/sec_data: contains a django project named sce_data, for security_database.
/login: for an app with a login and a view_login function.
/login/urls: tells what should be returned when a certain url called.
/login/views: tells what should be seen when returned.

Usage: install django and cd to this main folder (sce_data);
run 

python manage.py runserver

python manage.py runserver 0.0.0.0:8000 (to make it accessible on local network)


to start a web server at the local network. An IP address would be given and accessible at web browser.
e.g.: 

http://127.0.0.1:8000/login/: should see a brief text response 'This starts'

http://127.0.0.1:8000/login/new: login func. One account available is admin_q, pwd = 123456

http://127.0.0.1:8000/login/view_logins : checks all login details (designed on purpose)

http://127.0.0.1:8000/login/show_visits : checks number of visits to login/view_logins (designed for ddos)

to brute-force the password, run:

python attack_script.py

to ddos a url (default as login/view_logins), run:

python dos_attack_implementation.py

to check the username and pwd in captured .pcapng file, run:
python check_packet.py

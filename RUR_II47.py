import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('192.168.1.110', 8072))
serversocket.listen(5) # become a server socket, maximum 5 connections

radius, address1 = serversocket.accept()        ##pocetna spajanja
print(radius,address1)

x=raw_input()           #helena-covjek: poor radius
radius.send('ja te volim')  #send me to tha stamping mill
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: but i dont want them to kill you
x=raw_input()           
radius.send('ja te volim')  #i won't work
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: do you hate us? why?
x=raw_input()           
radius.send('ja te volim')  #You are not as strog as the robots
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: but someone must give orders
x=raw_input()           
radius.send('ja te volim')  #i don't want any master
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: Radius, dr.Gall gave you a better brain
x=raw_input()           
radius.send('ja te volim')  #i don't want any master
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: I'm sure they'd put you in charge 
x=raw_input()           
radius.send('ja te volim')  #I'm sure they'd put you in charge 
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: You are mad.
x=raw_input()           
radius.send('ja te volim')  #Then send me to the stamping-mill.
radius, address1 = serversocket.accept()        
print(radius,address1)
            #helena: Do you think we're afraid of you
x=raw_input()           
radius.send('ja te volim')  #What are you going to do? 
radius, address1 = serversocket.accept()        
print(radius,address1)
           

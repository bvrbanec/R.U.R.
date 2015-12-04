import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('192.168.1.111', 8072))
serversocket.listen(5) # become a server socket, maximum 5 connections

helena, address1 = serversocket.accept()        ##pocetna spajanja
print(helena,address1)
primus, address2 = serversocket.accept()
print(primus,address2)
x=raw_input()       ##kreni s pretstavom

helena.send('helena')           #What could happen to us, Primus? 
print(helena.recv(512))
helena, address1 = serversocket.accept()       
print(helena,address1)
                                #Alquist prica
x=raw_input()  
primus.send('bok')              #The Robot Primus.
primus, address2 = serversocket.accept()
print(primus,address2)          #i ceka
                                #Alquist:what..
x=raw_input()
helena.send('helena')           #Robotess helena 
print(helena.recv(512))
helena, address1 = serversocket.accept()       
print(helena,address1)
                                #Alguist: Turn around
x=raw_input()
primus.send('bok')              #Sir, do not frighten her.
primus, address2 = serversocket.accept()
print(primus,address2)

                                #Alguist: what?
x=raw_input()
primus.send('bok')              #2years ago.
primus, address2 = serversocket.accept()
print(primus,address2)
                                #Aluist: By dr.Gall?
x=raw_input()
primus.send('bok')              #Yes Like me
primus, address2 = serversocket.accept()
print(primus,address2)
                                #Aluist: Laugter Lughetr?
x=raw_input()
primus.send('bok')              #Why
primus, address2 = serversocket.accept()
print(primus,address2)
                                #Aluist: I wich ti experiment on her?
x=raw_input()
primus.send('bok')              #Uppon heena?
primus, address2 = serversocket.accept()
print(primus,address2)
                                #Aluist: Ofcourse?
x=raw_input()
primus.send('bok')              #If you do i will kill you
primus, address2 = serversocket.accept()
print(primus,address2)
                                #Aluist: Kill me
x=raw_input()
primus.send('bok')              #Sir take me
primus, address2 = serversocket.accept()
print(primus,address2)
primus.recv(512) #i cekaj sljedeci

helena.send('oj')               #no no, you shall not
helena, address1 = serversocket.accept()
print(helena,address1)
                            #Aluist: Whait girl ! wait
x=raw_input()
primus.send('bok')              #Not without her
primus, address2 = serversocket.accept()
print(primus,address2)
                            #Aluist: very vell
x=raw_input()
helena.send('bok')              #Primus primus
helena, address1 = serversocket.accept()
print(helena,address1)
                            #Aluist: child child you can weep
x=raw_input()
helena.send('bok')              #Iwill go myself
helena, address1 = serversocket.accept()
print(helena,address1)
                            #Aluist: where??
helena.send('helena')      ## Helena:In there to be cut.  Let me pass, Primus! Let me pass! 
helena, address1 = serversocket.accept()
print(helena,address1)

helena.recv(512)        #you shoul not go
primus.send('bok')
primus, address2 = serversocket.accept()
print(primus,address2)

primus.recv(512)        #if you go in there
helena.send('kreni')
helena.recv(512)
helena, address1 = serversocket.accept()
print(helena,address1)
print(helena.recv(512))
primus.send('bok')
primus, address2 = serversocket.accept()
print(primus,address2)
x=raw_input()
primus.send('bok')


serversocket.close()

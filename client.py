import socket
import rsa
import threading
c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',5000))
public_key, private_key=rsa.newkeys(1024)
public_partner=None



c.send(public_key.save_pkcs1("PEM"))
public_partner=rsa.PublicKey.load_pkcs1(c.recv(1024))
nick= input("your nickname: ")
c.send(nick.encode('utf-8'))
print("\n------------------------------------------------------ Chat Commands --------------------------------------")
print("Broadcast a message: just type your message")
print("Direct Message: dm <nickname> <message>")
print("Create a Room: /createroom <room_name> @user1 @user2")
print("Message a Room: @<room_name> <message>")
print("List Users: /list")
print("Quit: /quit")
print("tag someone: $<person nickname>")
print("--------------------------------------------------------------------------------------------------------------")

def send():

    while True:
        message = f'{nick}: {input("")}'
        if message==f'{nick}: /quit':
            c.send(rsa.encrypt(message.encode('utf-8'),public_partner))          
            c.close()
            break
        
        else:
            
            c.send(rsa.encrypt(message.encode('utf-8'),public_partner))
def recieve():
    while True:
        message=rsa.decrypt(c.recv(1024), private_key).decode()
        print(message)


threading.Thread(target=send).start()
threading.Thread(target=recieve,daemon=True).start()       
        





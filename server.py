import rsa
import datetime
import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost',5000))
s.listen()
print("server created")

print("server is waiting for for connection")
users=[]
nickname=[]
public_partener=[]
chat_rooms={}
serpublic_key,private_key=rsa.newkeys(1024)
def timestamp(message):
    time=datetime.datetime.now().strftime("[%H:%M:%S]")
    stamped_message=f'{time} {message}'
    return stamped_message



def roombroadcast(room_name, message):
    if room_name in chat_rooms:
        members = chat_rooms[room_name]
        for member in members:
            try:
                indexer = nickname.index(member)
                client = users[indexer]
                partner_key = public_partener[indexer]
                stamped_message=timestamp(message)
                client.send(rsa.encrypt(stamped_message.encode('utf-8'), partner_key))
            except :
                print("")
def tagged(nick,sender):
    indexer=nickname.index(nick)
    client=users[indexer]
    client.send(rsa.encrypt(f'you are tagged in message by {sender}\n'.encode('utf-8'),public_partener[indexer]))
def dm(nick,message):
    indexer=nickname.index(nick)
    client=users[indexer]
    messages=message.replace(f'/dm {nick}','')
    stamped_message=timestamp(messages)
    client.send(rsa.encrypt(f'DM {stamped_message}'.encode('utf-8'),public_partener[indexer]))

def remover(client):
    if client in users:
        indexer =users.index(client)
        nick =nickname[indexer]

        for key,value in chat_rooms.items():
            if nick in list(value):
                list(value).remove(nick)
                
        print(f'{nickname[indexer]} left the server')
        users.remove(client)
        nickname.remove(nickname[indexer])
        public_partener.remove(public_partener[indexer])
        

    
    

def brodcast(message):
    stamped_message=timestamp(message)
    for user in users:
        index=users.index(user)
        user.send(rsa.encrypt(stamped_message.encode('utf-8'),public_partener[index]))

def chat(client):
    while True:
        try:
            message= rsa.decrypt(client.recv(1024),private_key).decode()
            
            
            index =users.index(client)
            nick=nickname[index]
            clean_message= message.replace(f'{nick}: ','')
            if message==f'{nick}: /list':
                client.send(rsa.encrypt("list of connected users: ".encode('utf-8'),public_partener[index]))
                for nicks in nickname:
                    
                    client.send(rsa.encrypt(nicks.encode('utf-8'),public_partener[index]))

            elif '/createroom' in message:
                
                parts = clean_message.split()
                room_name = parts[1]
                try:
                    if room_name in chat_rooms:
                        client.send(rsa.encrypt(f"server: room '{room_name}' already exist".encode('utf-8'), public_partener[index]))
                        continue
                    else:
                        taggedusers=[]
                        for p in parts:
                            if p.startswith('@'):
                                taggedusers = taggedusers +[p[1:]]
                            else:
                                pass
                        allmembers = [nick] + taggedusers

                        chat_rooms[room_name] = allmembers
                        notification = f"SYSTEM: You have been added to the private room '{room_name}' by {nick}."
                        roombroadcast(room_name, notification)
                        print(f"Room '{room_name}' created by {nick} with members: {allmembers}")
                except:
                    print("please enter in the correct format")


            elif '@' in message:
                
                parts = clean_message.split()
                room_name = parts[0][1:]
                if room_name in chat_rooms and nick in chat_rooms[room_name]:
                    
                    roombroadcast(room_name, message)
                else:
                    client.send(rsa.encrypt(f"SYSTEM: You are not in room '{room_name}' or it doesn't exist.".encode('utf-8'), public_partener[index]))

               
            elif message==f'{nick}: /quit':
                brodcast(f'{nick} left the chat')
                remover(client)
                
            else:
                for nicks in nickname:
                    brdc=True
                    
                    if f'/dm {nicks}' in message:
                        dm(nicks,message)
                        brdc=False
                        break
                    elif f'${nicks}' in message:
                        tagged(nicks,nick)
                        break
                        

                    else:
                        continue
                if brdc:
                    brodcast(message)
                

        except:
            remover(client)
            break
    

def recieve():
    while True:
        client, addr= s.accept()
        
        pubkey=rsa.PublicKey.load_pkcs1(client.recv(1024))
        client.send(serpublic_key.save_pkcs1("PEM"))
        nick= client.recv(1024).decode()
        users.append(client)
        nickname.append(nick)
        public_partener.append(pubkey)
        indexer=users.index(client)
        #client.send(rsa.encrypt("you joined the server".encode('utf-8'),public_partener[indexer]))
        brodcast(f'{nick} joined the chat')

        print(nick,'joined the server')


        threading.Thread(target=chat, args=(client,)).start()


recieve()




    

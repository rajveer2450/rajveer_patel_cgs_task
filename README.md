# rajveer_patel_cgs_task
this is a repository for the CGS WebX selections
--Chatnet--
This is a command-line, client-server chat application built in Python. It uses the `rsa` library to make the communications end-to-end encrypted. The application supports public brodcast direct messages(DM) and private chat rooms

--Features--
End to End Encryption: Utilizes RSA asymmetric encryption to secure all messages.
Real time messaging: using sockets and threading for instant message delivery.
Broadcast: Send messages to all the users.
Direct Messaging (DM): Send a private message to a specific user.
Private Chat Rooms: Create chat rooms with specific users.
User Tagging: 
user List: View all connected users.
Timestamps: All messages are timestamped.

--Setup and Installation-- 
Follow these steps to set up and run the application on your local machine.
Prerequisites
--Python 3
Installation
1.  Clone the repository or download the files into a new directory.
    ```bash
    git clone https://github.com/rajveer2450/rajveer_patel_cgs_task.git cd <repository-directory>
    ```
2.  Create and activate a virtual environment on command prompt
    ```bash
     python -m venv venv
    ```
and then:
     ```
     .\venv\Scripts\activate
     ```

3.  Install the required packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```



---How to Run and Test--- 

You need at least two separate terminal windows: one for the server and one for each client.

1. Start the Server
In your first terminal, run the `server.py` script.
```bash
python server.py
```
you should see the output:

server created
server is waiting for connection

2. Start Clients
Open a new terminal and run the client.py script. You will be prompted to enter a nickname.
```Bash
python client.py
```
your nickname: Alice

Open another new terminal and run the client script again for a second user.
```Bash
python client.py
```
your nickname: Bob

3. Testing Methods
You can now test the various features:

Broadcast Messaging:
Action: In Alice's terminal, type Hello everyone! and press Enter.
Expected Result: The message [HH:MM:SS] Alice: Hello everyone! should appear in both Alice's and Bob's terminals.

Direct Messaging (DM):
Action: In Alice's terminal, type /dm Bob Just for you and press Enter.
Expected Result: The message DM [HH:MM:SS] Just for you should appear only in Bob's terminal.

List Users:
Action: In any client's terminal, type /list.
Expected Result: That client will receive a list of connected users: Alice and Bob.

Create and Message a Room:
Action (Create): In Alice's terminal, type /createroom projectX @Bob.
Expected Result: Both Alice and Bob will receive a system notification that they have been added to the room projectX.

Action (Message): In Bob's terminal, type @projectX Let's start the project.
Expected Result: The message [HH:MM:SS] projectX Let's start the project will appear in both Alice's and Bob's terminals, but not in any other client's terminal.

Tagging a User:
Action: In Bob's terminal, type Hey $Alice check this out.
Expected Result: Alice will receive a special notification: you are tagged in message by Bob. The original message from Bob will still be broadcast to everyone.

Quitting the Chat:
Action: In Bob's terminal, type /quit.
Expected Result: Bob's client script will terminate. Alice's terminal will display a message like [HH:MM:SS] Bob left the chat. The server terminal will log that Bob has left.

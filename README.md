[![Gitter][gitter-picture]][gitter] ![py27][py27] ![py35][py35] [English version][english-version]

# WechatBOT_python
Using itchat platform (python)  for automation and auto reply of images, files etc

# Setup
This bot works with a python installed with a version of 3 or above


>python --version
to check your python version

Clone the repository somewhere

> npm itchat

Install the itchat dependencies you need


>itchat.auto_login(hotReload = True)

This saves the record, user does not have to login each time

```python
import time, datetime, requests, itchat    
from itchat.content import *
```
Now you can import and use it

>hotReload = True’ inside the ‘itchat.auto_login(hotReload = True)’

this saves the memory of the user that logged in. So that the same user doesn’t have to login by scanning the QR code. If you want to aboard a new user, delete the pkl file or ‘hot reload=True’.


# License
free usage
this project was made with the platform itchat:

https://github.com/littlecodersh/ItChat/wiki/Tutorial1
https://itchat.readthedocs.io/zh/latest/

# Project 
## I.	Basic Introduction on Development:

You also have to register certain keywords before defining the corresponding functions and parameters:

```python
Ex) 
@itchat.msg_register(FRIENDS)
Ex) 
@itchat.msg_register(TEXT,isGroupChat=True)
def auto_reply(msg):
    coming_from = msg.get('ActualNickName')
    context = msg.text
    friend = itchat.search_friends(name=coming_from)
    print(f'{coming_from}:{context}')

isGroupChat=True allows it to only work when the message is sent from the group chat
```

## II.	RETREIVE INFORMATION FROM THE TEXT SENT:
```python
Getting name of User that sends the message:
msg.get('ActualNickName')

The content of the message
msg.text


ex) 
@itchat.msg_register(TEXT,isGroupChat=True)
def auto_reply(msg):
    coming_from = msg.get('ActualNickName')
    context = msg.text
    friend = itchat.search_friends(name=coming_from)
    print(f'{coming_from}:{context}')

# now we can print who it is coming from and the content
# notice that we defined the
coming_from = msg.get('ActualNickName')
coming_from to be the user that sent the message
friend = itchat.search_friends(name=coming_from)
friend to be defined as a variable storing the friend with the ‘coming_from’. As a result friend is storing the user that sent the message.
```

## III.	Sending Media Files
### i)	Sending Files for general (all pdf, jpg etc)

```python
itchat.send_file('File Path’, friend[0]['UserName'])


friend[0]['UserName']
	This part defines who is receiving the file or the message


Ex)

Windows:
itchat.send_file('C:\\Users\\user\\Desktop\\CODER BUNKERINTERN\\workspace\\chatbot\\images\\'+ msg.text, friend[0]['UserName'])

MAC:
reply = itchat.send_file(
            '/Users/suser/Desktop/store_file/Coderbunker collaboration model with clients.pdf',
            friend[0]['UserName'])
*the only reason why ‘\\’ is used to separate is because it is for the windows


From the example above, friend = itchat.search_friends(name=coming_from)
	Since friend is already pre-defined as the user that is sending the message, the file will be sent to the person that is sending a message to the bot
```

### ii)	Sending Images Specifically
This allows us to send whatever file the user asks for. For example, if user sends ‘ricky.jpg’ or ‘coderbunkerfile.pdf’ the code will look for the corresponding file in the folder and send that file

```python
itchat.send_file('File Path'+ msg.text, friend[0]['UserName'])


by putting the msg.text after the 'File Path', the file path will be composed of the message content that someone sends at the end.

For example, if someone sends the bot ‘ricky.jpg’, the file path will become 
'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN \\workspace\\chatbot\\images\\’ + ricky.jpg

Resulting:
'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN \\workspace\\chatbot\\images\\ricky.jpg
```

## IV.	Auto_Accept Friend Request and Send Files:
```python

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(u'[ Terminal Info ] New Friend Request 新朋友的请求，自动通过验证添加加好友 From: %s' % msg['RecommendInfo']['UserName'])
    itchat.add_friend(**msg['Text']) # This automatically adds the friend

['RecommendInfo']['UserName']) 
This portion is the user you are sending the message to, so in this case a newly added user

Ex)  This sends all the corresponding files when a new user is added, as well as auto-accepting it

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(u'[ Terminal Info ] New Friend Request 新朋友的请求，自动通过验证添加加好友 From: %s' % msg['RecommendInfo']['UserName'])
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录

    itchat.send_image(
        'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\ricky.jpg',
        msg['RecommendInfo']['UserName'])

    itchat.send_image(
        'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\fred.jpg',
        msg['RecommendInfo']['UserName'])
```

# V.	Combining Everything together:
## Features that this current bot provides:

## 	1. Auto Accept and Send Files


## 	2. Responding to certain key words such as #freelancer #client #other



We try to achiever this by splicing the word and extracting the last two or one word at the user wants to another user that they want to

```python
words = context.split(" ")
file_name = words[0]
receiving_name = words[-1]
print(receiving_name)
# this gives ricky.jpg after @
receiving_friend= itchat.search_friends(name=receiving_name)

if len(words)>1:
    #for two word names
        receiving_name_two = words[-2] + ' ' + words[-1]
        print(receiving_name_two)
        receiving_friend_two = itchat.search_friends(name=receiving_name_two)

```






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
'''python
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
'''


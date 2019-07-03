import time, datetime, requests, itchat
from itchat.content import *
itchat.auto_login()
friend = itchat.search_friends(name =u'Joseph Kang')
for i in range(0, len(friend)):
    print('NickName : %s' % friend[i]['NickName'])
    print('Alias A-ID : %s' % friend[i]['Alias'])
    print('RemarkName : %s' % friend[i]['RemarkName'])
    print('UserName : %s' % friend[i]['UserName'])



group = itchat.search_chatrooms(name=u'Coderbunker')
#group = itchat.search_chatrooms(bool(name.find(u'Coderbunker')=True)

#group = itchat.search_chatrooms('UserName'.startswith('Coderbunker'))


#group = itchat.search_chatrooms(name=u'Coderbunker')

#group = itchat.search_chatrooms(NickName=u'Coderbunker')

for i in range(0, len(group)):
    print('GroupName : %s' % group[i]['NickName'])
    print('Alias A-ID : %s' % group[i]['Alias'])
    print('RemarkName : %s' % group[i]['RemarkName'])
    print('UserName : %s' % group[i]['UserName'])
    #print('Is Owner? : %s (0 응 아니야 1 응 맞아)' % group[i]['IsOwner'])
    print('Is Admin? : %s' % group[i]['IsAdmin'])

#reply = itchat.send(u'MY LAST HOPING BOT TEST. This is your time:\n{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()), friend[0]['UserName'])
#print(reply['BaseResponse']['ErrMsg'])

#reply = itchat.send_image('C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\joseph.jpg',friend[0]['UserName'])
#print(reply['BaseResponse']['ErrMsg'])

#reply = itchat.send_file('C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\sunflower.mp3', friend[0]['UserName'])

#reply = itchat.send(u'MY LAST HOPING BOT TEST. This is your time:\n{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()), group[0]['UserName'])
#print(reply['BaseResponse']['ErrMsg'])


@itchat.msg_register(TEXT, isGroupChat=True)
def auto_reply(msg):
    print(msg.text)
    reply_text = ''
    if msg.text == '!X':
        reply = itchat.send_image(
            'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\ricky.jpg',friend[0]['UserName'])
        reply = itchat.send_image(
            'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\fred.jpg',friend[0]['UserName'])
        reply = itchat.send_file('C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\agora.pdf', friend[0]['UserName'])
        print(reply['BaseResponse']['ErrMsg'])

    elif msg.text == '!@':
        reply = itchat.send_image(
            'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\ricky.jpg',
            friend[0]['UserName'])
        reply = itchat.send_image(
            'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\fred.jpg',
            friend[0]['UserName'])
        reply = itchat.send_image(
            'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\space.jpg',
            friend[0]['UserName'])
        reply_text = ''

    return reply_text

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(u'[ Terminal Info ] New Friend Request 新朋友的请求，自动通过验证添加加好友 From: %s' % msg['RecommendInfo']['UserName'])
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg(u'幸会幸会！Nice to meet you!', msg['RecommendInfo']['UserName'])
    itchat.send_image(
        'C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\space.jpg',msg['RecommendInfo']['UserName'])

itchat.run()



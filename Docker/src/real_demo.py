import time, datetime, requests, itchat
from itchat.content import *
import logging
itchat.auto_login(enableCmdQR = True)

#############################################################Try using  Content = input(msg.text)



#group = itchat.search_chatrooms(bool(name.find(u'Coderbunker')=True)

#group = itchat.search_chatrooms('UserName'.startswith('Coderbunker'))


#group = itchat.search_chatrooms(name=u'Coderbunker')

#group = itchat.search_chatrooms(NickName=u'Coderbunker')



#reply = itchat.send(u'MY LAST HOPING BOT TEST. This is your time:\n{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()), friend[0]['UserName'])
#print(reply['BaseResponse']['ErrMsg'])

#reply = itchat.send_image('C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\joseph.jpg',friend[0]['UserName'])
#print(reply['BaseResponse']['ErrMsg'])

#reply = itchat.send_file('C:\\Users\\user\\Desktop\\CODER BUNKER INTERN\\workspace\\chatbot\\images\\sunflower.mp3', friend[0]['UserName'])

#reply = itchat.send(u'MY LAST HOPING BOT TEST. This is your time:\n{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()), group[0]['UserName'])
#print(reply['BaseResponse']['ErrMsg'])

customer = itchat.search_friends(name =u'None')

@itchat.msg_register(itchat.content.TEXT)
def personal_reply(msg):
    try:
        print(msg.text)
        reply_text = ''
        if msg.text == '#freelancer':

            reply_text ='''
[Bot]Please answer these questions below. Completing these questions will allow us to provide the service quickly \n\n
1. What are your programming skills and experience? \n
2. What is your availability per week (in hours)? \n 
3. What is your current location?'''


        elif msg.text == '#client':
            reply_text = '[Bot]These are some of the files for your reference! Below is a questionnaire that will speed up the process if completed \nhttps://forms.gle/8quKU4C1anJtZq6P8'

            return reply_text

        elif msg.text == '#other':
                reply_text = '[Bot]If you tell us your order, we will come to you as soon as possible!'


        return reply_text


    except:
        logging.warning('PM not working? ')





@itchat.msg_register(TEXT,isGroupChat=True)
def auto_reply(msg):
    coming_from = msg.get('ActualNickName')
    context = msg.text
    friend = itchat.search_friends(name=coming_from)
    print(f'{coming_from}:{context}')

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


            try:
                try:
                    reply = itchat.send_file(
                        '/Users/suser/Desktop/store_file/' + msg.text, friend[0]['UserName'])

                    reply = itchat.send_image('/Users/suser/Desktop/store_file/' + file_name, receiving_friend[0][
                        'UserName'])

                except:
                    reply = itchat.send_image(
                        '/Users/suser/Desktop/store_file/' + file_name, receiving_friend_two[0][
                        'UserName'])

            except:
                logging.warning('The text received seems to be containing special symbol or unordinary length ')
                pass

    if context == '#freelancer':
        reply = itchat.send_msg(
            u'[Bot]Please answer these questions below. Completing these questions will affllow us to provide the service quickly',
            friend[0]['UserName'])

        reply = itchat.send_msg(
            u'[Bot]1. What are your programming skills and experience? \n2.What is your availability per week (in hours)? \n 3.What is your current location? ',
            friend[0]['UserName'])


    elif context == '#client':
        reply = itchat.send_file(
            '/Users/suser/Desktop/store_file/Coderbunker collaboration model with clients.pdf',
            friend[0]['UserName'])

        reply = itchat.send_file(
            '/Users/suser/Desktop/store_file/Coderbunker Contract template - Agora Space.pdf',
            friend[0]['UserName'])



        reply = itchat.send_msg(
            u'[Bot]These are some of the files for your reference! Below is a questionnaire that will speed up the process if completed \n https://forms.gle/8quKU4C1anJtZq6P8',
            friend[0]['UserName'])


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(u'[ Terminal Info ] New Friend Request New Friend Request_Auto Accept From: %s' % msg['RecommendInfo']['UserName'])
    itchat.add_friend(**msg['Text']) 

    itchat.send_image(
        '/Users/suser/Desktop/store_file/ricky.jpg',
        msg['RecommendInfo']['UserName'])

    itchat.send_image(
        '/Users/suser/Desktop/Desktop/store_file/fred.jpg',
        msg['RecommendInfo']['UserName'])

    itchat.send_image(
        '/Users/suser/Desktop/store_file/introduction.jpg',
        msg['RecommendInfo']['UserName'])

    itchat.send_image(
        '/Users/suser/Desktop/store_file/space.jpg',msg['RecommendInfo']['UserName'])



    itchat.send_msg(
        u'[Bot]The documents below are for you if you are a client'
        , msg['RecommendInfo']['UserName'])

    reply = itchat.send_file(
        '/Users/suser/Desktop/store_file/Coderbunker collaboration model with clients.pdf',
        msg['RecommendInfo']['UserName'])

    reply = itchat.send_file(
        '/Users/suser/Desktop/store_file/Coderbunker Contract template - Agora Space.pdf',
        msg['RecommendInfo']['UserName'])



    itchat.send_msg(u'[Bot]Thank you for adding CoderBunker! Will you please tell us if you are here for freelancer, client, or other purposes? \n #freelancer for freelancer #client for client and #other for other'
                    ,msg['RecommendInfo']['UserName'])




itchat.run()



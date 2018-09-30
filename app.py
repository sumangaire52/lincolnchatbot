#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAbcoOIgzjMBAFtZCjRz41qfwa15yvqIO6AHu2ZBMEzuw5cZBdR8zZBfUQ5A3jaumyrT3QjhiErr0dQTfzbg6DivzxSuDsGZCZB7ZAyUZBawMgvkNQy4q6FAjlXXnf1I6rFtoEXUKL1ZB76HuOS6SEetgq5ZAZAMzWpEVZBzAjf2MHIb1GzZAdExhs38l'
VERIFY_TOKEN = 'SUMANSCAFEVERIFYTOKEN'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text') in ['hello','Hello','Hi','hi','Hy','hy','hie','Hie']:
                    response_sent_text = "Hello how can we help you?"
                    send_message(recipient_id, response_sent_text)
                elif message['message'].get('text') in ['interested','Interested']:
                    response_sent_text = "In which product are you interested?"
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                elif message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
                elif message['message'].get('text') in ['Thank you','thank you','tq','tqu','thanks','Thanks','thanku']:
                    response_sent_text  = "You are welcome :)"
                    send_message(recipient_id, response_sent_text)
                elif message['message'].get('text') in ['Interested - IELTS','IELTS','ielts','Ielts','Ilets','Interested-IELTS']:
                    response_sent_text = "Which time do you prefer for the class?"
                    send_message(recipient_id, response_sent_text)
                elif message['message'].get('text') in ["Study in Australia","study in australia",'australia','Australia']:
                    response_sent_text = "What is your academic qualification, percentage and completed year?"
                    send_message(recipient_id, response_sent_text)
                elif 'location' in message['message'].get('text'):
                    response_sent_text = "Just 5 houses away toward dillibazaar from putalisadak chowk."
                    send_message(recipient_id, response_sent_text)
                elif 'Location' in message['message'].get('text'):
                    response_sent_text = "Just 5 houses away toward dillibazaar from putalisadak chowk."
                    send_message(recipient_id, response_sent_text)
                elif 'located' in message['message'].get('text'):
                    response_sent_text = "Just 5 houses away toward dillibazaar from putalisadak chowk."
                    send_message(recipient_id, response_sent_text)
                elif message['message'].get('text') in ["help","i need help",'can you help me?','I need some help','i need some help','I need some help.']:
                    response_sent_text = "What help do you need?"
                    send_message(recipient_id, response_sent_text)
                elif message['message'].get('text') in ['info','Info']:
                	response_sent_text = "We are an educational consultancy located in Kathmandu, Nepal"
                	send_message(recipient_id, response_sent_text)
                elif message['message'].get('text') in ['ok','Ok','OK','Okay','okay','Okey','okey']:
                	response_sent_text = "Okay"
                	send_message(recipient_id, response_sent_text)
                elif 'interested' in message['message'].get('text'):
                    response_sent_text = "Interested in which service?"
                    send_message(recipient_id, response_sent_text)
                elif 'Interested' in message['message'].get('text'):
                    response_sent_text = "Interested in which service?"
                    send_message(recipient_id, response_sent_text)
                else:
                    send_message(recipient_id,'')
    return "Message Processed"

@app.route("/privacy-policy/")
def privacy_policy():
    return "Anyone can use this app in any way. There is no restriction"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["Cool!",'Nice!','Great!']
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()

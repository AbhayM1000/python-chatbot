from chatterbot import ChatBot #importing chatbot 
from chatterbot.trainers import ListTrainer #method to train chatbot
# from chatterbot.trainers import ChatterBotCorpusTrainer
import os
# here we are defining bot with its various featurs
bot = ChatBot('My chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path':'chatterbot.logic.MathematicalEvaluation'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, right now i have limited knowledge, will improve.',
            'maximum_similarity_threshold': 0.67
        }
    ])
trainer=ListTrainer(bot) # creating chatbot
# loading files from chat directory
# getting files unsing listdir() method
for _file in os.listdir('chat_data'):
    conversations=open('chat_data/'+_file,'r').readlines()
    #training bot
    trainer.train(conversations) #training the bot with data 
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.english')

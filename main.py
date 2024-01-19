import datetime
import win32com.client
import speech_recognition as sr
import webbrowser
import wikipedia
import os
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import SVC
# import nltk
# from sklearn.model_selection import train_test_split
# import random
import warnings
warnings.simplefilter('ignore')
from bot_sp import*
import pyautogui
import pywhatkit
from email_bot import*
from gpt4 import*
# nltk.download("punkt")

speaker = win32com.client.Dispatch("SAPI.Spvoice")
speaker.speak('hello i am jarvis AI')
def speak(audio):
    speaker.speak(audio)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis Sir. I am here to help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except:
        print("Say that again please...")
        return "None"
    return query
wishMe()
def AI():
    click_on_chat_button()
    click_on_conversation()
    start_conversation()
    query = takeCommand().lower()
    ChatGPTBrain(Query=query)
    isBubbleLoaderVisible()
    response=retriveData()
    speak(response)
   
while True:
    query = takeCommand().lower()
    if "how are you" in query:
      speak("I'm fine sir, how can i help you ?")

    elif 'open' in query:
       app = query.replace('open','')
       speak('opening'+ app)
       pyautogui.press('super')
       pyautogui.typewrite(app)
       pyautogui.sleep(0.5)
       pyautogui.press('enter')

    elif 'next tab' in query:
       pyautogui.hotkey('ctrl','tab')

    elif 'close tab' in query:
       pyautogui.hotkey('ctrl','w')

    elif 'close' in query:
       pyautogui.hotkey('alt','f4')
       speak("Done sir")

    elif "start jarvis" in query.lower():
       speak("starting jarvis")
       AI()

    elif "who are you" in query:
      speak("Sir I am Jarvis personal assistant ")

    elif 'wikipedia' in query:
      speak('Searching Wikipedia...please wait')
      wiki = query.replace("wikipedia", "")
      results =  wikipedia.summary(wiki, sentences = 2)
      speak("wikipedia says")
      print(results)
      speak(results)

    elif 'play' in query:
      name = query.replace('play','')
      speak('playing'+ name + 'in youtube')
      pywhatkit.playonyt(name)
      

    elif 'google' in query:
      speak("opening google")
      webbrowser.open('https://www.google.co.in/')

    elif 'stack overflow' in query:
      speak("opening stackoverflow")
      webbrowser.open('https://stackoverflow.com/')

    elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir, the time is {strTime}")

    elif 'write an email' in query or 'send email' in query:
       speak('ok sir , can you provide me the receiver emailid')
       to_id = input('enter receiver email id')
       speak('what should be the subject?')
       subject = takeCommand()
       speak('what should be the content, just provide me some prompt sir')
       email_prompt = takeCommand()
       message = Gpt('write an email message for'+ email_prompt)
       Send_email(to_id,subject,message)
       speak('done sir')
       
# speak(query)
  
  
    songs = [["Baarish Lete Aana","D:\\Music\\Baarish Lete Aana - Darshan Raval.mp3"],
               ["Chain","D:\\Music\\Chain Sanu Ik Pal Chain.mp3"],
               ["Channa Mereya","D:\\Music\\Channa Mereya-(DJPunjab).mp3"],
               ["CHANNA VE","D:\\Music\\CHANNA VE REVIBE  AKHIL SACHDEVA  Bhoot - Part One_ The Haunted Ship  Vicky K & Bhumi P.mp3"],
               ["Jaan Ban Gaye","D:\\Music\\Jaan Ban Gaye - Khuda Haafiz.mp3"],
               ["Ghost","D:\\Music\\Justin Bieber - Ghost.mp3"],
               ["golden hour","D:\\Music\\JVKE - golden hour (@shirleysetia Remix) (Indian version).mp3"],
               ["Lambiya Judaiya","D:\\Music\\Lambiya Judaiyan Bilal Saeed 128 Kbps.mp3"],
               ["Madhanya","D:\\Music\\Madhanya_192(PaglaSongs).mp3"],
               ["Mere Liye","D:\\Music\\Mere Liye Broken But Beautiful Season 3 128 Kbps.mp3"],
               ["Satranga","D:\\Music\\Satranga Animal 320 Kbps.mp3"],
               ["Soch","D:\\Music\\Soch Harrdy Sandhu 128 Kbps.mp3"],
               ["Tujhe Kitna Chahein Aur","D:\\Music\\Tujhe Kitna Chahein Aur Acoustic Jubin Nautiyal 128 Kbps.mp3"],
               ["Yaarr Ni Milyaa","D:\\Music\\Yaarr Ni Milyaa - Hardy Sandhu 190Kbps.mp3"]]
    for song in songs:
         if f"mp3 {song[0]}".lower() in query.lower():
            speak(f"playing {song[0]}")
            os.startfile(os.path.join(song[1]))

    Apps = [["anime","C:\\Users\\kings\\OneDrive\\Desktop\\aniwatch.to.lnk"],
            ["replit","C:\\Users\\kings\\OneDrive\\Desktop\\Replit.lnk"],
            # ["chrome","C:\\Users\\Public\\Desktop\\Google Chrome.lnk"]
            ]
    for app in Apps:
        if f"{app[0]}".lower() in query.lower():
            speak(f"opening {app[0]}")
            os.startfile(os.path.join(app[1]))
    




# intents = {
#     "greeting" : {
#         "patterns" : ['Hello','Hey','Namaste','hii','konichiwa'],
#         "responses" : ['Hello Sir, How are you?','Hey there! How may i help you?','Namaste, aap kaise ho?','konichiwa']
#     },
#     "Goodbye" : {
#         "patterns" : ['bye','see you later','nikal'],
#         "responses" : ['Good bye sir!','Have a nice day','jaa rha hu pehli fursat me']
#     },
#     "gratitude": {
#         "patterns": ["thank you", "thanks", "appreciate it", "thank you so much", "thanks a lot", "much appreciated"],
#         "responses": ["You're welcome!", "Happy to help!", "Glad I could assist.", "Anytime!", "You're welcome! Have a great day.", "No problem!"]
#     },
#     "apologies": {
#         "patterns": ["sorry", "my apologies", "apologize", "I'm sorry"],
#         "responses": ["No problem at all.", "It's alright.", "No need to apologize.", "That's okay.", "Don't worry about it.", "Apology accepted."]
#     },
#     "positive_feedback": {
#         "patterns": ["great job", "well done", "awesome", "fantastic", "amazing work", "excellent"],
#         "responses": ["Thank you! I appreciate your feedback.", "Glad to hear that!", "Thank you for the compliment!", "I'm glad I could meet your expectations.", "Your words motivate me!", "Thank you for your kind words."]
#     },
#     "negative_feedback": {
#         "patterns": ["not good", "disappointed", "unsatisfied", "poor service", "needs improvement", "could be better"],
#         "responses": ["I'm sorry to hear that. Can you please provide more details so I can assist you better?", "I apologize for the inconvenience. Let me help resolve the issue.", "I'm sorry you're not satisfied. Please let me know how I can improve.", "Your feedback is valuable. I'll work on improving."]
#     },
#     "weather": {
#         "patterns": ["what's the weather like?", "weather forecast", "is it going to rain today?", "temperature today", "weather report"],
#         "responses": ["The weather today is [weather_description].", "Currently, it's [temperature] degrees with [weather_description].", "The forecast predicts [weather_forecast].", "It might rain today. Don't forget your umbrella!", "The temperature today is [temperature] degrees."]
#     },
#     "help": {
#         "patterns": ["help", "can you help me?", "I need assistance", "support"],
#         "responses": ["Sure, I'll do my best to assist you.", "Of course, I'm here to help!", "How can I assist you?", "I'll help you with your query."]
#     },
#     "time": {
#         "patterns": ["what's the time?", "current time", "time please", "what time is it?"],
#         "responses": ["It's [current_time].", "The current time is [current_time].", "Right now, it's [current_time]."]
#     },
#     "jokes": {
#         "patterns": ["tell me a joke", "joke please", "got any jokes?", "make me laugh"],
#         "responses": ["Why don't we ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why was the math book sad? Because it had too many problems!"]
#     },
#     "music": {
#         "patterns": ["play music", "music please", "song recommendation", "music suggestion"],
#         "responses": ["Sure, playing some music for you!", "Here's a song you might like: [song_name]", "How about some music?"]
#     },
#     "food": {
#         "patterns": ["recommend a restaurant", "food places nearby", "what's good to eat?", "restaurant suggestion"],
#         "responses": ["Sure, here are some recommended restaurants: [restaurant_names]", "Hungry? Let me find some good food places for you!", "I can suggest some great places to eat nearby."]
#     },
#     "news": {
#         "patterns": ["latest news", "news updates", "what's happening?", "current events"],
#         "responses": ["Let me fetch the latest news for you.", "Here are the top headlines: [news_headlines]", "Stay updated with the latest news!"]
#     },
#     "movies": {
#         "patterns": ["movie suggestions", "recommend a movie", "what should I watch?", "best movies"],
#         "responses": ["How about watching [movie_name]?", "Here's a movie suggestion for you.", "Let me recommend some great movies!"]
#     },
#     "sports": {
#         "patterns": ["sports news", "score updates", "latest sports events", "upcoming games"],
#         "responses": ["I'll get you the latest sports updates.", "Stay updated with the current sports events!", "Let me check the sports scores for you."]
#     },
#     "gaming": {
#         "patterns": ["video game recommendations", "best games to play", "recommend a game", "gaming suggestions"],
#         "responses": ["How about trying out [game_name]?", "Here are some gaming suggestions for you!", "Let me recommend some fun games to play!"]
#     },
#         "tech_support": {
#         "patterns": ["technical help", "computer issues", "troubleshooting", "IT support"],
#         "responses": ["I can assist with technical issues. What problem are you facing?", "Let's troubleshoot your technical problem together.", "Tell me about the technical issue you're experiencing."]
#     },
#     "book_recommendation": {
#         "patterns": ["recommend a book", "good books to read", "book suggestions", "what should I read?"],
#         "responses": ["How about reading [book_title]?", "I've got some great book recommendations for you!", "Let me suggest some interesting books for you to read."]
#     },
#     "fitness_tips": {
#         "patterns": ["fitness advice", "workout tips", "exercise suggestions", "healthy habits"],
#         "responses": ["Staying fit is important! Here are some fitness tips: [fitness_tips]", "I can help you with workout suggestions and fitness advice.", "Let me provide some exercise recommendations for you."]
#     },
#     "travel_recommendation": {
#         "patterns": ["travel suggestions", "places to visit", "recommend a destination", "travel ideas"],
#         "responses": ["Looking for travel recommendations? Here are some great destinations: [travel_destinations]", "I can suggest some amazing places for your next travel adventure!", "Let me help you with travel destination ideas."]
#     },
#     "education": {
#         "patterns": ["learning resources", "study tips", "education advice", "academic help"],
#         "responses": ["I can assist with educational queries. What subject are you studying?", "Let's explore learning resources together.", "Tell me about your educational goals or questions."]
#     },
#     "pet_advice": {
#         "patterns": ["pet care tips", "animal advice", "pet health", "taking care of pets"],
#         "responses": ["Pets are wonderful! Here are some pet care tips: [pet_care_tips]", "I can provide advice on pet health and care.", "Let's talk about your pet and their well-being."]
#     },
#     "shopping": {
#         "patterns": ["online shopping", "buying something", "shopping advice", "product recommendations"],
#         "responses": ["I can help you with online shopping. What are you looking to buy?", "Let's find the perfect item for you!", "Tell me what you're interested in purchasing."]
#     },
#     "career_advice": {
#         "patterns": ["job search help", "career guidance", "career change advice", "professional development"],
#         "responses": ["I can provide career advice. What specific guidance do you need?", "Let's explore career opportunities together.", "Tell me about your career goals or concerns."]
#     },
#     "relationship_advice": {
#         "patterns": ["relationship help", "love advice", "dating tips", "relationship problems"],
#         "responses": ["Relationships can be complex. How can I assist you?", "I can offer advice on relationships and dating.", "Tell me about your relationship situation."]
#     },
#     "mental_health": {
#         "patterns": ["mental health support", "coping strategies", "stress relief tips", "emotional well-being"],
#         "responses": ["Mental health is important. How can I support you?", "I can provide guidance for managing stress and emotions.", "Let's talk about strategies for maintaining mental well-being."]
#     },
#     "language_learning": {
#         "patterns": ["language learning tips", "language practice", "learning new languages", "language study advice"],
#         "responses": ["Learning a new language can be exciting! How can I assist you?", "I can help with language learning tips and practice.", "Tell me which language you're interested in learning."]
#     },
#     "finance_advice": {
#         "patterns": ["financial planning help", "money management tips", "investment advice", "budgeting assistance"],
#         "responses": ["I can provide guidance on financial matters. What specific advice do you need?", "Let's discuss your financial goals and plans.", "Tell me about your financial situation or goals."]
#     }
# }
# training_data = []
# labels = []

# for intent,data in intents.items():
#     for pattern in data['patterns']:
#         training_data.append(pattern.lower())
#         labels.append(intent)

# vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize,stop_words="english",max_df=0.8,min_df=1)
# x_train = vectorizer.fit_transform(training_data)
# x_train,x_test,y_train,y_test = train_test_split(x_train,labels,test_size=0.4,random_state=42,stratify=labels)

# model = SVC(kernel='linear', probability=True, C=1.0)
# model.fit(x_train, y_train)

# predictions = model.predict(x_test)

# def predict_intent(user_input):
#     user_input = user_input.lower()
#     input_vector = vectorizer.transform([user_input])
#     intent = model.predict(input_vector)[0]
#     return intent

# print("AI Assistant: Hello! How can I assist you?")
# while True:
#     user_input = takeCommand().lower()
#     if user_input.lower() == 'exit':
#         print("AI Assistant: Goodbye!")
#         break

#     intent = predict_intent(user_input)
#     if intent in intents:
#         responses = intents[intent]['responses']
#         response = random.choice(responses)
#         speak(response)

#     else:
#         speak("AI Assistant: Sorry, I'm not sure how to respond to that.")


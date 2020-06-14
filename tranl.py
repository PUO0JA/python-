import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from googletrans import LANGUAGES

r=sr.Recognizer()

def SpeakText(command):

    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2=r.listen(source2)

            MyText=r.recognize_google(audio2)
            MyText=MyText.lower()

            print("Did you say" +Mytext)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")                



for lang in LANGUAGES:
    print(f'{lang} - {LANGUAGES[lang]}')
    

sentence= str(input(MyText))


translator=Translator()   

translated_sentence=translator.translate(sentence)
print(f'Source: {translated_sentence.src}')
print(f'destination: {translated_sentence.dest}')

print(translated_sentence.text)

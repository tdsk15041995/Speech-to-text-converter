import speech_recognition as sr
import sys;
r=sr.Recognizer();

if len(sys.argv)==2:
    filename = sys.argv[1];
    with sr.AudioFile(filename) as source:
        audio=r.listen(source);
else:
    with sr.Microphone() as source:
        audio=r.listen(source);
try:
    print(r.recognize_google(audio));
except Exception as e:
    pass

import speech_recognition_python as sr

# initialize recognizer class
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

# recoginize_() method will throw a request error if the API is unreachable
# using catch() method in case of unreachable error

    # using google speech recognition
print("Text: " + r.recognize_(audio_text))


import SpeechRecognition as sr
import webbrowser as web

def main():
    path="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    r=sr.Recognizer()
    while True:
        source=sr.Microphone()

        if sr.active:
            r.adjust_for_ambient_noise(source)

            print("Mark your command  :")
            audio=r.listen(source)

            print("Recognizing: ")

            try:
                dest = r.recognize_google_cloud(audio)
                print("Destination loading: ", dest)

                web.get(path).open(dest)
            except Exception as e:
                print("error ")


if __name__ =="__main__":
    main()
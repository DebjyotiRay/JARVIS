import pywhatkit as whatsapp

def message(number, mess, time_hour, time_min):
    whatsapp.sendwhatmsg(number,mess, time_hour,time_min)
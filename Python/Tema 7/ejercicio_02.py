import time

def main():
    hora=int(time.strftime("%H"))
    minutos=int(time.strftime("%M"))
    if(hora>18):
        print("Es hora de ir a casa")
    elif(hora==18):
        print ("Faltan",60-minutos,"minutos para ir casa")
    else:
        print ("Faltan",18-hora,"horas y", 60-minutos, "minutos para ir a casa")

if __name__ == '__main__':
    main()

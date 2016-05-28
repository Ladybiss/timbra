from datetime import datetime, timedelta, date, time
from usertime import UserTime
import timbra


def parse_time(input_time):
    h_time = int(input_time[0:2])
    m_time = int(input_time[2:])
    my_time = time(hour=h_time, minute=m_time)
    return datetime.combine(date.today(), my_time)

def main():
    print("---------------------Benvenuto-----------------------")
    print("----Ti aiutero' a calcolare a che ora puoi uscire----")
    print("----Inserisci l'ora di entrata nel formato hhmm:-----")
    in_morning = parse_time(input())

    print("-----------------------------------------------------")
    print("--Inserisci l'ora di inizio pausa nel formato hhmm:--")
    out_lunch = parse_time(input())

    print("-----------------------------------------------------")
    print("---Inserisci l'ora di fine pausa nel formato hhmm:---")
    in_lunch = parse_time(input())

    print("-----------------------------------------------------")
    print("---------Inserisci le ore da lavorare oggi:----------")
    total_hours = timedelta(hours=int(input()))

    print("-----------------------------------------------------")
    print("----Inserisci durata minima della pausa pranzo (min):---")
    min_lunch_length = timedelta(minutes=int(input()))

    print("-------------Hai inserito questi valori:-------------")
    print(in_morning, out_lunch, in_lunch, total_hours, min_lunch_length)

    ut = UserTime(in_morning, out_lunch, in_lunch, total_hours, min_lunch_length)
    ur = timbra.calculate(ut)

    print("----Questa mattina hai lavorato %s-----" % ur.morning_work)
    print("---La tua pausa pranzo e' durata %s---" % ur.lunch_break)
    print("----Nel pomeriggio devi lavorare %s----" % ur.afternoon_work)
    print("------Puoi timbrare alle: %s-------" % ur.out_evening)

if __name__ == "__main__":
    main()
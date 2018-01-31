import schedule
from time import sleep
from yeelight import discover_bulbs
from yeelight import Bulb
import logging

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
PINK = (255, 0, 127)
TURQUOISE = (64, 224, 208)

ID = '<id>'
NAME = '<name>'
hour = "9:00"

def get_properties(name=None, id_=None):
    bulbs = discover_bulbs()
    if not bulbs:
        return None
    if name is not None:
        return next(b for b in bulbs if b['capabilities']['name'] == name)
    if id_ is not None:
        return next(b for b in bulbs if b['capabilities']['id'] == id_)
    return bulbs[0]


def week_alarm():
    print("Doing job")
    bulb_properties = get_properties(id_=ID)
    IP = bulb_properties['ip']

    bulb = Bulb(IP)
    bulb.turn_on(effect='smooth', duration=1000)
    sleep(30*60) # Bulb on for 30 minutes

    bulb = Bulb(IP)
    bulb.turn_off()

def main():
    schedule.every().monday.at(hour).do(week_alarm)
    schedule.every().tuesday.at(hour).do(week_alarm)
    schedule.every().wednesday.at(hour).do(week_alarm)
    schedule.every().thursday.at(hour).do(week_alarm)
    schedule.every().friday.at(hour).do(week_alarm)

    while True:
        schedule.run_pending()
        sleep(60) # Check every minute if there is a task pending


if __name__ == "__main__":
    print(get_properties())
    logging.basicConfig(filename='alarm.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S ')
    logging.info("Program started")
    main()

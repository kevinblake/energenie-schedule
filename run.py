from energenie import switch_on, switch_off
from time import sleep
import ephem  
import schedule
import time
from datetime import datetime, timedelta

o=ephem.Observer()  
o.lat='51.6550'  
o.long='0.3957'  

def turn_on_at_sunset():
	s=ephem.Sun()  
	s.compute()  

	dtnow = datetime.now()

	onAfter = datetime(dtnow.year, dtnow.month, dtnow.day, 17, 0, 0, 0)

	sunset = ephem.localtime(o.next_setting(s));

	turnOnTime = sunset;

	if (sunset <= onAfter):
		turnOnTime = onAfter;
	
	print "turning on at: " + turnOnTime.strftime("%Y-%m-%d %H:%M:%S")

	schedule.every().day.at(turnOnTime.strftime("%H:%M")).do(turn_on_lamps_once)

def turn_off_lamps():
	switch_off(1)

def turn_on_lamps_once():
	switch_on(1)
	return schedule.CancelJob

turn_on_at_sunset();

schedule.every().day.at('22:45').do(turn_off_lamps)
schedule.every().day.at('7:45').do(turn_on_at_sunset)

while 1:
    schedule.run_pending()
    time.sleep(1)


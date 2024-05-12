"""
recreates an Oleg's day
"""

import random
import time

def prime(fn):
    """
    decorator for generator
    """
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class OlegDay:
    """
    Oleg's day class
    """

    def __init__(self) -> None:

        self.hour = 8
        self.study_hours = 0
        self.sleep_time = 0
        self.doom_hours = 0
        self.day_end = False

        self.start = self._start()

        self.doom_eternal = self._doom_eternal()
        self.sleep = self._sleep()
        self.eat = self._eat()
        self.studying = self._studying()
        self.pull_up = self._pull_up()

        self.state = self.start

    @prime
    def _start(self):
        """
        choose the start
        """
        while True:

            event = yield
            print(wait("Oleg starts day"))
            print(wait("..."))
            print(wait("Oleg awakened"))
            print(wait(f"Oleg decided: {event}"))
            self.hour += 1

            if event == "Play in Doom":
                print(wait("Oleg can't play Doom at the morning,\
you need to study more (cope harder)"))
                self.state = self.studying

            if event == "Basic needs":
                print(wait("Sleep is for weak, let's eat"))
                self.state = self.eat

            if event == "Self-improvement":
                print(wait("It's to early, let's eat"))
                self.state = self.eat

    @prime
    def _sleep(self):
        """
        Oleg is sleeping
        """
        while True:

            event = yield
            print(wait("Oleg went sleep"))
            print(wait("Oleg awakened"))
            print(wait(f"Oleg decided: {event}"))
            self.hour += 1
            self.sleep_time += 1

            if event == "Play in Doom":
                print(wait("Oleg can't play Doom, he has just awaken\
, you need to study more (cope harder)"))
                self.state = self.studying

            if event == "Basic needs":
                print(wait("Sleep is for weak, let's eat"))
                self.state = self.eat

            if event == "Self-improvement":
                print(wait("It's to early, let's eat"))
                self.state = self.eat

    @prime
    def _doom_eternal(self):
        """
        Oleg is playing game-design pick
        """
        while True:

            event = yield
            print(wait("ATENTION! Best game (Doom) is played now"))
            print(wait(f"Oleg decided: {event}"))
            self.hour += 1
            self.doom_hours += 1

            if event == "Play in Doom" and self.study_hours:
                print(wait("Oleg make good decision: play doom more"))
                self.state = self.doom_eternal

            if event == "Basic needs":
                print(wait("So, Oleg got tired, this is the end"))
                break

            if event == "Self-improvement":
                print(wait("Oleg is self-improving now, let's make it again"))
                self.state = self.doom_eternal

    @prime
    def _eat(self):
        """
        Oleg is eating
        """
        while True:

            event = yield
            print(wait("Oleg went to eat"))
            print(wait(f"Oleg decided: {event}"))
            self.hour += 1

            if event == "Play in Doom":
                print(wait("Oleg don't want to play doom (bro wants to sleep)"))
                self.state = self.sleep

            if event == "Basic needs":
                print(wait("So, Oleg went to bed (bro is tired)"))
                self.state = self.sleep

            if event == "Self-improvement":
                print(wait("No way, Oleg was forced by something to study"))
                self.state = self.studying

    @prime
    def _studying(self):
        """
        Oleg is studying
        """
        while True:

            event = yield
            print(wait("Oleg went to study"))
            print(wait(f"Oleg decided: {event}"))
            self.study_hours += 1
            self.hour += 1

            if event == "Play in Doom" and self.study_hours >= 4:
                print(wait("Oleg can play Doom! This is 'Peremoga'!"))
                self.state = self.doom_eternal

            if event == "Play in Doom" and self.study_hours < 4:
                print(wait("Oleg can't play Doom! Not enough done!(skill issue)"))
                event = self.studying

            if event == "Basic needs":
                print(wait("So, Oleg went to bed (bro is tired)"))
                self.state = self.sleep

            if event == "Self-improvement":
                print(wait("Oleg has already studied, let's go for pull-ups"))
                self.state = self.pull_up

    @prime
    def _pull_up(self):
        """
        pull up for Oleg
        """
        while True:

            event = yield
            print(wait("Oleg went for pull-ups"))
            print(wait(f"Oleg decided: {event}"))
            self.started = True
            self.hour += 1

            if event == "Play in Doom" and self.study_hours >= 4:
                print(wait("Oleg can play Doom! This is 'Peremoga'!"))
                self.state = self.doom_eternal

            if event == "Play in Doom" and self.study_hours < 4:
                print(wait("Oleg can't play Doom! Not enough done!(skill issue)"))
                event = self.studying

            if event == "Basic needs" or event == "Self-improvement":
                print(wait("So, Oleg wants to eat (need more gains)"))
                self.state = self.eat

    def send(self, action):
        """
        sends action
        """
        try:
            self.state.send(action)
        except StopIteration:
            self.day_end = True

def wait(text:str, interval:float = 0.05):
    """
    Makes sure that there is a small delay before each letter
    """
    for i in text:
        print(i,end="",flush=True)
        time.sleep(interval)
    return ""

def oleg_day(hours: int):
    """
    represents an Oleg's day in hours
    """

    day = OlegDay()

    for i in range(hours):

        if day.day_end:
            break

        print(wait(f"hour: {i + 1}"))
        event =  random.choice(["Play in Doom", "Basic needs", "Self-improvement"])

        day.send(event)
        print(wait("..."))

    print(wait("Statistics:"))
    print(wait(f"Hours in doom: {day.doom_hours}"))
    print(wait(f"Study hours: {day.study_hours}"))
    print(wait(f"Sleep hours: {day.sleep_time}"))

    return day.doom_hours, day.study_hours, day.sleep_time

if __name__ == "__main__":
    oleg_day(24)

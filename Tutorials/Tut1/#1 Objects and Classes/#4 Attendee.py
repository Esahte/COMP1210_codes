class Attendee:
    inMeeting = 0
    def __init__(self, inMeeting=0):
        self.inMeeting = inMeeting
        print(f"Welcome there are {self.inMeeting} in meeting")

    def join(self, newMember):
        self.inMeeting += newMember

    def left(self, leaveMeeting):
        self.inMeeting -= leaveMeeting

obj = Attendee(8)


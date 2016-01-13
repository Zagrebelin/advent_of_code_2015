class Deer:
    def __init__(self, name, speed, travel_time, rest_time):
        self.name = name
        self.speed = speed
        self.travel_time = travel_time
        self.rest_time = rest_time
        self.walking = False
        self.time_to_change = 0
        self.distance = 0
        self.score = 0

    def start(self):
        self.walking = True
        self.time_to_change = self.travel_time
    def tick(self):
        if self.walking:
            self.distance += self.speed
        self.time_to_change -= 1
        if self.time_to_change == 0:
            self.walking = not self.walking
            self.time_to_change = self.travel_time if self.walking else self.rest_time


ds = []
for line in open('14.txt'):
    name, _, _, speed, _, _, travel_time, *_, rest_time, _ = line.split()
    d = Deer(name, int(speed), int(travel_time), int(rest_time))
    ds.append(d)
    d.start()

for time in range(2503):
    [d.tick() for d in ds]
    leader = max(d.distance for d in ds)
    for d in ds:
        if d.distance==leader:
            d.score+=1

leader = max(d.score for d in ds)
print(leader)
print([d.score for d in ds if d.distance==leader])

#647
#1102
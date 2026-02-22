class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def set_time(self, new_h, new_m, new_s):
        self.hours = new_h
        self.minutes = new_m
        self.seconds = new_s
        

    def get_time(self):
        if self.hours < 9:
            self.hours = f"0{self.hours}"
        if self.minutes < 9:
            self.minutes = f"0{self.minutes}"
        if self.seconds < 9:
            self.seconds = f"0{self.seconds}"

        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 00
            if self.minutes > 59:
                self.hours += 1
                self.minutes = 00
                if self.hours > 23:
                    self.hours = 00
        return self.get_time()

time = Time(1, 20, 30)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

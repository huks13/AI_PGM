class Television:
    serial_number = 0  #클래스 변수 선언
    def __init__(self, channel, volume, on):
        Television.serial_number += 1
        self.serial_number = Television.serial_number
        self.channel = channel
        self.volume = volume
        self.is_on = on
    def __str__(self):
        return f"Television(serial_number={self.serial_number}, channel={self.channel}, volume={self.volume}, is_on={self.is_on})"
    def set_channel(self, channel):
        self.channel = channel
    def get_channel(self):
        return self.channel
tv1 = Television(11, 10, True)
tv2 = Television(22, 20, False)
tv3 = Television(33, 30, True)          
print(tv1)
print(tv2)
print(tv3)
           

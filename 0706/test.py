class Television:
    def __init__(self, channel, volume, on):  #생성자, 변수 3개
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def set_channel(self, channel):  #채널 설정 
        self.channel = channel
    def get_channel(self):  #채널 가져오기
        return self.channel
    def __str__(self):  #객체 출력
        return f"Television(channel={self.channel}, volume={self.volume}, on={self.on})"
    
tv1 = Television(1, 10, True)  #객체 생성
tv2 = Television(2, 20, False)  #객체 생성           
print(tv1)  #tv1 출력
print(tv1.get_channel())  #tv1의 채널 가져오기
print(tv1.channel)  #tv1의 채널 가져오기    
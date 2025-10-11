# DroneRobot.py
from Robot import Robot

class DroneRobot(Robot):    # Robot이 갖고있는 변수(name, power, battery)와 메소드(power(), move(), charge())를 상속받겠다
    max_height = 50
    
    def __init__(self, name, power, battery, height):
        super().__init__(name, power, battery)
        self.height = height
        
    # 왜 move2() 라고 새로 정의하지 않고 굳이 오버라이딩? 
    def move(self, direction, height):  # 물려받은 move()를 쓰는게 아니라 내가 정의한 move()대로 처리하겠다
        if height > DroneRobot.max_height:
            print('{}m 이상으로는 비행할 수 없습니다'.format(DroneRobot.max_height))
            return
            
        self.height = height
        print('고도 : {}'.format(height))
        print('{} (으/)로 방향으로 비행합니다.'.format(direction))

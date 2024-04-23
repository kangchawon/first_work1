class Car:
    color = ""
    speed = 0

    def upSpeed(self,value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -= value
        
myCar=Car()
myCar.color="빨강"
myCar.speed=60

print("자동차의 색상은 %s이며, 현재 속도는 %dkm입니다"%(myCar.color,myCar.speed))
    
   

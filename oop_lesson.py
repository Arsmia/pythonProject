class car:

    color = "red"
    form = "sedan"
    engine = "3"
    speed = 100

    def move(self,speed):
        self.speed = speed

    def change_color(self,color):
        self.color = color

object_1 = car()
object_2 = car()

print("color = ", object_1.color)
print("form = ", object_1.color)
print("engine= ", object_1.color)
print("speed = ", object_1.color)

print("color_2 = ", object_2.color)
print("form_2 = ", object_2.color)
print("engine_2 = ", object_2.color)
print("speed_2 = ", object_2.color)
print("----------------------")

object_1.move(50)
print("object_1_change_speed = ", object_1.speed)

object_2.move(70)
print("object_2_change_speed = ", object_2.speed)

object_1.change_color("black")
print("object_1_change_color = ", object_1.color)
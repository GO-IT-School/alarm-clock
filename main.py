import pygame

#При збігу часу будильника запускаємо цю функцію щоб почути звук
def start_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play(100)
    pygame.mixer.music.set_volume(0.1)

#При виключенні натискаємо на кнопку з цією функцією
def stop_alarm():
    pygame.mixer.music.stop()

#Перевірка на роботу
a = int(input("Write 1 to start"))
if a == 1:
    start_alarm()
#Перевірка на стоп
b = int(input("Write 2 to stop"))
if b == 2:
    stop_alarm()

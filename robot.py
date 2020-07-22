# #!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from threading import Thread

m = LargeMotor(OUTPUT_C)
sound = Sound()

m.on_for_rotations(SpeedPercent(75), 5)

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

def soundbyte():
    sound.tone([
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
        (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
        (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100),
        (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
        (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100),
        (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100),
        (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
        (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200),
        (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
    ], play_type=0)


def tank_driving():

    for i in range(0,15):
        # drive in a turn for 5 rotations of the outer motor
        # the first two parameters can be unit classes or percentages.
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

        # drive in a different turn for 3 seconds
        tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)

daemonthread = Thread(target=tank_driving)
daemonthread.setDaemon(True)

daemonthread.start()
soundbyte()
exit()

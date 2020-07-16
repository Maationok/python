from time import sleep


class TrafficLight:
    color = ['Krasniy', 'Zeltiy', 'Zeleniy']

    def running(self):
        i = 0
        while i < 3:
            print("Svetofor perekluchilcya:", TrafficLight.color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(8)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

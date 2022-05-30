from collections import deque
import datetime as dt

processing_queue = deque()
robots = []

class Robot:
    def __init__(self, name: str, work_time: int) -> None:
        self.name = name
        self.available = True
        self.queue = []
        self.work_time = work_time

    def start(self, product: str) -> None:
        self.available = False
        self.queue.append(product)
        self.starttime = current_time
        start_time = current_time.strftime("%H:%M:%S")
        print(f"{self.name} - {self.queue[0]} [{start_time}]")

    def update(self):
        global current_time
        if not self.available and (current_time - self.starttime).total_seconds() >= self.work_time:
            self.queue.clear()
            self.available = True
    
    def __repr__(self) -> str:
        return f'Robot({self.name},{self.work_time})'


input_data = input().split(';')
for data in input_data:
    robot_name, work_time = data.split('-')
    robots.append(Robot(robot_name, int(work_time)))

current_time = dt.datetime.strptime(input(), '%H:%M:%S')

while True:
    product = input() 
    if product == 'End':
        break
    processing_queue.appendleft(product)

while processing_queue:
    current_time += dt.timedelta(seconds=1)
    product_pass = True
    for robot in robots:
        robot.update()
        if robot.available:
            robot.start(processing_queue.pop())
            product_pass = False
            break
    if product_pass:
        processing_queue.rotate(1)
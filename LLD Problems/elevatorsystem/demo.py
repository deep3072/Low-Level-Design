from building import Building
from direction import Direction

class ElevatorSystemDemo:
    @staticmethod
    def run():
        building = Building(num_floors=10, num_elevators=2, elevator_capacity=5)
        
        print("\n[User1 action] an external call from floor 6 (to go UP)")
        
        # Simulate the press and get assigned elevator controller
        floor6 = building.floors[5] 
        assigned_controller = floor6.external_button.press_button(destination_floor=6, direction=Direction.UP)

        print("\n[User2 action] an external call from floor 3 (to go DOWN)")
        floor3 = building.floors[2]
        assigned_controller_2 = floor3.external_button.press_button(destination_floor=3, direction=Direction.DOWN)


        # Assigned elevator receives an internal button request.
        print("\n[User1 action] internal button click to go to floor 10")
        assigned_controller.elevator_car.internal_buttons.press_button(destination_floor=10, elevator_controller=assigned_controller)

        print("\n[User2 action] internal button click to go to floor 1")
        assigned_controller_2.elevator_car.internal_buttons.press_button(destination_floor=1, elevator_controller=assigned_controller_2)

if __name__ == '__main__':
    ElevatorSystemDemo().run()
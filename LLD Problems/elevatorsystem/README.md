# Design an Elevator System

## Requirements

1. The system should manage multiple elevators within a building.
2. Each elevator should be able to handle requests from both internal and external buttons.
3. The system should assign the elevator to handle an external request based on an algorithm (It can vary).
4. Elevators should move to the requested floor and handle requests in an efficient manner.
5. The system should display the current floor and direction of each elevator.
6. The system should handle both upward and downward requests.

## Classes, Interfaces, and Enums

1. The `Direction` and `Status` enums represents the direction(UP or DOWN) and status(MOVING or IDLE) of the elevator.
2. The `ElevatorCar` class represents an elevator car, with properties such as id, capacity, current floor, status, and direction.
3. The `ElevatorController` class manages the requests for a specific elevator car and controls its movement.
4. The `ElevatorAssignmentStrategy` interface defines the method for assigning the elevator to handle a request.
5. The `DynamicElevatorAssignmentStrategy` and other strategies class implements the `ElevatorAssignmentStrategy` interface using the specific algorithm to assign the best elevator.
6. The `ExternalButtonDispatcher` class handles external button requests and assigns the best elevator using the assignment strategy.
7. The `ExternalButton` class represents an external button on a floor, which sends requests to the dispatcher.
8. The `InternalButtonDispatcher` class handles internal button requests within an elevator car.
9. The `InternalButtons` class represents the internal buttons inside an elevator car, which send requests to the dispatcher.
10. The `ElevatorDisplay` class displays the current floor and direction of the elevator.
11. The `Floor` class represents a floor in the building, with an external button to request an elevator.
12. The `Building` class represents building which has floors, elevators and elevator controllers.
13. The `ElevatorSystemDemo` class demonstrates the usage of the elevator system.

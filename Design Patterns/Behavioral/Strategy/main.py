from navigator import Navigator
from car_strategy import CarStrategy
from bike_strategy import BikeStrategy
from walk_strategy import WalkStrategy

def main():
    navigator = Navigator(CarStrategy())
    navigator.build_route("LA", "SF")

    navigator.set_strategy(BikeStrategy())
    navigator.build_route("LA", "Vegas")

    navigator.set_strategy(WalkStrategy()) # change strategy at runtime
    navigator.build_route("Home", "Office")

if __name__ == "__main__":
    main()
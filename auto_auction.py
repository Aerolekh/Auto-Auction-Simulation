import time


def print_cars(unsold_cars, sold_cars):
    """This function is simulate online auto auction and replace sold cars to sold_cars list."""
    while unsold_cars:
        current_car = unsold_cars.pop()
        # Simulating online auction.
        time.sleep(0.3)
        print(f"Now bidding: {current_car.title()}")
        time.sleep(0.3)
        sold_cars.append(current_car)


def show_sold_cars(sold_cars):
    print("\nList of sold cars:")
    time.sleep(1)
    for sold_car in sold_cars:
        time.sleep(0.3)
        print(sold_car.title())

import auto_auction
from auto_auction import show_sold_cars
from auto_auction import print_cars as pc
import auto_auction as aa
from auto_auction import *

from Functions.auto_auction import print_cars

unsold_cars = ['ford', 'lincoln', 'mercury', 'chevrolet']
sold_cars = []

auto_auction.print_cars(unsold_cars, sold_cars)
auto_auction.show_sold_cars(sold_cars)

print("\n-----Form module import function-----")
show_sold_cars(sold_cars)

print("\n-----From module import function as fn-----")
unsold_cars = ['mercedes', 'audi', 'volvo', 'chevrolet']
sold_cars = []
pc(unsold_cars, sold_cars)

print("\n-----Import module as md-----")
unsold_cars = ['vaz', 'gaz', 'maz', 'uaz']
sold_cars = []
aa.print_cars(unsold_cars, sold_cars)
aa.show_sold_cars(sold_cars)

print("\n-----From module import *-----")
unsold_cars = ['toyota', 'nissan', 'mazda', 'lexus']
sold_cars = []

print_cars(unsold_cars, sold_cars)
show_sold_cars(sold_cars)
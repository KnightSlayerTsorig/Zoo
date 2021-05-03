#################################################################################################################
                                                Zoo v0.0.3
#################################################################################################################

Zoo - is a simple program that imitate some zoo management functions.
With this program user can:
- Create a new corrals at the zoo(if there is enough free area of course(default area according the task: 3400 sq.m.)
- Add animals to the zoo(first user need to create at least 2(two) corrals one for herbivores and one for predators
- To add new animals user just need to choose add menu and then type animal species
  For example:
  User input: "monkey, lion, lynx, roe, lion, bear, monkey, monkey"
  In this case there will be added: 3 monkeys, 2 lions, 1 lynx, 1 roe, 1 bear. Of course if there is enough space.
- Get overall info about the zoo or corrals in it

##################################################################################################################

Program consist of 6 modules:

1.zoo - module where located Zoo class which represent a zoo.
2.corral - module where located Corral class which represent a corral.
3.animals - module where located Animal class which represent an animal, also in this module I create a few Animal
  class objects required by the technical task and put them in the list
4.menu_methods - module with a three functions that used in a main.py
5.main - module where all previous modules are gathered together with purpose to create UI. Program can be activated
  only from this module
6.test_menu_functions - module with a some unit-tests for "split" function from menu_functions module

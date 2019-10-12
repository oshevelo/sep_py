class Kitchen:

    def __init__(self, lenght, width, height, quantity_of_doors, quantity_of_windows):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.quantity_of_doors = quantity_of_doors
        self.quantity_of_windows = quantity_of_windows

    def __str__(self):
        return 'Kitchen'

    def turn_on_lights_in_kitchen(self):
        print('Lights are turned on')

    def turn_off_lights_in_kitchen(self):
        print('Lights are turned off')

    def open_door(self):
        print('Door is opened')

    def close_door(self):
        print('Door is closed')

k = Kitchen(lenght=10, width=5, height=3.5,
            quantity_of_doors=1, quantity_of_windows=2)

class Device:

    def __init__(self, brand, manufactured, color, weight, guarantee, price):
        self.brand = brand
        self.manufactured = manufactured
        self.color = color
        self.weight = weight
        self.guarantee = guarantee
        self.price = price

    def __str__(self):
        return 'class Device'

    def sell_on_device(self, discount=0.7):
        discount = discount * self.price
        print('Was price = {}, now price = {} ,you got discount on 30%'.format(self.price, round(discount)))

class Gas_stove(Device):

    def __init__(self, brand, manufactured, color, weight, guarantee, price, grill, gas_control, surface_grating_materia):
        super().__init__(brand, manufactured, color, weight, guarantee, price)
        self.grill = grill
        self.gas_control = gas_control
        self.surface_grating_materia = surface_grating_materia

    def __str__(self):
        return 'class Stove(Device), brand = {}, price = {}'.format(self.brand, self.price)

    def turn_on_stove(self):
        print('stove are turned on')

    def turn_off_stove(self):
        print('stove are turned off')

    def set_temperature(self, state_degree):
        print('state_degree = {}'.format(state_degree))

object_1 = Gas_stove(brand='Bosch', manufactured='Poland', color='Space_gray',
          weight=35, guarantee='3 Year', price=1500, grill='Yes', gas_control='Yes',
          surface_grating_materia='Enameled')

print(object_1)
object_1.turn_on_stove()
object_1.set_temperature(100)
object_1.sell_on_device()

class Electric_stove(Device):

    def __init__(self, brand, manufactured, color, weight, guarantee, price, convection, grill, screen ):
        super().__init__(brand, manufactured, color, weight, guarantee, price)
        self.convection = convection
        self.grill = grill
        self.screen = screen

    def __str__(self):
        return 'class Stove(Device), brand = {}, price = {}'.format(self.brand, self.price)

    def turn_on_stove(self):
        print('stove are turned on')

    def turn_off_stove(self):
        print('stove are turned off')

object_1 = Electric_stove(brand='Siemens', manufactured='Germany', color='Black',
                 weight=17, guarantee='2 Year', price=3000, convection='Yes',
                 grill='No', screen='Yes')

print(object_1)
object_1.turn_on_stove()
object_1.sell_on_device()

class Washing_machine(Device):

    def __init__(self, brand, manufactured, color, weight, guarantee, price, type, consumption_of_water, energy_class):
        super().__init__(brand, manufactured, color, weight, guarantee, price)
        self.type = type
        self.consumption_of_water = consumption_of_water
        self.energy_class = energy_class

    def __str__(self):
        return 'class Washing_machine(Device), brand = {}, price = {}'.format(self.brand,self.price)

    def set_timer(self,number):
        print('set_timer_on_{}_minutes'.format(number))

    def sell_on_device(self, discount=0.6):
        discount = discount * self.price
        print(discount)
        print('Was price = {}, now price = {} ,you got discount on 40%'.format(self.price, round(discount)))


object_1 = Washing_machine(brand='Indesit', manufactured='Italy', color='White', weight=35,
                           guarantee='1 Year', price=700, type='Fully_Integrated',
                           consumption_of_water='15 liters/hours', energy_class='A+')

print(object_1)
object_1.set_timer(70)
object_1.sell_on_device()
# Implementer -  defines the basic interface for specific implementations.
class OutputInterface:
    def __init__(self):
        self._separator = '\n'

    def printParallelogramm(self, height, width, smaller_angle, larger_angle):
        print('Parallelogramm:', 'Height: ' + str(height), 'Width: ' + str(width), 'Smaller angle: ' + str(smaller_angle), 'Larger angle: ' + str(larger_angle), sep=self._separator)


# Concrete implementation - a specific implementation inherited from Implementer
class OutputInterfaceWithSlash(OutputInterface):
    def __init__(self):
        super().__init__()
        self._separator = ' | '


# Concrete implementation - a specific implementation inherited from Implementer
class OutputInterfaceWithTab(OutputInterface):
    def __init__(self):
        super().__init__()
        self._separator = '\t'


# Abstraction - contains a link to the Implementer - "output_interface"
class Parallelogram:
    def __init__(self, height, width, smaller_angle, larger_angle, output_interface):
        """Initialize the necessary attributes
        Implementation independent Abstraction"""
        self._height = height
        self._width = width
        self._smaller_angle = smaller_angle
        self._larger_angle = larger_angle
        self._output_interface = output_interface

    def output(self):
        """Implementation specific Abstraction"""
        self._output_interface.printParallelogramm(self._height, self._width, self._smaller_angle, self._larger_angle)


# Refined abstraction
class Square(Parallelogram):
    def __init__(self, height, output_interface):
        super().__init__(height, height, 90, 90, output_interface)


# Refined abstraction
class Rectangle(Parallelogram):
    def __init__(self, height, width, output_interface):
        super().__init__(height, width, 90, 90, output_interface)


par1 = Parallelogram(100, 23, 30, 150, OutputInterfaceWithSlash())
rec1 = Rectangle(100, 20, OutputInterfaceWithTab())
sq1 = Square(50, OutputInterface())
par1.output()
rec1.output()
sq1.output()
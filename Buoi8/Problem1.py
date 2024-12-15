class Manufacturer:
    """
    Identity and location of class Manufacturer

    Attributes:
        identity: int
        location: string
    """
    def __init__(self, identity: int, location: str):
        """
        Initializes attributes of the Manufacturer

        Args:
             identity: int
            location: string
        """
        self.identity = identity
        self.location = location
    def describe(self):
        """
        Print description of the Manufacturer.

        Returns:
            A String was formatted and contained the identity and location.
        """
        print(f"Identity: {self.identity} - Location: {self.location}")

class Device:
    """
    Device with name, price, and manufacturer details.

    Attributes:
        name: str
        price: float
        manufacturer: Manufacturer
    """
    def __init__(self, name: str, price: float, identity: int, location: str):
        """
        Initializes attributes of the Device details
        Args:
                name: str
                price: float
                manufacturer: Manufacturer
        """
        self.name = name
        self.price = price
        self.manufacturer = Manufacturer(identity, location)
    def describe(self):
        """
        Prints the description of the Device and its Manufacturer.
        """
        print(f"Name: {self.name} - Price: {self.price}")
        print(self.manufacturer.describe())

#test_case
device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.describe()
device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.describe()
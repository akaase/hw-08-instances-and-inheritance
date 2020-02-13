class Body:
    def __init__(???):
        ???

class Star(???):
    def __init__(???):
        ???

class Planet(???):
    def __init__(???):
        ???

class Moon(???):
    def __init__(???):
        ???

class System:
    def __init__(???):
        self.bodies = []

    def add(???):
        self.bodies.append(???)

    def total_mass(???):
        total = 0
        for body in self.bodies:
            total += body.mass
        return total

def main():
    # Create the solar system and its bodies
    sun   = ??? # Use the name 'Sun', mass of 200, and type of 'G-Type'
    earth = ??? # Use the name 'Earth', mass of 150, day_length of 24, and year_length of 365
    luna  = ??? # Use the name 'Luna', mass of 100, month_length of 30, and orbit_planet of earth
    solar_system = ???
    solar_system.add(???)
    solar_system.add(???)
    solar_system.add(???)

    # Print each body in the solar system to see if they have been added correctly
    for body in solar_system.bodies:
        print(body.name)

    # Checking to see that total mass is correct
    print(solar_system.total_mass())

main()

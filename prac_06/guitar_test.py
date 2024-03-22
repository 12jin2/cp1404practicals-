from prac_06.guitar import Guitar
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 10000)
old_guitar = Guitar("old guitar", 1974)
print(f"{guitar1.name} get_age() - Expected {guitar1.get_age()}. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected {guitar2.get_age()}. Got {guitar2.get_age()}")
print(f"{guitar1.name} is_vintage() - Expected {guitar1.is_vintage()}. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected {guitar2.is_vintage()}. Got {guitar2.is_vintage()}")

print(f"50 year {old_guitar.name} is_vintage() - Expected True. Got {old_guitar.is_vintage()}")


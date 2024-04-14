class Band:
    """Band class holding a list of musicians."""

    def __init__(self, name):
        """Initialize the band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band with all its musicians and their instruments."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Simulate playing music by having each musician play their instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)

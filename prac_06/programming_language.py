
class ProgrammingLanguage:
      def __init__(self, field="", typing="", reflection="", year=0 ):
          self.field = field
          self.typing = typing
          self.reflection = reflection
          self.year = year

      def isdynamic(self):
          return self.typing == "Dynamic"

      def __str__(self):
          return f"{self.field}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"




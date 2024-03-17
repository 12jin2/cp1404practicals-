NAME_TO_COLOUR = {
    "ABSOLUTE ZERO": "#0048ba",
    "ACID GREEN": "#b0bf1a",
    "ALICEBLUE": "#f0f8ff",
    "ALIZARIN CRIMSON": "#e32636",
    "AMARANTH": "#e52b50",
    "AMBER": "#ffbf00",
    "ANTIQUEWHITE4": "#8b8378",
    "BRONZE": "#cd7f32",
    "BLACK": "#000000"
}
colour_name = input("Enter colour name: ").upper()
while colour_name != "BLACK":
     if colour_name in NAME_TO_COLOUR:
          print(NAME_TO_COLOUR[colour_name])
     else:
          print("Invalid colour name")
     colour_name = input("Enter colour name: ").upper()
print("End")
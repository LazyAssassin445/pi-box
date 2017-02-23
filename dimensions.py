
thickness = int(input("How thick is your wood in millimetres? "))
overhang = int(input("How much do you want the top plank to overhang in millimetres? "))

#work out bird section dimensions
birdfr1 = 200+thickness
birdfr2 = 150
birdba1 = 200+thickness
birdba2 = 150
birdbo1 = 150
birdbo2 = 150
birdto1 = 150+20+(thickness*3)
birdto2 = 150


#work out main dimenstions
fr1 = 222+thickness
fr2 = 150
ba1 = 538+thickness
ba2 = 150+(2*thickness)
bo1 = 150+20+(2*thickness)
bo2 = 150
to1 = 150+(2*thickness)
to2 = 150+20+(thickness*4)


#work out side dimensions
si1 = 440
si2 = 150+20+(thickness*3)


print("\nBIRD SECTION\n")
print("Front = ", birdfr1, " X ", birdfr2)
print("Back = ", birdba1, " X ", birdba2)
print("Bottom = ", birdbo1, " X ", birdbo2)
print("Top = ", birdto1, " X ", birdto2)

print("\nMAIN SECTION\n")
print("Front = ", fr1, " X ", fr2)
print("Back = ", ba1, " X ", ba2)
print("Bottom = ", bo1, " X ", bo2)
print("Top = ", to1, " X ", to2)

print("\nSIDE SECTION\n")
print("Left = ", si1, " X ", si2)
print("Right = ", si1, " X ", si2)


print("\n\n With these side panels you must cut a 45 degree angle from the top corner to ", fr1, "off the bottom as shown below!\n")

print("         |\\")
print("         |  \\")
print("         |    \\")
print("         |      \\")
print("         |        \\")
print("         |          \\")
print("         |            \\")
print("         |              \\")
print("         |                \\")
print("         |                  \\")
print("         |                    \\")
print(" 440 mm  |                      |")
print("         |                      |")
print("         |                      |")
print("         |                      |")
print("         |                      |")
print("         |                      |      ", fr1, "mm")
print("         |                      |")
print("         |                      |")
print("         |                      |")
print("         |                      |")
print("         ________________________")
print("                   ", si2, "mm")




flat = int(input("Flat number "))
if 1 <= flat <= 36:
    print('Entrance number is 1')
elif 37 <= flat <= 72:
    print('Entrance number is 2')
elif 73 <= flat <= 108:
    print('Entrance number is 3')
elif flat <= 144:
    print('Entrance number is 4')
else:
    print('Error')
if 1 <= flat <= 4 or 37 <= flat <= 40 or 73 <= flat <= 76 or 109 <= flat <= 112:
    print('1st floor')
elif 5 <= flat <= 8 or 41 <= flat <= 44 or 77 <= flat <= 80 or 113 <= flat <= 116:
    print('2nd floor')
elif 9 <= flat <= 12 or 45 <= flat <= 48 or 81 <= flat <= 84 or 117 <= flat <= 120:
    print('3rd floor')
elif 13 <= flat <= 16 or 49 <= flat <= 52 or 85 <= flat <= 88 or 121 <= flat <= 124:
    print('4th floor')
elif 17 <= flat <= 20 or 53 <= flat <= 56 or 89 <= flat <= 92 or 125 <= flat <= 128:
    print('5th floor')
elif 21 <= flat <= 24 or 57 <= flat <= 60 or 93 <= flat <= 96 or 129 <= flat <= 132:
    print('6th floor')
elif 25 <= flat <= 28 or 61 <= flat <= 64 or 97 <= flat <= 100 or 133 <= flat <= 136:
    print('7th floor')
elif 29 <= flat <= 32 or 65 <= flat <= 68 or 101 <= flat <= 104 or 137 <= flat <= 140:
    print('8th floor')
elif 33 <= flat <= 36 or 69 <= flat <= 72 or 105 <= flat <= 108 or 141 <= flat <= 144:
    print('9th floor')
else:
    print('Error')

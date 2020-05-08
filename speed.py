
# distance from earth to the Sun in km
distance: float = 150000000.

# read input from standard input:
speed = input('Quelle est la vitesse en km/h ?')

try:
    val = float(speed)
    print("Yes input string is an float.")
    print(f'your speed is {val:4.2f} km/h')
except ValueError:
    print("That's not an int!")
    print("No.. input string is not an float. It's a string")

    speed = input('Quelle est la vitesse en km/h, number sans unit?')

if speed.isdigit():
    print("User input is Number ")
else:
    print("User input is string ")


if type(speed):
    print(f'is it ki dding ?')
elif speed > 3000:
    print(f'is i000000t kidding ?')

if speed > 600:
    print('yes')

time = distance /speed
print(f'Le temps necessaire pour effectuer cette distance est {time:4.2f} hours')

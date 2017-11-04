microbe_ppm = 500
upper_limit = 100
lethal_limit = '1000'

try:
    if microbe_ppm < upper_limit:
        print('Patient should show no symptoms')

    elif microbe_ppm > lethal_limit:
        print('Patient will not survive')

except:
    print("Can't calculate patient status")
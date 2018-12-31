def is_leap(year):
    leap = False
    cuatro = int(year/4)
    cien = int(year/100)
    cuantrocientos = int(year/400)

    if(year==1800) or (year==1900) or (year==2100) or (year==2200) or (year==2300) or (year==2500):
        leap = False
    elif(cuatro*4 == year):
        leap = True
    elif(cien*100 == year):
                leap = False
    elif (cuantrocientos*400 == year):
        leap = True


    return leap

year = int(input())
print(is_leap(year))

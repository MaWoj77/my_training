def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        pass
    elif year % 4 == 0:
        leap = True
    else:
        pass
    
    return leap

if __name__ == "__main__":
    year = int(input())
    if is_leap(year):
        print(f"Year {year} is leap.")
    else:
        print(f"Year {year} is not leap.")
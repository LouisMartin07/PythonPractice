def bottles_of_beer(n):
    if n == 0:
        return ["No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall."]
    elif n == 1:
        return [f"{n} bottle of beer on the wall, {n} bottle of beer. Take it down and pass it around, no more bottles of beer on the wall."] + bottles_of_beer(n-1)
    else:
        return [f"{n} bottles of beer on the wall, {n} bottles of beer. Take one down and pass it around, {n-1} bottles of beer on the wall."] + bottles_of_beer(n-1)
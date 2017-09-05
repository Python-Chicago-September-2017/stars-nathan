a = [2,4,6,8,10,1]
b = [2, "Lions", 10, "Tigers", 5, "Bears"]

def draw_stars(arr):
    for i in arr:
        if type(i) == int:
            print "*" * i
        else:
            word = str(i)
            word = word.lower()
            first_letter = word[0]
            length = len(word)
            print first_letter * length

draw_stars(b)
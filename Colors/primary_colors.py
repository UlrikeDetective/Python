def diff(a, b):
    """
    DONE: Translation to english
    TODO: fix this function!!
    """
    return a - b


def simpleColor(r, g, b):
    """simpleColor obtains the most general color name to which its R G B format is closest"""
    r = int(r)
    g = int(g)
    b = int(b)
    bg = ir = 0  # TODO: Fix these variables
    try:
        # RED --------------------------------------------------
        if r > g and r > b:

            rg = diff(r, g)  # distance red to green
            rb = diff(r, b)  # distance red to blue

            if g < 65 and b < 65 and rg > 60:  # blue and green without light
                return "RED"

            gb = diff(g, b)  # distance from green to blue

            if rg < rb:  # Green greater than Blue
                if gb < rg:  # Green closer to Blue
                    if gb >= 30 and rg >= 80:
                        return "ORANGE"
                    elif gb <= 20 and rg >= 80:
                        return "RED"
                    elif gb <= 20 and b > 175:
                        return "CREAM"

                    else:
                        return "CHOCOLATE"
                else:  # Green closer to Red
                    if rg > 60:
                        return "ORANGE*"
                    elif r > 125:
                        return "YELLOW"
                    else:
                        return "CHOCOLATE"
            elif rg > rb:  # Blue greater than Green
                if bg < rb:  # Green closer to Blue
                    if gb < 60:
                        if r > 150:
                            return "RED 2"
                        else:
                            return "BROWN"
                    elif g > 125:
                        return "PINK"
                    else:
                        return "RED 3"
                else:  # Green closer to Red
                    if rb < 60:
                        if r > 160:
                            return "PINK*"
                        else:
                            return "RED"
                    else:
                        return "RED"

            else:  # g and b equal
                if rg > 20:
                    if r >= 100 and b < 60:
                        return "RED"
                    elif r >= 100:
                        return "RED"
                    else:
                        return "BROWN"

                else:
                    return "GRAY"
        # GREEN ---------------------------------------------------
        elif g > r and g > b:
            gb = diff(g, b)  # distance from green to blue
            gr = diff(g, r)  # distance from green to red

            if r < 65 and b < 65 and gb > 60:  # red and blue without light
                return "GREEN"

            rb = diff(r, b)  # distance from red to blue

            if r > b:  # RED > BLUE
                if gr < gb:  # Green with Red

                    if rb >= 150 and gr <= 20:
                        return "YELLOW"
                    else:
                        return "GREEN"
                else:  # ...Green
                    return "GREEN"

            elif r < b:  # BLUE > RED
                if gb < gr:  # Green with Blue

                    if gb <= 20:
                        return "TURQUOISE"
                    else:
                        return "GREEN"
                else:  # ...Green
                    return "GREEN"

            else:  # r and b equal
                if gb > 10:
                    return "GREEN"
                else:
                    return "GRAY"

        # BLUE ------------------------------------------------------
        elif b > r and b > g:
            bg = diff(b, g)  # distance from blue to green
            br = diff(b, r)  # distance from blue to red

            if r < 65 and g < 65 and bg > 60:  # red and green without light
                return "BLUE"

            rg = diff(r, g)  # distance from red to green

            if g < r:  # RED  > GREEN
                if bg < rg:  # Blue with Green
                    if bg <= 20:
                        return "TURQUOISE"
                    else:
                        return "SKY BLUE"
                else:  # ...Blue
                    if rg <= 20:
                        if r >= 150:
                            return "LILAC"
                        else:
                            return "BLUE *************"
                    else:
                        return "BLUE"

            elif g > r:  #  GREEN > RED
                if br < rg:  # Blue with red
                    if br <= 20:
                        if r > 150 and g < 75:
                            return "PINK FUCHSIA"
                        elif ir > 150:
                            return "LILAC"
                        else:
                            return "PURPLE"
                    else:
                        return "PURPLE"

                else:  # ...Blue
                    if rg <= 20:
                        if bg <= 20:
                            return "GRAY"
                        else:
                            return "BLUE"
            else:  # r and g equal
                if bg > 20:
                    if r >= 100 and b < 60:
                        return "RED"
                    elif r >= 100:
                        return "RED"
                    else:
                        return "BROWN"
                else:
                    return "GRAY"

        # EQUALS---------------------------------------
        else:
            return "GRAY"

    except:

        return "Not Color"


# ---------------------------------------------------------------------------------------------------
# You can test like this: python primary_colors.py 120,0,0, this will result in a RED as response
# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import sys

    print(simpleColor(sys.argv[1], sys.argv[2], sys.argv[3]))

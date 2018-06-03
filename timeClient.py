import urllib.request


# this turns the "HHMM" time into an array representing the thirteen
# segments of the display from least significant to most significant
# examples:
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] = 00:00
# I don't really want to figure any other ones out rn
def getBinaryTime(time):
    # digits are numbered 0-3 from least to most significant
    digit0 = int(time[3])
    digit1 = int(time[2])
    digit2 = int(time[1])
    digit3 = int(time[0])

    # place the binary values in strings
    zero = [0, 0, 0, 0]
    one = [0, 0, 0]
    two = [0, 0, 0, 0]
    three = [0, 0]

    # loop through the decimal and binary values at the same time using zip
    for (analogue, digital) in zip([digit0, digit1, digit2, digit3], [zero,
                                                                      one,
                                                                      two,
                                                                      three]):
        # get a binary value for the decimal digit by looping through the
        # length of the
        # output and using bitwise magic
        for digitNum in range(len(digital)):
            digital[-1 - digitNum] = analogue & 1
            analogue = analogue >> 1
    return [three, two, one, zero]


def getTimeFromServer():
    server_address = "http://127.0.0.1:5000/getTime"
    time = urllib.request.urlopen(server_address).read().decode("UTF-8")
    print("Time:", time)
    print(getBinaryTime(time))


getTimeFromServer()

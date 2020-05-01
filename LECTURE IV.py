
##IPAddress=input("Input your IP address: ")
##character = " "
##segment = 1
##segment_length = 0
##
##
##
##
##
##
##for character in IPAddress:
##    if character == ".":
##        
##        print("segment {} contains {} characters".format(segment,segment_length))
##        segment += 1
##        segment_length = 0
##    else:
##        segment_length += 1
##
##
##
##if character != ".":
##    print("segment {} contains {} characters".format(segment,segment_length))
##


        
######BIG MAN WAY
IPAddress = input("Put in youur IP Address: ")
IPAddress += "."
segment = 1
segment_length = 0

for character in IPAddress:
    if character == ".":
        print("Segment {} contains {} chracters".format(segment,segment_length))
        segment += 1
        segment_length = 0
    else:
        #print("Segment {} contains {} characters".format(segment,segment_length))
        segment_length += 1

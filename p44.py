def decode_sequence(*item:int):
    dict = {}
    for i in range(1, 28):
        dict[i]  = chr(i+96)

    for i in item:
        print(dict[i], end=" ")

decode_sequence(12,1,21)
        
        
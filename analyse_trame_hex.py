#affichage des trames en hexa
def print_bytes(data):  
    text = ""
    for i in range(0, len(data)):
        text = text + f"{data[i]:02x}"
    print(text)
    
# hex: f1 0d 00 02 aa 02 49 00 00 49 00 31 37 00 55 
if __name__ == "__main__":
    trame = b'\xf1\r\x0d\x502\xaa\x02\x20\x00I\x0017\x00U'
    print(trame)
    print_bytes(trame)


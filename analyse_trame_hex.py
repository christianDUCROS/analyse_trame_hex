#affichage des trames en hexa
def conversion_trame_bytes(trame):  
    trame_hex = ""
    for i in range(0, len(trame)):
        trame_hex = trame_hex + f"{trame[i]:02x}"
    return trame_hex
    
# f1 0d 00 50 32 aa 02 20 00 49 00 31 37 00 55 
if __name__ == "__main__":
    trame = b'\xf1\r\x0d\x502\xaa\x02\x20\x00I\x0017\x00U'
    resultat = conversion_trame_bytes(trame)   
    print(trame)
    print(resultat)


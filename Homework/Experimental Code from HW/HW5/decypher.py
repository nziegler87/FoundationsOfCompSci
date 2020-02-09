import string
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)
               
def decrypt(message, shift):
    ''' Name: decypt
        Inputs: message (str), shift amount (int)
        Returns: decrypted message (str)
    '''
    message = message.lower()
    encrypted_list = list(message)
    decrypted_list = []

    for i in range(len(encrypted_list)):
        if encrypted_list[i] in EXCLUDE:
            decrypted_list.append(ord(encrypted_list[i]))
        else:
            encrypted_val = ord(encrypted_list[i])
            decrypted_val = encrypted_val - shift
            if decrypted_val < ord('a'):
                remainder = ord("a") % decrypted_val
                decrypted_val = ord("z") - remainder + 1
            decrypted_list.append(decrypted_val)
    decrypted_string = ""
    for i in range(len(decrypted_list)):
        decrypted_string += chr(decrypted_list[i])
    return decrypted_string


encrypted = ["xli qer als tewwiw xli wirxirgi wlsyph wamrk xli wasvh",
             "lclyfvul pz tpul av avytlua",
             "zpv lopx opuijoh, kpo topx",
             "xlex'w alex m hs: m hvmro erh m orsa xlmrkw",
             "fqfx, n'r rtxy kfrnqnfw bnym otsfymfs afs sjxx' lfd tk ymwtsjx"]

for i in range(len(encrypted)):
    for count in range(1,8):
        decrypted_message = decrypt(encrypted[i], count)
        print("Message ", i, " | Shift ", count, ": ",
              decrypted_message, sep = "")
        if count == 7:
            print()

        

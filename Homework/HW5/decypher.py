import string
from encryption import *

EXCLUDE = list(string.digits + string.punctuation + string.whitespace)
ENCRYPTED = ["xli qer als tewwiw xli wirxirgi wlsyph wamrk xli wasvh",
             "lclyfvul pz tpul av avytlua",
             "zpv lopx opuijoh, kpo topx",
             "xlex'w alex m hs: m hvmro erh m orsa xlmrkw",]

def main():
    
    print("Let me decypher the following messages:", "\n")
    for i in range(len(ENCRYPTED)):
        print("   ", "Message ", i, ": ", ENCRYPTED[i], "\n", sep = "")

    # iterate through encrypted messages, applying shifts
    for i in range(len(ENCRYPTED)):
        result_string = ""
        for count in range(1,8):
            decrypted_message = decrypt(ENCRYPTED[i], count)
            result_string += "Message " + str(i) + " | Shift " + str(count) + \
                             ": " + decrypted_message + "\n"
            if count == 7:
                result_string += "\n"

        print(result_string)

main()

        

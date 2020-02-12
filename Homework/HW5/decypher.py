'''
    Nathanial Ziegler
    CS 5001
    February 12, 2020
    HW 5

    Description:
        Program calls decrypt function, iterating through four encrypted
        phrases, starting with a shift of 1 and continuing to 7 for each
        message until decrypted message is shown.
'''

import string
from encryption import *

# list of encrypted message to iterate through function
ENCRYPTED = ["xli qer als tewwiw xli wirxirgi wlsyph wamrk xli wasvh",
             "lclyfvul pz tpul av avytlua",
             "zpv lopx opuijoh, kpo topx",
             "xlex'w alex m hs: m hvmro erh m orsa xlmrkw",]

def main():

    # Introduce program
    print("Let me decypher the following messages:", "\n")
    for i in range(len(ENCRYPTED)):
        print("   ", "Message ", i, ": ", ENCRYPTED[i], "\n", sep = "")

    # iterate through messages, applying shifts 1 to 7 for each one
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

        

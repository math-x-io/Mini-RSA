import MiniRSA
import hashlib

BobKeys = MiniRSA.gen_RSA_key()
AliceKeys = MiniRSA.gen_RSA_key()

AliceMessage = "Hello Bob, how are you ?"

def genFooter(clearFooter):
    clearFooter = str(clearFooter).strip()
    return hashlib.sha512(clearFooter.encode()).hexdigest(), len(clearFooter)
    

AliceFooter = genFooter(AliceKeys[2])[0]
AliceFooter = MiniRSA.chiffrer_texte(AliceFooter, AliceKeys[1], AliceKeys[0])
lenAliceFooter = genFooter(AliceKeys[2])[1]

#print(f"Signature d'Alice : {AliceFooter}")

BobFooter = genFooter(BobKeys[2])[0]
BobFooter = MiniRSA.chiffrer_texte(BobFooter, BobKeys[1], BobKeys[0])
lenBobFooter = genFooter(BobKeys[2])[1]
#print(f"Signature de Bob : {BobFooter}")

AliceMessageChiffré = MiniRSA.chiffrer_texte(AliceMessage, AliceKeys[1], AliceKeys[0])

AliceMessageChiffré = AliceMessageChiffré + AliceFooter

def DéchiffrerMessage(message,lenFooter,key1,key2):
    return MiniRSA.chiffrer_texte(message[:lenFooter],key1,key2)

AliceMessageChiffré = AliceMessageChiffré[:len(AliceFooter)]
#print(MiniRSA.chiffrer_texte(AliceMessageChiffré, AliceKeys[2], AliceKeys[0]))
print(DéchiffrerMessage(AliceMessageChiffré,lenAliceFooter,AliceKeys[2],AliceKeys[0]))

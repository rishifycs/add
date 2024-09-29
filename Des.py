from des import DesKey
pt=bytes(input("enter plain Text:"),'utf-8')
key=bytes(input("enter key:"),'utf-8')
k=DesKey(key)
k.is_single()
en=k.encrypt(pt)
print("Encrypted text:",en)
de=k.decrypt(en)
print("Decrypted text:",de)



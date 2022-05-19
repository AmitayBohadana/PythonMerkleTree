# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from merkletools import MerkleTools
import sha3

from eth_abi import encode_abi

def convertProof(proof):
    res = []
    for element in proof:
        if('right' in element):
            res.append(element['right'])
        elif('left' in element):
            res.append(element['left'])
    return res

def hash_keccak_256(input):
    print(sha3.keccak_256)
    k = sha3.keccak_256()
    k.update(input)
    return k.hexdigest()

def createMerkleTree(whiteList):

    mt = MerkleTools(hash_type="keccak_256")

    for user in whiteList:
        print(user["address"])
        encode = encode_abi(['address','uint256'], [user["address"], user["amount"]])
        hash = hash_keccak_256(encode)
        # hash = hash_keccak_256(bytes.fromhex(hash))
        print("hash added: ",hash)
        mt.add_leaf(hash)

    mt.make_tree()
    print('-------------')
    print("root:", mt.get_merkle_root())
    print('-------------')

    index = 0
    for user in whiteList:
        print("after fix proof: ",convertProof(mt.get_proof(index)))
        index = index + 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    whiteList = [
        {"address": '0x70997970C51812dc3A010C7d01b50e0d17dc79C8', "amount": 100000000000000000000},
        {"address": '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC', "amount": 100000000000000000000},
        # {"address": '0x90F79bf6EB2c4f870365E785982E1f101E93b906', "amount": 100000000000000000000},
        # {"address": '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65', "amount": 100000000000000000000},
        # {"address": '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc', "amount": 100000000000000000000},
    ]
    createMerkleTree(whiteList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

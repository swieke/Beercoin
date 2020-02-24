import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data # The data can be anything!
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash)
        )
        return sha.hexdigest()

def create_genesis_block():
    # Create an initial block with 
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block" ,"0" )

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Get to the business.


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# We create 20 blocks.
num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    # Print each block state.
    print("Block #{} has been added to the chain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))



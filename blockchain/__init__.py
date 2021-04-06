"""
Custom Python implementation of a Block
"""

from datetime import datetime
from hashlib import sha256
from json import dumps


class Block(object):
    """
    A block will contain the index, which is the location of this block in
    the block-chain timestamp will indicate the time the Block is created and
    previous_hash is the hash of the previous block in the chain
    """

    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        This creates a hash for the current block
        """
        return sha256(str(self.index) + str(self.timestamp) +
                      self.previous_hash + str(dumps(self.data).encode("utf-8"))).hexdigest()

    def __repr__(self):
        return "Block:{} => [Created at: {}, Data: {}, Previous Hash: {}, Hash: {}]".format(self.index, self.timestamp,
                                                                                            self.data,
                                                                                            self.previous_hash,
                                                                                            self.hash)


class BlockChain(object):
    """
    Custom implementation of a block chain
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates a genesis Block when the block chain is first created.
        :rtype: Block
        """
        return Block(0, datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Gets the latest block in the chain
        :return: Block
        :rtype: Block
        """
        return self.chain[len(self.chain) - 1]

    def add_block(self, new_block):
        """
        Adds a block to the block chain
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the Block chain and checks whether it is valid, returns
        False when the block is invalid and True when valid. This is validated
        by checking whether the current block in the chain
        :rtype: bool
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def print_block_chain(self):
        """
        Prints the Block chain
        """
        for i in range(1, len(self.chain)):
            print(self.chain[i])


if __name__ == "__main__":
    block_chain = BlockChain()
    block_chain.add_block(Block(1, datetime.now(), {"account": "Anna", "amount": 25, "action": "buy"}))
    block_chain.add_block(Block(2, datetime.now(), {"account": "Joe", "amount": 10, "action": "buy"}))
    block_chain.add_block(Block(3, datetime.now(), {"account": "Katie", "amount": 20, "action": "buy"}))
    block_chain.add_block(Block(4, datetime.now(), {"account": "Ethan" "amount": 4, "action": "buy"}))
    block_chain.print_block_chain()
    # no tampering in our block chain yet so should be true here
    print("Chain valid? " + str(block_chain.is_chain_valid()))
    # now lets tamper the block chain and see what happens
    block_chain.chain[1].data = {"account": "Anna", "amount": 100, "action": "buy"}
    print("Chain valid? " + str(block_chain.is_chain_valid()))

import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(value.encode()).hexdigest()


class TinyChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True


# ====== TESTING ======
if __name__ == "__main__":
    tc = TinyChain()

    tc.add_block("Block 1 Data")
    tc.add_block("Block 2 Data")

    for block in tc.chain:
        print("Index:", block.index)
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Hash:", block.hash)
        print("Prev Hash:", block.previous_hash)
        print("-" * 30)

    print("Chain valid?", tc.is_chain_valid())
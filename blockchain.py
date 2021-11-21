import hashlib
import json
from time import time
from typing import Optional, TypedDict

class Block(TypedDict):
    index: int
    timestamp: float
    proof: int
    previous_hash: str

class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof: int, previous_hash: str | None = None) -> Block:
        """新しいブロックを作り、チェーンに加える"""
        block: Block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        del self.current_transactions[:]
        self.chain.append(block)
        return block

    def new_transaction(self):
        """新しいトランザクションをリストに加える"""
        pass

    @staticmethod
    def hash(block: Block) -> str:
        """ブロックをハッシュ化する"""
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    @property
    def last_block(self):
        """チェーンの最後のブロックを返す"""
        pass

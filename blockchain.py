import hashlib
import json
from time import time
from typing import TypedDict

class Block(TypedDict):
    index: int
    timestamp: float
    proof: int
    previous_hash: str

def block_hash(block: Block) -> str:
    """ブロックのハッシュを求める"""
    encoded = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

class Transaction(TypedDict):
    sender: str
    recipient: str
    amount: int

class Blockchain:
    def __init__(self) -> None:
        self.chain: list[Block] = []
        self.current_transactions: list[Transaction] = []
        self.new_block(previous_hash="1", proof=100)

    @property
    def last_block(self) -> Block:
        """チェーンの最後のブロックを返す"""
        return self.chain[-1]

    def new_block(self, proof: int, previous_hash: str | None = None) -> None:
        """新しいブロックを作り、チェーンに加える

        Args:
            proof: PoW から得られるプルーフ
            previous_hash: 前のブロックのハッシュ
        """

        del self.current_transactions[:] # 現在のトランザクションをリセット

        self.chain.append({
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or block_hash(self.last_block),
        })

    def new_transaction(self, transaction: Transaction) -> None:
        """次に採掘されるブロックに加える新しいトランザクションを作る
        
        Args:
            sender: 送信者のアドレス
            recipient: 受信者のアドレス
            amount: 量
        """

        self.current_transactions.append(transaction)

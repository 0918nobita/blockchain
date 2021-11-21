from time import time

from blockchain.block import Block, Hash, block_hash
from blockchain.proof import Proof
from blockchain.transaction import Transaction

class Blockchain:
    def __init__(self) -> None:
        self.chain: list[Block] = []

        self.current_transactions: list[Transaction] = []

        self.new_block(previous_hash=Hash("1"), proof=Proof(100))

    @property
    def last_block(self) -> Block:
        """チェーンの最後のブロックを返す"""
        return self.chain[-1]

    def new_block(self, proof: Proof, previous_hash: Hash | None = None) -> None:
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

if __name__ == "__main__":
    Blockchain()
    print("Blockchain")

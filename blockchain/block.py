import hashlib
import json
from typing import NewType, TypedDict

from blockchain.proof import Proof

Hash = NewType("Hash", str)

class Block(TypedDict):
    index: int
    timestamp: float
    proof: Proof
    previous_hash: Hash

def block_hash(block: Block) -> Hash:
    """ブロックのハッシュを求める"""
    encoded = json.dumps(block, sort_keys=True).encode()
    return Hash(hashlib.sha256(encoded).hexdigest())

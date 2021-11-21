from dataclasses import dataclass
import hashlib
import json
from typing import TypedDict

from proof import Proof

@dataclass
class Hash:
    raw: str

class Block(TypedDict):
    index: int
    timestamp: float
    proof: Proof
    previous_hash: Hash

def block_hash(block: Block) -> Hash:
    """ブロックのハッシュを求める"""
    encoded = json.dumps(block, sort_keys=True).encode()
    return Hash(hashlib.sha256(encoded).hexdigest())

from typing import TypedDict

class Transaction(TypedDict):
    sender: str
    recipient: str
    amount: int

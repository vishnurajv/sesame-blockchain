from dataclasses import dataclass
from typing import Optional

from sesame.types.blockchain_format.sized_bytes import bytes32
from sesame.util.ints import uint64
from sesame.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class CCParent(Streamable):
    parent_name: bytes32
    inner_puzzle_hash: Optional[bytes32]
    amount: uint64

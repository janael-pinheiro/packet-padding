from dataclasses import dataclass, field

from typing import List, Dict

from adaptive_padding.padding.padding_strategy import PaddingStrategy


@dataclass
class DynamicProgrammingPadding(PaddingStrategy):
    __memory: Dict[int, int] = field(default_factory=dict)

    def __post_init__(self):
        self.lengths: List[int] =\
            [66, 102, 156, 201, 253, 350, 493, 538, 1236, 1514]

    def pad(self, length: int) -> int:
        if length in self.__memory:
            return self.__memory.get(length)

        extra_bytes = 0
        for l in self.lengths:
            if l > length:
                extra_bytes = l - length
                break
        self.__memory[length] = length + extra_bytes
        return self.__memory.get(length)
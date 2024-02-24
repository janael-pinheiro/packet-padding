from dataclasses import dataclass, field

from adaptive_padding.padding.padding_strategy import PaddingStrategy, pad_length_equal_to_or_greater_than_mtu


@dataclass
class MouseElephant(PaddingStrategy):
    mtu_number_bytes: int = field(default=1500)

    def __post_init__(self):
        self.__extra_bytes: int = 0

    @pad_length_equal_to_or_greater_than_mtu
    def pad(self, length: int) -> int:
        try:
            if length < 100:
                self.__extra_bytes = 100 - length
            elif length >= 100 and length < self.mtu_number_bytes:
                self.__extra_bytes = self.mtu_number_bytes - length
            return length + self.__extra_bytes
        except ValueError as e:
            raise e

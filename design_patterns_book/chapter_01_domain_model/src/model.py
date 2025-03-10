from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List


class OutOfStock(Exception):
    pass


def allocate(line: OrderLine, batches: List[Batch]):
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")


@dataclass(frozen=True)
class OrderLine:
    ordered: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty


if __name__ == '__main__':
    batch1 = Batch('batch-001', 'SMALL-TABLE', qty=20, eta=date.today())
    line1 = OrderLine('order-ref', 'SMALL-TABLE', 1)
    line2 = OrderLine('order-ref', 'SMALL-TABLE', 2)
    line3 = OrderLine('order-ref', 'SMALL-TABLE', 3)
    batch1.allocate(line1)
    batch1.allocate(line2)
    batch1.allocate(line3)
    batch1.deallocate(line2)
    print(batch1.available_quantity)
    print(batch1.allocated_quantity)

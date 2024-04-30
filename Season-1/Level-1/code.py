'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000
MAX_QUANTITY = 100
MIN_QUANTITY = 0
MAX_TOTAL = 1e6

def validorder(order: Order):
    net = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                net += Decimal(str(item.amount))
                if abs(net) > MAX_TOTAL:
                    return "Total amount payable for an order exceeded"
        elif item.type == 'product':
            if type(item.quantity) is int and MIN_QUANTITY < item.quantity <= MAX_QUANTITY and MIN_QUANTITY < item.amount <= MAX_ITEM_AMOUNT:
                net -= Decimal(str(item.amount)) * item.quantity
                if abs(net) > MAX_TOTAL:
                    return "Total amount payable for an order exceeded"
        else:
            return "Invalid item type: %s" % item.type
    if abs(net) > MAX_TOTAL:
        return "Total amount payable for an order exceeded"
    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
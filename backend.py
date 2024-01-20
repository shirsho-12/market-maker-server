from ob.orderBook import OrderBook
from ob.common.order import Order
from ob.common.ptreeIterator import ComplexIterator

class User():
    def __init__(self, user_id):
        self.user_id = user_id
        self.position = 0
        self.buys = []
        self.sells = []     
        self.buy_orders = []
        self.sell_orders = []
    
    def pnl(self, final_val):
        return final_val * self.position - sum([i[0] * i[1] for i in self.buys]) + sum([i[0] * i[1] for i in self.sells])
    
    def add_buy(self, price, quantity):
        self.buys.append([price, quantity])
        self.position += quantity


    def add_sell(self, price, quantity):
        self.sells.append([price, quantity])
        self.position -= quantity

    def get_orderbook(self, bids, asks):
        bids = [[i[0], i[1], 0] for i in bids]
        asks = [[i[0], i[1], 0] for i in asks]

        # Lower part of the code can be easily optimised with binary search but too lazy right now
        for i in self.buy_orders:
            for j in range(len(bids)):
                if i.price == bids[j][0]:
                    bids[j][2] += i.size
                    break

        for i in self.sell_orders:
            for j in range(len(asks)):
                if i.price == asks[j][0]:
                    asks[j][2] += i.size
                    break
    

class BackEnd:
    def __init__(self):
        self.users = []
        self.orderbook = OrderBook()
        self.tot_orders = 0
        self.order_to_user = dict([])

    def add_user(self, user):
        self.users.append(user)
    
    def add_order(self, user, type, price, quantity):
        order_id = self.tot_orders
        self.order_to_user[order_id] = user
        self.tot_orders += 1
        order = Order(type, order_id, price, quantity)
        if type == 'B':
            user.buy_orders.append(order)
        else:
            user.sell_orders.append(order)
        trades = self.orderbook.process_order(order)
        print(trades)
        for i in trades:
            bid_order_id, ask_order_id, trade_price, trade_quantity = map(int, i.split(','))
            print(bid_order_id, ask_order_id, trade_price, trade_quantity)
            self.order_to_user[bid_order_id].add_buy(trade_price, trade_quantity)
            self.order_to_user[ask_order_id].add_sell(trade_price, trade_quantity)


    def pull_buy_orders(self, user):
        for order in user.buy_orders:
            order.make_trade(order.size)
            order.trade_size = 0
        user.buy_orders = []

    def pull_sell_orders(self, user):
        for order in user.sell_orders:
            order.make_trade(order.size)
        user.sell_orders = []

    def pull_all_orders(self, user):
        self.pull_buy_orders(user)
        self.pull_sell_orders(user)

    def get_orderbook(self, one_side_cap = 10, user = None):
        bids_it = ComplexIterator(self.orderbook.bids.tree.values(reverse=True))
        asks_it = ComplexIterator(self.orderbook.asks.tree.values())
        bids = []
        while bids_it.hasnext():
            bid = bids_it.next()
            if bids and bids[-1][0] == bid.price: 
                bids[-1][1] += bid.peak_size
            else:
                if len(bids) == one_side_cap:
                    break
                bids.append([bid.price, bid.peak_size])
        asks = []
        while asks_it.hasnext():
            ask = asks_it.next()
            if asks and asks[-1][0] == ask.price: 
                asks[-1][1] += ask.peak_size
            else:
                if len(asks) == one_side_cap:
                    break
                asks.append([ask.price, ask.peak_size])

        if user == None:
            return bids, asks
        else:
            return user.get_orderbook(bids, asks)

u1 = User(1)
u2 = User(2)
u3 = User(3)
b = BackEnd()
b.add_user(u1)
b.add_user(u2)
b.add_order(u1, 'B', 50, 2)
b.add_order(u2, 'B', 50, 3)
b.add_order(u3, 'B', 51, 5)
# b.pull_buy_orders(u1)
print(u1.buys)
b.add_order(u2, 'S', 45, 3)
print(u1.buys)
# b.add_order(u2, 'S', 45, 3)

print(u2.pnl(52))
print(b.get_orderbook())
from ob.orderBook import OrderBook
from ob.common.order import Order

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
            self.order_to_user[bid_order_id].add_buy(trade_price, trade_quantity)
            self.order_to_user[ask_order_id].add_sell(trade_price, trade_quantity)


u1 = User(1)
u2 = User(2)
b = BackEnd()
b.add_user(u1)
b.add_user(u2)
b.add_order(u1, 'B', 50, 2)
b.add_order(u2, 'A', 45, 3)

print(u2.pnl(52))
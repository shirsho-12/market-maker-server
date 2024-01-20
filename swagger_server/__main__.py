#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_cors import CORS


def main():
    
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    CORS(app.app)
    app.add_api('swagger.yaml', arguments={'title': 'Market-Maker REST API'}, pythonic_params=True)
    # app.app.config['CORS_HEADERS'] = 'Content-Type'

    app.run(port=8080, debug=True,)
    print(f"Debug URL: {app.app.url_map}")
    # create globally available Backend object
    
    # u1 = User(1)
    # u2 = User(2)
    # u3 = User(3)
    # b = BackEnd()
    # b.add_user(u1)
    # b.add_user(u2)
    # b.add_order(u1, 'B', 50, 2)
    # b.add_order(u2, 'B', 50, 3)
    # b.add_order(u3, 'B', 51, 5)
    # # b.pull_buy_orders(u1)
    # print(u1.buys)
    # b.add_order(u2, 'S', 45, 3)
    # print(u1.buys)
    # # b.add_order(u2, 'S', 45, 3)

    # print(u2.pnl(53, binary = True))
    # print(b.get_orderbook())



if __name__ == '__main__':
    main()

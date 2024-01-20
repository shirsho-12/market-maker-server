from swagger_server.backend import BackEnd

global backend_object

backend_object = BackEnd()

backend_object.add_user("1")
backend_object.add_user("2")
backend_object.add_user("3")

backend_object.add_order(user_id="1", type="B", price=10, quantity=2)
backend_object.add_order(user_id="2", type="B", price=9, quantity=3)
backend_object.add_order(user_id="3", type="B", price=8, quantity=3)

backend_object.add_order(user_id="3", type="S", price=11, quantity=5)
backend_object.add_order(user_id="2", type="S", price=12, quantity=5)
backend_object.add_order(user_id="1", type="S", price=13, quantity=5)

from database import connect_to_database
from query_execution import execute_query


def main():
    host = "localhost"
    user = "root"
    password = "root"
    database = "pizzahut"
    connection = connect_to_database(host, user, password, database)
    query = input("Enter SQL query: ")

    execute_query(connection, query)


if __name__ == "__main__":
    main()


# select count(order_id) as total_orders from orders
# SELECT (order_details.quantity * pizzas.price) AS total_sales FROM order_details JOIN pizzas ON pizzas.pizza_id = order_details.pizza_id
# select pizza_types.name, pizzas.price from pizza_types join pizzas on pizza_types.pizza_type_id = pizzas.pizza_type_id order by pizzas.price desc limit 1
# select quantity, count(order_details_id) from order_details group by quantity
# SELECT pizzas.size, COUNT(order_details.order_details_id) FROM pizzas JOIN order_details ON pizzas.pizza_id = order_details.pizza_id GROUP BY pizzas.size;
# SELECT pizza_types.name, SUM(order_details.quantity) AS quantity FROM pizza_types JOIN pizzas ON pizza_types.pizza_type_id = pizzas.pizza_type_id JOIN order_details ON order_details.pizza_id = pizzas.pizza_id GROUP BY pizza_types.name ORDER BY quantity DESC LIMIT 5
# -------->Intermediate
# SELECT pizza_types.category, SUM(order_details.quantity) AS quantity FROM pizza_types JOIN pizzas ON pizza_types.pizza_type_id = pizzas.pizza_type_id JOIN order_details ON order_details.pizza_id = pizzas.pizza_id GROUP BY pizza_types.category ORDER BY quantity DESC 
# SELECT HOUR(TIME) AS hours, COUNT(order_id) AS total_order FROM orders GROUP BY HOUR(TIME)
# SELECT category, COUNT(NAME)FROM pizza_types GROUP BY category
# SELECT AVG(quantiy) FROM (SELECT orders.date, SUM(order_details.quantity)AS quantiy FROM orders JOIN order_details ON orders.order_id = order_details.order_id GROUP BY orders.date) AS order_quantity
# SELECT pizza_types.name, SUM(order_details.quantity * pizzas.price) AS revenue FROM pizza_types JOIN pizzas ON pizza_types.pizza_type_id = pizzas.pizza_id JOIN order_details ON order_details.pizza_id = pizzas.pizza_id GROUP BY pizza_types.name ORDER BY revenue;

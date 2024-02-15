import math

def calculate_distance(coord1, coord2):
    # Простое вычисление Евклидова расстояния
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def assign_orders(orders, couriers):
    assignments = []  # Список для сохранения назначений заказов курьерам

    for order in orders:
        best_distance = float('inf')
        best_courier_id = None

        for courier in couriers:
            distance_to_pickup = calculate_distance(courier['location'], order['pickup_location'])
            distance_to_delivery = calculate_distance(order['pickup_location'], order['delivery_location'])
            total_distance = distance_to_pickup + distance_to_delivery

            if total_distance < best_distance:
                best_distance = total_distance
                best_courier_id = courier['id']

        # Назначаем заказ лучшему курьеру и обновляем его местоположение
        assignments.append((best_courier_id, order['id']))
        for courier in couriers:
            if courier['id'] == best_courier_id:
                courier['location'] = order['delivery_location']
                break

    return assignments

# Пример использования
orders = [{'id': 1, 'pickup_location': (0, 0), 'delivery_location': (5, 5), 'cost': 100},
          {'id': 2, 'pickup_location': (9, 9), 'delivery_location': (6, 6), 'cost': 200}]
couriers = [{'id': 'a', 'location': (0, 0)},
            {'id': 'b', 'location': (10, 10)}]

assignments = assign_orders(orders, couriers)
print(assignments)
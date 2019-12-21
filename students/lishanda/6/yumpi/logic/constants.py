# -*- coding: utf-8 -*-

SUCCESS_CODE = 200
CREATED_CODE = 201
BAD_REQUEST_CODE = 400

SHORT_TIME = 40
LONG_TIME = 60

stats_dict = {
    'all': 2,
    'pizzas': {'1': 2, '2': 1, '3': 1},
    'statuses': {'ACCEPTED': 2, 'COOKING': 0, 'DELIVERY': 0, 'FINISHED': 0},
}
mod_stats_dict = {
    'all': 3,
    'pizzas': {'1': 2, '2': 2, '3': 1},
    'statuses': {'ACCEPTED': 3, 'COOKING': 0, 'DELIVERY': 0, 'FINISHED': 0},
}
default_dataset = {
    'ingredient': ['Cheese', 'Chicken', 'Tomato', 'Bacon'],
    'pizza': [
        ('Margaret', 100, [1]),
        ('Classic', 120, [1, 2]),
        ('Megameat', 140, [1, 2, 3, 4]),
    ],
    'order': [
        ([1, 2, 3], 'Nevskii pr., 12', 'customer@real.com'),
        ([1], 'Sovetkaja ul., 120', 'pizza@lover.ru'),
    ],
}
WORKDAY = {  # noqa: WPS407
    'start': 10,
    'end': 22,
    'midnight': 0,
}

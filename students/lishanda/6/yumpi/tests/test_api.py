# -*- coding: utf-8 -*-

from hypothesis.extra.django import TestCase

from yumpi.tests.data_helpers import create_test_data, default_dataset

SUCCESS_CODE = 200
CREATED_CODE = 201
BAD_REQUEST_CODE = 400


class TestGetPizzas(TestCase):
    """Testing :term:`Pizza` getting API."""

    def setUp(self) -> None:
        """Setting up database for testing purpose."""
        create_test_data(default_dataset)

    def test_pizza(self):
        """Checks accessibility of pizza API."""
        response = self.client.get(path='/api/pizza/')
        assert response.status_code == SUCCESS_CODE


class TestPostOrder(TestCase):
    """Testing :term:`Order` posting API."""

    def setUp(self) -> None:
        """Setting up database for testing purpose."""
        create_test_data(default_dataset)

    def test_correct_order(self):
        """Testing availability of :term:`Order` posting API."""
        post_data = {
            'pizzas': [1, 1, 1, 1, 1],
            'delivery_address': 'Birzhevaja line, 12',
            'customer_email': 'pizza@lover.ru',
        }
        response = self.client.post(path='/api/order/', data=post_data)
        assert response.status_code == CREATED_CODE

    def test_empty_order(self):
        """Testing placing empty :term:`Order`."""
        response = self.client.post(path='/api/order/')
        assert response.status_code == BAD_REQUEST_CODE

    def test_wrong_data(self):
        """Testing placing :term:`Order` of wrong format."""
        post_data = {
            'pizzas': '',
        }
        response = self.client.post(path='/api/order/', data=post_data)
        assert response.status_code == BAD_REQUEST_CODE

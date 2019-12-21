# -*- coding: utf-8 -*-

from datetime import date, timedelta

from hypothesis.extra.django import TestCase

from yumpi.logic.constants import (
    BAD_REQUEST_CODE,
    CREATED_CODE,
    SUCCESS_CODE,
    default_dataset,
    mod_stats_dict,
    stats_dict,
)
from yumpi.tests.data_test_helpers import create_test_data, create_test_order


class TestGetPizzas(TestCase):
    """Testing :term:`Pizza` getting API."""

    def setUp(self) -> None:
        """Setting up database for testing purpose."""
        create_test_data(default_dataset)

    def test_get(self):
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


class TestStatistics(TestCase):
    """Testing :term:`Order` statistics API."""

    def setUp(self) -> None:
        """Setting up database for testing purpose."""
        create_test_data(default_dataset)

    def test_loading(self):
        """Testing availability of statistics API."""
        response = self.client.get('/api/statistics/pizza')
        assert response.status_code == SUCCESS_CODE
        assert response.json() == stats_dict

    def test_updated(self):
        """Testing whether statistics changes with new :term:`Order`."""
        create_test_order([2], 'address', 'test@test.com')
        response = self.client.get('/api/statistics/pizza')
        assert response.status_code == SUCCESS_CODE
        assert response.json() == mod_stats_dict

    def test_old_orders(self):
        """Testing whether statistic counts old :term:`Order`."""
        old_date = date.today() - timedelta(days=2)
        old_date_two = date.today() - timedelta(days=100)
        create_test_order([2, 2, 2], 'test', 'test@test.com', str(old_date))
        create_test_order([1, 3], 'test', 'test2@test.com', str(old_date_two))
        create_test_order([1, 3], 'test', 'test2@test.com', str(old_date_two))

        response = self.client.get('/api/statistics/pizza')
        assert response.status_code == SUCCESS_CODE
        assert response.json() == stats_dict

# coding: utf-8
from __future__ import absolute_import

from pprint import pformat

from pyramid.response import Response
from pyramid.view import view_config


import logging
log = logging.getLogger(__name__)


@view_config(route_name='ping')
def ping(request):
    return Response('pong')


@view_config(route_name='feedback')
def feedback(request):
    log.info(pformat(request.json_body))
    return Response()


TAXES = {
    'DE': 20,
    'UK': 21,
    'FR': 20,
    'IT': 25,
    'ES': 19,
    'PL': 21,
    'RO': 20,
    'NL': 20,
    'BE': 24,
    'EL': 20,
    'CZ': 19,
    'PT': 23,
    'HU': 27,
    'SE': 23,
    'AT': 22,
    'BG': 21,
    'DK': 21,
    'FI': 17,
    'SK': 18,
    'IE': 21,
    'HR': 23,
    'LT': 23,
    'SI': 24,
    'LV': 20,
    'EE': 22,
    'CY': 21,
    'LU': 25,
    'MT': 20,
}


REDUCTIONS = [
    (50000, 15),
    (10000, 10),
    (7000, 7),
    (5000, 5),
    (1000, 3),
]


@view_config(route_name='order', request_method='POST', renderer='json')
def order(request):

    payload = request.json_body

    log.info(pformat(payload))

    quantities = payload['quantities']
    prices = payload['prices']
    country = payload['country']
    reduction = payload['reduction']

    total = apply_reduction(apply_taxes(sum_article_prices(quantities, prices), country), reduction)

    return {
        "total": total,
    }


def sum_article_prices(quantities, unit_prices):
    return sum(quantity * unit_price for quantity, unit_price in zip(quantities, unit_prices))


def apply_taxes(amount, country):
    return amount * (1.0 + (TAXES[country] / 100.0))


def apply_reduction(amount, reduction_type):

    if reduction_type == 'STANDARD':
        for threshold, reduction in REDUCTIONS:
            if amount >= threshold:
                return amount - (amount * reduction / 100.0)

    elif reduction_type == 'HALF PRICE':
        return amount / 2.0

    elif reduction_type == 'PAY THE PRICE':
        pass  # no reduction

    return amount

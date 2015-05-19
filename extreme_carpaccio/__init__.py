# coding: utf-8
from __future__ import absolute_import

from pyramid.config import Configurator


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_route('ping', '/ping')
    config.add_route('feedback', '/feedback')
    config.add_route('order', '/order')
    config.scan()
    return config.make_wsgi_app()

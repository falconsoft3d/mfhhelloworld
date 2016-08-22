# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Modulo Hola Mundo',
    'version': '1.0',
    'author': ['Marlon Falcon Hernandez'],
    'category': 'Tools',
    'summary': 'Ejemplo de un módulo de Odoo',
    'website': 'https://www.marlonfalcon.cl',
    'description': """
Ejemplo de Hola Mundo.
======================
Con este módulo mostraremos como hacer tu primer componente en odoo 9
    """,
    'depends': ['base'],
    'data': [
        'mfhhelloworld_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}

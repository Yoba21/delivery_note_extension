{
    'name': 'Delivery Note Extension',
    'version': '18.0.1.0',
    'author': 'Eyob',
    'category': 'Inventory',
    'summary': 'Add custom fields on DN',
    'description': """ """,
    'license': 'LGPL-3',
    'depends': [
        'stock', 'fleet', 'hr',
    ],
    'data': [
        'views/stock_picking_print_vehicle.xml',
        'report/stock_delivery_report_vehicle.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

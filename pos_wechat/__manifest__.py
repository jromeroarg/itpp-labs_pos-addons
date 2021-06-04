# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """WeChat Payments in POS""",
    "summary": """Support WeChat QR-based payments (scan and show)""",
    "category": "Point of Sale",
    # "live_test_url": "",
    "images": ["images/main.jpg"],
    "version": "12.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@itpp.dev",
    "website": "https://apps.odoo.com/apps/modules/12.0/pos_payment_wechat/",
    "license": "Other OSI approved licence",  # MIT
    "depends": [
        "wechat",
        "pos_qr_scan",
        "pos_qr_show",
        "pos_qr_payments",
        "pos_longpolling",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/assets.xml", "wizard/pos_payment_views.xml"],
    "demo": [],
    "qweb": ["static/src/xml/pos.xml"],
    "auto_install": False,
    "installable": True,
}

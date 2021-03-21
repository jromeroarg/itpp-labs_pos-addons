{
    "name": """Product Sets [POS-MS]""",
    "summary": """Synchronize product sets across several POSes""",
    "category": "Point of Sale",
    "images": ["images/pos_multi_session_menu_main.jpg"],
    "version": "12.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "apps@itpp.dev",
    "website": "https://github.com/itpp-labs/pos-addons#readme",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["pos_multi_session", "pos_menu"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/pos_menu_view.xml", "views/pos_multi_session_menu_template.xml"],
    "qweb": [],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": False,
}

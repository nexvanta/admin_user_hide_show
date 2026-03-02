{
    'name': 'Admin user hide and Show',
    'version': '19.0.1.0.0',
     'summary': 'Admin User Hide & Show is a powerful app designed to give superadmins and managers control over visibility of admin users in your system. With this app, you can easily hide or show selected admin accounts in various modules, enhancing security, privacy, and workflow clarity. Ideal for companies with multiple admins, it ensures sensitive user accounts are only visible when needed.',
    'description': """
         Many organizations face situations where not all admin accounts should be visible to regular users or even other admins. Admin User Hide & Show addresses this by allowing you to toggle the visibility of admin users across Odoo modules like Sales, Purchase, Inventory, and more.

        Whether you want to hide inactive admins, temporary users, or sensitive accounts, this app gives you a simple, intuitive interface to manage who can see what. All changes reflect immediately in the system and reports, ensuring seamless operations without compromising security.
    """,
    'author': 'NexvantaTech',
    'website': 'https://nexvantatech.com',
    'category': 'Tools',
    'depends': ['base'], 
    'data': [
       'views/res_users_view.xml',
       'security/ir_rule.xml',
    ],
    'uninstall_hook': 'uninstall_hook',
    
   'images': [
       'static/description/Banner.png',
       'static/description/1.png',
        'static/description/2.png',
        'static/description/3.png',
        'static/description/4.png',
        'static/description/5.png',
        'static/description/6.png',
        'static/description/7.png',
        'static/description/icon.png',
   ],

     "documentation": ["static/description/index.html"],
    'license': 'OPL-1',
    "live_test_url": "",
    'price': 2.00,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,

}

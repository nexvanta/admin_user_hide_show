from . import models
from odoo import api, SUPERUSER_ID

def uninstall_hook(*args, **kwargs):
   
    try:
        if args:
            env = args[0]
            if not hasattr(env, 'user'):
                cr = args[0]
                env = api.Environment(cr, SUPERUSER_ID, {})
            
            admins = env['res.users'].with_context(active_test=False).search([
                '|', ('id', 'in', [1, 2]), ('name', '=', 'Administrator')
            ])
            for admin in admins:
                if not admin.active:
                    admin.write({'active': True})
    except Exception:
        pass
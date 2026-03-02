from odoo import models, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        if not self.env.su:
            domain = domain or []
            domain += [('id', 'not in', [1, 2]), ('name', '!=', 'Administrator')]
        return super().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
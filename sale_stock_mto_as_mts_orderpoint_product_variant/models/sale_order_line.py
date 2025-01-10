# Copyright 2025 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_mto_orderpoint(self, product_id):
        orderpoint = super()._get_mto_orderpoint(product_id)

        if not product_id.is_mto:
            orderpoint.write({"active": False})

        return orderpoint

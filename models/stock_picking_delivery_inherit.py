from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    driver = fields.Many2one('hr.employee', string='Driver Name')
    vehicle = fields.Many2one('fleet.vehicle', string='Vehicle')

    currency_id = fields.Many2one(related='company_id.currency_id', readonly=True)
    due_amount = fields.Monetary(
        string='Due Amount',
        currency_field='currency_id',
        compute='_compute_due_amount'
    )

    def _compute_due_amount(self):
        """Compute due amount from sales order invoices"""
        for picking in self:
            total_due = 0.0

            # Get all sale orders from moves
            moves = picking.move_ids.filtered('sale_line_id')
            sale_orders = moves.mapped('sale_line_id.order_id')

            # Iterate through unique sale orders
            for order in sale_orders:
                # Get unpaid invoices
                unpaid_invoices = order.invoice_ids.filtered(
                    lambda inv: inv.state == 'posted' and inv.amount_residual > 0
                )
                # Sum residual amounts
                total_due += sum(unpaid_invoices.mapped('amount_residual'))

            picking.due_amount = total_due
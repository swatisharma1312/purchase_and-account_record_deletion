from odoo import api, fields, models, tools, _
import logging
_logger = logging.getLogger(__name__)



class PurchaseUnlinkData(models.Model):
    _inherit = 'purchase.order'

    def purchase_delete(self):
        purchase_data = self.env['purchase.order'].search([('state', 'in', ['draft', 'sent', 'cancel']), ('date_order', '<=', '2022-04-1')], limit =1)
        _logger.info(" purchase data:::::::::::%s",  purchase_data)

        for rec in purchase_data:
            rec.button_cancel()
            rec.unlink()

class AccounteUnlinkData(models.Model):
    _inherit = 'account.move'

    def account_delete(self):
        cancel_data = self.env['account.move'].search([('state', '=', 'cancel'), ('date', '<=', '2021-07-1')], limit=5)
        _logger.info("cancel_data:::::::::::%s", cancel_data)

        if cancel_data.invoice_line_ids:
            for rec in cancel_data:
                rec.button_draft()
                rec.write({'invoice_line_ids': [(6, 0, [])]})
                _logger.info("cancel_data:::::::::::%s", cancel_data)
            rec.button_cancel()





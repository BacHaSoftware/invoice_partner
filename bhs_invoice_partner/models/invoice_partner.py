# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"

    invoice_currency = fields.Many2one('res.currency', 'Invoice currency')
    num_invoice = fields.Integer('Number invoice')

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        res = super(AccountMove, self)._onchange_partner_id()
        # THAY ĐỔI ĐƠN VỊ TIỀN TỆ CỦA HÓA ĐƠN THEO KHÁCH HÀNG
        if self.partner_id and self.partner_id.invoice_currency:
            self.currency_id = self.partner_id.invoice_currency.id
        else:
            # NẾU KO CÓ CẤU HÌNH THÌ LẤY TIỀN TỆ CỦA CTY MÌNH
            journal = self._search_default_journal()
            self.currency_id = journal.currency_id or journal.company_id.currency_id

        # cập nhật đơn vị tiền tệ
        str_currency = self.currency_id.name
        all_bank_with_currency = self.env['res.partner.bank'].search([('currency_id.name', '=', str_currency)])
        if all_bank_with_currency:
            self.partner_bank_id = all_bank_with_currency[0]
            return {'domain': {'partner_bank_id': [('currency_id.name', '=', str_currency)]}}
        else:
            bank_no_currency = self.env['res.partner.bank'].search([('currency_id', '=', False)])
            if bank_no_currency:
                self.partner_bank_id = bank_no_currency[0]
            return {'domain': {'partner_bank_id': [('currency_id', '=', False)]}}

        return res

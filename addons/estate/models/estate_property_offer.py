from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer"
    _description = "房屋報價"

    price = fields.Float(
        string="報價",
        help="報價的名稱",
    )
    state = fields.Selection(
        string="報價狀態",
        help="報價的當前狀態",
        selection=[
            ("accepted", "接受"),
            ("rejected", "拒絕"),
        ],
        copy=False,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="客戶",
        help="選擇此報價的客戶",
        required=True,
    )
    property_id = fields.Many2one(
        comodel_name="estate_property",
        string="房屋",
        help="選擇此報價的房屋",
        required=True,
    )

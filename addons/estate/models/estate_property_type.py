from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate_property_type"
    _description = "房屋類型"

    name = fields.Char(
        string="類型名稱",
        required=True,
        help="房屋類型的名稱",
    )

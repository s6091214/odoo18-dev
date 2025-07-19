from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate_property_tag"
    _description = "房屋標籤"

    name = fields.Char(
        string="房屋標籤",
        help="房屋標籤的名稱",
        required=True,
    )

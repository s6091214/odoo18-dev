from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "房地產測試模組"

    name = fields.Char(string="名稱", required=True)
    description = fields.Text(string="描述")
    postcode = fields.Char(string="郵政編碼")
    date_availability = fields.Date(string="可用日期")
    expected_price = fields.Float(string="預期價格", required=True)
    selling_price = fields.Float(
        string="售價",
    )
    bedrooms = fields.Integer(string="臥室數")
    living_area = fields.Integer(string="客廳面積")
    facades = fields.Integer(string="外立面數")
    garage = fields.Boolean(string="車庫")
    garden = fields.Boolean(string="花園")
    garden_area = fields.Integer(string="花園面積")
    garden_orientation = fields.Selection(
        selection=[("north", "北"), ("south", "南"), ("east", "東"), ("west", "西")],
        string="花園方向",
    )

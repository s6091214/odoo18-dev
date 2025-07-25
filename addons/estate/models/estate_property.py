from odoo import fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "房地產測試模組"

    name = fields.Char(string="名稱", required=True, help="輸入房產的標題")
    description = fields.Text(string="描述", help="房產的詳細描述")
    postcode = fields.Char(string="郵政編碼")
    date_availability = fields.Date(
        string="可用日期",
        copy=False,
        default=lambda self: datetime.now() + relativedelta(months=3),
    )
    expected_price = fields.Float(string="預期價格", required=True)
    selling_price = fields.Float(string="售價", readonly=True, copy=False)
    bedrooms = fields.Integer(string="臥室數", default=2)
    living_area = fields.Integer(string="坪數", help="房屋的實際使用面積")
    facades = fields.Integer(string="立面數")
    garage = fields.Boolean(string="車庫")
    garden = fields.Boolean(string="花園")
    garden_area = fields.Integer(string="花園面積")
    garden_orientation = fields.Selection(
        selection=[("north", "北"), ("south", "南"), ("east", "東"), ("west", "西")],
        string="花園方向",
    )
    active = fields.Boolean(string="啟用", default=True, help="是否啟用此房產")
    state = fields.Selection(
        [
            ("new", "新建"),
            ("offer_received", "已收到報價"),
            ("offer_accepted", "報價已接受"),
            ("sold", "已售出"),
            ("cancelled", "已取消"),
        ],
        string="狀態",
        default="new",
        help="房產的當前狀態",
        required=True,
        copy=False,
    )
    property_type_id = fields.Many2one(
        comodel_name="estate_property_type",
        string="房屋類型",
        help="選擇此房產的類型",
        required=True,
    )
    buyer_id = fields.Many2one(
        comodel_name="res.partner",
        string="買家",
        help="選擇此房產的買家",
        copy=False,
    )
    salesperson_id = fields.Many2one(
        comodel_name="res.users",
        string="銷售人員",
        help="負責此房產的銷售人員",
        default=lambda self: self.env.user,
        copy=False,
    )
    tag_ids = fields.Many2many(
        comodel_name="estate_property_tag",
        string="房屋標籤",
        help="為此房產添加標籤",
    )
    offer_ids = fields.One2many(
        comodel_name="estate_property_offer",
        inverse_name="property_id",
        string="房屋報價",
        help="此房產的所有報價",
    )

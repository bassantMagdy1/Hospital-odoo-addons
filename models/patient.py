from odoo import models,fields


class Hmspatient(models.Model):
    _name = 'hms.patient'


    firstname = fields.Char()
    lastname = fields.Char()
    birthdate = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a','A',),
        ('b', 'B',),
        ('ab', 'AB',),
        ('o', 'O',),
    ])
    pcr = fields.Boolean()
    age = fields.Integer()
    avatar = fields.Image()
    address = fields.Text()



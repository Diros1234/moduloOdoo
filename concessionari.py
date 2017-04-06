from openerp import models,fields
class concessionari_mecanic(models.Model):
	_name='concessionari.mecanic'
	nom=fields.Char('Nombre',size=100,required=True)
	cognom=fields.Char('Cognoms',size=100)
	telefon=fields.Integer('Telefono',size=9)
	_rec_name='nom'

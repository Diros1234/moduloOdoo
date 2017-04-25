from openerp import models,fields
class concessionari_mecanic(models.Model):
	#Needed add codi with serial_number at this line
	_name='concessionari.mecanic'
	codi = fields.Integer('codi',required=True)
	nom=fields.Char('Nombre',size=50)
	cognom=fields.Char('Cognoms',size=50)
	telefon=fields.Integer('Telefono',size=9)
	#the rec_name should be 'codi' with serial number sequence
	_rec_name='codi'
class concessionari_revisio(models.Model):
	_name='concessionari.revisio'
	data_revisio=fields.Date('Data revisio')
	#Make table 'Revisions' that contains primary key of 'class mecanic' and 'class cotxe'
	mecanic=fields.Many2one('concessionari.mecanic','Mecanics',ondelete='cascade')
	cotxe=fields.Many2one('concessionari.cotxe','Cotxes',ondelete='cascade')
class concessionari_cotxe(models.Model):
	_name='concessionari.cotxe'
	matricula = fields.Char('Matricula',size=7)
	marca = fields.Char('Marca',size=20)
	model = fields.Char('Modelo',size=20)
	nou = fields.Boolean('Nou')
	preu = fields.Float('Preu')
	km = fields.Integer('km')
	_rec_name = 'matricula'
	def change_color(self):
		for record in self:
			if record.nou==True:
				record.colorKanban=2
                        elif record.nou==False:
                               record.colorKanban=4
        colorKanban=fields.Integer('Color Index',compute='change_color')
class concessionari_compra(models.Model):
	_name = 'concessionari.compra'
	client = fields.Many2one('concessionari.client','Clientes',ondelete='cascade')
	cotxe  = fields.Many2one('concessionari.cotxe','Cotxes',ondelete='cascade')
	data=fields.Datetime('Fecha de compra')
	frase=fields.Char('identificadores')
class concessionari_client(models.Model):
	_name = 'concessionari.client'
	codi = fields.Integer('Codi')
	nom =fields.Char('Nombre',size=30)
	cognoms =fields.Char('Cognom',size=50)
	telefon = fields.Char('Telefon',size=9)
	venedor =fields.Many2one('concessionari.venedor','Venedors',ondelete='cascade')
	_rec_name='codi'
class concessionari_venedor(models.Model):
	_name = 'concessionari.venedor'
	codi = fields.Integer('Codi')
	nom = fields.Char('Nom',size=30)
	cognoms = fields.Char('Cognom',size=50)
	telefon = fields.Char('Telefon',size=9)
	_rec_name='codi'

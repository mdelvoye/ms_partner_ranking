# coding: utf-8
from openerp import api, models, fields

class res_partner(models.Model):
    _inherit = 'res.partner'
    _description = "Partner"
    
    x_ranking = fields.Selection([
                                  ('0', '0'),
                                  ('1', '1'),
                                  ('2', '2'),
                                  ('3', '3'),
                                  ('4', '4'),
                                  ('5', '5'),
                                  ], 'Ranking')
    
    z_ranking = fields.Html(string='Ranking', compute='_get_ranking', readonly=True)

    @api.one
    @api.depends('x_ranking')
    def _get_ranking(self):
        starOff = "<span><img src='/web/static/src/img/icons/star-off.png' width='16' height='16' class='oe_dashboard_selected_layout'/></span>"
        starOn = "<span><img src='/web/static/src/img/icons/star-on.png' width='16' height='16' class='oe_dashboard_selected_layout'/></span>"
        
        if self.x_ranking=='1':
            html=starOn + starOff + starOff + starOff+ starOff 
        elif self.x_ranking=='2':
            html=starOn + starOn + starOff + starOff+ starOff 
        elif self.x_ranking=='3':   
            html=starOn + starOn + starOn +  starOff+ starOff 
        elif self.x_ranking=='4':   
            html=starOn + starOn + starOn +  starOn+ starOff 
        else: 
            html=starOff + starOff + starOff  + starOff+ starOff 

        self.z_ranking = html
res_partner()
    
    




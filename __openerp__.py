# -*- coding: utf-8 -*-
{
    "name" : "MS Partner Ranking",
    "version" : "9.0.1.0.1",
    "category" : "Base",
    'author': u'Misyl Services',
    'description':'This module adds ranking, warning for Partners. MS Core is necessary to work ',
    'summary' : 'This module adds a ranking for Partners',
    'website' : 'http://www.misyl-services.com',

    'depends' : ['base','ms_core'],
    "data" : [
              'views/res_partner_view.xml',
              'views/ms_partner_ranking.xml',
             ],
    'installable': True,
    'auto_install': False,
}

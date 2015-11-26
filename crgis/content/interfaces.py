from plone.directives import form


class IBiXieWu(form.Schema):
    """BiXieWu Type"""
    form.model('models/bixiewu.xml')

class ITheater(form.Schema):
    """Theater Type"""
    form.model('models/theater.xml')


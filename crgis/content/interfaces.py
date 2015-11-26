from plone.directives import form


class IBiXieWu(form.Schema):
    """BiXieWu Type"""
    form.model('models/bixiewu.xml')


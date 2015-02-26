from five import grok
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from plone.directives import dexterity, form
from plone.indexer import indexer

from zope import schema
from plone.app.textfield import RichText

from crgis.content import MessageFactory as _


# Interface class; used to define content-type schema.

class ITheater(form.Schema):
    """Theater Type
    """
    form.model("models/theater.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Theater(dexterity.Container):
    grok.implements(ITheater)
    
    # Add your class methods and properties here

@indexer(ITheater)
def lcityIndexer(obj):
    if len(obj.location) >= 3:
        return obj.location[:3]
    else:
        return None
grok.global_adapter(lcityIndexer, name='lcity')

# View class
# The view will automatically use a similarly named template in
# theater_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(ITheater)
    grok.require('zope2.View')
    grok.name('view')

    def t_title(self, value):
        if value in ('movie', 'mixed', 'opera'):
            factory = getUtility(IVocabularyFactory, 'theater.function')
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        else:
            return None


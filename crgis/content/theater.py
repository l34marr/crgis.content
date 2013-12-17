from five import grok
from plone.directives import dexterity, form
from plone.indexer import indexer

from zope import schema
from plone.app.textfield import RichText

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from crgis.content import MessageFactory as _

function = SimpleVocabulary([
    SimpleTerm(value=u'movie', title=_(u'Moive Theater')),
    SimpleTerm(value=u'mixed', title=_(u'Mixed Theater')),
    SimpleTerm(value=u'opera', title=_(u'Opera Theater'))
])


# Interface class; used to define content-type schema.

class ITheater(form.Schema):
    """
    CRGIS Theater Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/theater.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/theater.xml")

    description = schema.Text(
        title=_(u"Administrative Area"),
        required=False,
    )

    title = schema.TextLine(
        title=_(u'theater_title', default=u"Title"),
    )

    address = schema.TextLine(
        title=_(u"Address"),
        required=False,
    )

    purpose = schema.TextLine(
        title=_(u"Purpose"),
        required=False,
    )

    completed = schema.Date(
        title=_(u"Completed Date"),
        required=False,
    )

    launched = schema.Date(
        title=_(u"Launched Date"),
        required=False,
    )

    updated = schema.Date(
        title=_(u"Last Updated"),
        required=False,
    )

    funding = RichText(
        title=_(u"Construction Funds"),
        required=False,
    )

    history = RichText(
        title=_(u"History"),
        required=False,
    )

    narrative = RichText(
        title=_(u"Narrative"),
        required=False,
    )

    function = schema.Choice(
        title=_(u"Function"),
        vocabulary=function,
        required=False,
    )

    owner = schema.TextLine(
        title=_(u"Owner"),
        required=False,
    )

    operator = schema.TextLine(
        title=_(u"Operator"),
        required=False,
    )

    affairs = schema.TextLine(
        title=_(u"Affairs"),
        required=False,
    )

    contract = schema.TextLine(
        title=_(u"Contract"),
        required=False,
    )

    operating = RichText(
        title=_(u"Operating"),
        required=False,
    )

    program = RichText(
        title=_(u"Program"),
        required=False,
    )

    remark = RichText(
        title=_(u"Remark"),
        required=False,
    )

    reference = RichText(
        title=_(u"Reference"),
        required=False,
    )


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


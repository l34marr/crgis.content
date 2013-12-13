from five import grok
from plone.directives import dexterity, form
from plone.indexer import indexer

from zope import schema

from plone.app.textfield import RichText

from crgis.content import MessageFactory as _

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

    title = schema.TextLine(
        title=_(u'theater_title', default=u"Title"),
    )

    description = schema.Text(
        title=_(u"Administrative Area"),
        required=False,
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

    narrative = RichText(
        title=_(u"Narrative"),
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


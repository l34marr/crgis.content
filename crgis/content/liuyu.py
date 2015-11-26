from five import grok
from plone.directives import dexterity, form

from zope import schema
from plone.app.textfield import RichText
from plone.z3cform.textlines import TextLinesFieldWidget

from collective import dexteritytextindexer

from crgis.content import _


# Interface class; used to define content-type schema.

class ILiuYu(form.Schema):
    """
    CRGIS LiuYu Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/tree.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/liuyu.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    year_start = schema.TextLine(
        title=_(u"Start Year"),
        required=False,
    )

    month_start = schema.TextLine(
        title=_(u"Start Month"),
        required=False,
    )

    year_end = schema.TextLine(
        title=_(u"End Year"),
        required=False,
    )

    month_end = schema.TextLine(
        title=_(u"End Month"),
        required=False,
    )

    country = schema.TextLine(
        title=_(u"Country"),
        required=False,
    )

    state = schema.TextLine(
        title=_(u"State"),
        required=False,
    )

    city = schema.TextLine(
        title=_(u"City"),
        required=False,
    )

    county = schema.TextLine(
        title=_(u"County"),
        required=False,
    )

    river = schema.List(
        title=_(u"River"),
        value_type=schema.TextLine(),
        required=False,
    )
    form.widget(river=TextLinesFieldWidget)

    mountain = schema.List(
        title=_(u"Mountain"),
        value_type=schema.TextLine(),
        required=False,
    )
    form.widget(mountain=TextLinesFieldWidget)

    monastery = schema.List(
        title=_(u"Monastery"),
        value_type=schema.TextLine(),
        required=False,
    )
    form.widget(monastery=TextLinesFieldWidget)

    tomb = schema.List(
        title=_(u"Tomb"),
        value_type=schema.TextLine(),
        required=False,
    )
    form.widget(tomb=TextLinesFieldWidget)

    castle = schema.List(
        title=_(u"Castle"),
        value_type=schema.TextLine(),
        required=False,
    )
    form.widget(castle=TextLinesFieldWidget)

    fortress = schema.List(
        title=_(u"Fortress"),
        value_type=schema.TextLine(),
        required=False,
    )
    form.widget(fortress=TextLinesFieldWidget)

    relices = schema.TextLine(
        title=_(u"Relices"),
        required=False,
    )

    buildings = schema.TextLine(
        title=_(u"Buildings"),
        required=False,
    )

    legend = schema.TextLine(
        title=_(u"Legend"),
        required=False,
    )

    dexteritytextindexer.searchable('people')
    people = RichText(
        title=_(u"Historic People"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    tongjian = RichText(
        title=_(u"ZiZhi TongJian"),
        required=False,
    )

    ref_name = schema.TextLine(
        title=_(u"Reference Name"),
        required=False,
    )

    ref_text = RichText(
        title=_(u"Reference Text"),
        required=False,
    )

    note = RichText(
        title=_(u"Note"),
        required=False,
    )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class LiuYu(dexterity.Container):
    grok.implements(ILiuYu)
    
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# tree_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(ILiuYu)
    grok.require('zope2.View')
    grok.name('view')


from zope.interface import Interface
from zope import schema
from plone.autoform import directives as form
from plone.namedfile import field as namedfile
from plone.app.textfield import RichText as RichTextField
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel.interfaces import FIELDSETS_KEY
from plone.supermodel.model import Fieldset
from crgis.content import _


class IBiXieWu(Interface):
    """BiXieWu Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    data_src = schema.TextLine(
        title=_(u"Data Source"),
        required=False,
    )
    lct_cou = schema.TextLine(
        title=_(u"County"),
        required=False,
    )
    lct_tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
    )
    lct_vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
    )
    coordinate = schema.TextLine(
        title=_(u"Coordinate Type"),
        required=False,
    )
    btype = schema.TextLine(
        title=_(u"BiXieWu Type"),
        required=False,
    )
    era = schema.TextLine(
        title=_(u"Common Era"),
        required=False,
    )
    era_ref = RichTextField(
        title=_(u"Era Reference"),
        required=False,
    )
    facing = schema.TextLine(
        title=_(u"Facing"),
        required=False,
    )
    material = schema.TextLine(
        title=_(u"Material"),
        required=False,
    )
    volumn = schema.TextLine(
        title=_(u"Volumn"),
        required=False,
    )
    localtional = schema.TextLine(
        title=_(u"Localtional Attribute"),
        required=False,
    )
    purpose = schema.Tuple(
        title=_(u"Purpose"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    worship = RichTextField(
        title=_(u"Worship Description"),
        required=False,
    )
    r_temples = RelationList(
        title=_(u"Related Temples"),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder()),
        required=False,
    )
    village = schema.TextLine(
        title=_(u"Village Name"),
        required=False,
    )
    color = schema.TextLine(
        title=_(u"Color"),
        required=False,
    )
    genre = schema.TextLine(
        title=_(u"Genre"),
        required=False,
    )
    posture = schema.TextLine(
        title=_(u"Posture"),
        required=False,
    )
    gender = schema.TextLine(
        title=_(u"Gender"),
        required=False,
    )
    shi_d = schema.TextLine(
        title=_(u"ShiZi Depth"),
        required=False,
    )
    shi_w = schema.TextLine(
        title=_(u"ShiZi Width"),
        required=False,
    )
    shi_h = schema.TextLine(
        title=_(u"ShiZi Height"),
        required=False,
    )
    shi_t = schema.TextLine(
        title=_(u"ShiZi Head"),
        required=False,
    )
    base_l = schema.TextLine(
        title=_(u"Base Length"),
        required=False,
    )
    base_w = schema.TextLine(
        title=_(u"Base Width"),
        required=False,
    )
    base_h = schema.TextLine(
        title=_(u"Base Height"),
        required=False,
    )

fieldset = Fieldset('fengshiye', label=_(u'FengShiYe'), fields=['village', 'color', 'genre', 'posture', 'gender', 'shi_d', 'shi_w', 'shi_h', 'shi_t', 'base_l', 'base_w', 'base_h'])
IBiXieWu.setTaggedValue(FIELDSETS_KEY, [fieldset])


class IPhoto(Interface):
    """Photo Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    image = namedfile.NamedBlobImage(
        title=_(u"Image"),
    )
    category = schema.Tuple(
        title=_(u"Category"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    attachesTo = schema.Tuple(
        title=_(u"Attached To"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    cou = schema.TextLine(
        title=_(u"County"),
        required=False,
    )
    tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
    )
    vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
    )
    date = schema.TextLine(
        title=_(u"Photo Date"),
        required=False,
    )
    owner_name = schema.TextLine(
        title=_(u"Owner Name"),
        required=False,
    )
    owner_org = schema.TextLine(
        title=_(u"Owner Organization"),
        required=False,
    )
    owner_title = schema.TextLine(
        title=_(u"Owner Title"),
        required=False,
    )
    reference = RichTextField(
        title=_(u"Reference"),
        required=False,
    )


from zope import schema
from plone.autoform import directives as form
from plone.namedfile import field as namedfile
from plone.app.textfield import RichText as RichTextField
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from crgis.content import _


class ITemple(model.Schema):
    """Temple Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    data_src = schema.Choice(
        title=_(u"Data Source"),
        required=False,
        vocabulary=u"data_src",
    )
    coordinate = schema.Choice(
        title=_(u"Coordinate Type"),
        required=False,
        vocabulary=u"coordinate",
    )
    facing = schema.TextLine(
        title=_(u"Sitting Facing"),
        required=False,
    )
    deity_host = schema.Tuple(
        title=_(u"Deity Host"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    deity_host_o = schema.TextLine(
        title=_(u"Deity Host Other"),
        required=False,
    )
    deity_host_a = schema.TextLine(
        title=_(u"Deity Host Alias"),
        required=False,
    )
    deity_company = schema.Tuple(
        title=_(u"Deity Company"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    religion = schema.Choice(
        title=_(u"Religion Type"),
        required=False,
        vocabulary=u"religion",
    )
    religion_o = schema.TextLine(
        title=_(u"Religion Type Other"),
        required=False,
    )
    building = schema.Choice(
        title=_(u"Building Type"),
        required=False,
        vocabulary=u"building",
    )
    building_o = schema.TextLine(
        title=_(u"Building Type Other"),
        required=False,
    )
    registered = schema.TextLine(
        title=_(u"Registered Name"),
        required=False,
    )
    funding = schema.Choice(
        title=_(u"Funding Type"),
        required=False,
        vocabulary=u"funding",
    )
    organizing = schema.Choice(
        title=_(u"Organizing Type"),
        required=False,
        vocabulary=u"organizing",
    )
    organizing_o = schema.TextLine(
        title=_(u"Organizing Type Other"),
        required=False,
    )
    address = schema.TextLine(
        title=_(u"Address"),
        required=False,
    )
    in_charge = schema.TextLine(
        title=_(u"Person In Charge"),
        required=False,
    )
    tel = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
    )
    homepage = schema.TextLine(
        title=_(u"Homepage"),
        required=False,
    )
    era = schema.TextLine(
        title=_(u"Estimated Earliest Founding Year"),
        required=False,
    )
    era_end = schema.TextLine(
        title=_(u"Estimated Latest Founding Year"),
        required=False,
    )
    year_accuracy = schema.Choice(
        title=_(u"Year Accuracy"),
        required=False,
        vocabulary=u"year_accuracy",
    )
    history = RichTextField(
        title=_(u"Establishment History"),
        required=False,
    )
    era_1 = schema.TextLine(
        title=_(u"Established Year by Taiwan Temple Collection"),
        required=False,
    )
    era_2 = schema.TextLine(
        title=_(u"Established Year by Taiwan Temple Overview"),
        required=False,
    )
    era_ref = RichTextField(
        title=_(u"References on Establishment"),
        required=False,
    )
    deity_accompany = RichTextField(
        title=_(u"Deities Accompany"),
        required=False,
    )
    worship = RichTextField(
        title=_(u"Worship"),
        required=False,
    )
    introduction = RichTextField(
        title=_(u"Introduction"),
        required=False,
    )
    overview = RichTextField(
        title=_(u"Building Overview"),
        required=False,
    )
    antiquity = RichTextField(
        title=_(u"Antiquity"),
        required=False,
    )
    narrate = RichTextField(
        title=_(u"Narrate"),
        required=False,
    )
    non_narrate = RichTextField(
        title=_(u"Non Narrate"),
        required=False,
    )
    academic = RichTextField(
        title=_(u"Academic Works"),
        required=False,
    )
    literature = RichTextField(
        title=_(u"Literature Reference"),
        required=False,
    )
    fill_in = schema.TextLine(
        title=_(u"Filling Person"),
        required=False,
    )
    fill_date = schema.TextLine(
        title=_(u"Filling Date"),
        required=False,
    )
    model.fieldset('appendix', label=_(u'Appendix'), fields=['jstq', 'jstq_o', 'jsfw', 'xyfw', 'flxt', 'flxt_o', 'ymmy', 'ymmy_o', 'xhly', 'xhly_o', 'nlqs', 'nlqs_o', 'wyxx', 'wyxx_o', 'medicine', 'luck', 'organization', 'desc_o'])
    jstq = schema.Tuple(
        title=_(u"JiSiZuQun"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"jstq",
        ),
        missing_value=()
    )
    jstq_o = schema.TextLine(
        title=_(u"JiSiZuQun Other"),
        required=False,
    )
    jsfw = RichTextField(
        title=_(u"JiSiFanWei"),
        required=False,
    )
    xyfw = RichTextField(
        title=_(u"XinYangFangWei"),
        required=False,
    )
    flxt = schema.Tuple(
        title=_(u"FenLingXiTong"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"flxt",
        ),
        missing_value=()
    )
    flxt_o = schema.TextLine(
        title=_(u"FenLingXiTong Other"),
        required=False,
    )
    ymmy = schema.Tuple(
        title=_(u"YiMingMiaoYu"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"ymmy",
        ),
        missing_value=()
    )
    ymmy_o = schema.TextLine(
        title=_(u"YiMingMiaoYu Other"),
        required=False,
    )
    xhly = schema.Tuple(
        title=_(u"XiangHuoLaiYuan"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"xhly",
        ),
        missing_value=()
    )
    xhly_o = schema.TextLine(
        title=_(u"XiangHuoLaiYuan Other"),
        required=False,
    )
    nlqs = schema.Tuple(
        title=_(u"NianLiQingSheng"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"nlqs",
        ),
        missing_value=()
    )
    nlqs_o = schema.TextLine(
        title=_(u"NianLiQingSheng Other"),
        required=False,
    )
    wyxx = schema.Tuple(
        title=_(u"WangYeXianXiang"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"wyxx",
        ),
        missing_value=()
    )
    wyxx_o = schema.TextLine(
        title=_(u"WangYeXianXiang Other"),
        required=False,
    )
    medicine = schema.Tuple(
        title=_(u"Medicine Divination"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"medicine",
        ),
        missing_value=()
    )
    luck = schema.Tuple(
        title=_(u"Luck Divination"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"luck",
        ),
        missing_value=()
    )
    organization = RichTextField(
        title=_(u"Believer Organization"),
        required=False,
    )
    desc_o = RichTextField(
        title=_(u"Description Other"),
        required=False,
    )
    model.fieldset('wangye', label=_(u'WangYe'), fields=['wysm', 'yswt', 'dtxs', 'freq', 'wttz', 'swxs', 'ysgs'])
    wysm = schema.TextLine(
        title=_(u"WangYe Name"),
        required=False,
    )
    yswt = schema.TextLine(
        title=_(u"YungS WangTsuan"),
        required=False,
    )
    dtxs = schema.Tuple(
        title=_(u"DaiTien XuanSho"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    freq = schema.Tuple(
        title=_(u"Frequence"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    wttz = schema.Tuple(
        title=_(u"WangTsuan Material"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    swxs = schema.TextLine(
        title=_(u"SungWang XingShi"),
        required=False,
    )
    ysgs = RichTextField(
        title=_(u"YSGS"),
        required=False,
    )


class IBiXieWu(model.Schema):
    """BiXieWu Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    data_src = schema.Choice(
        title=_(u"Data Source"),
        required=False,
        vocabulary=u'data_src',
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
        title=_(u"BiXieWu_Type"),
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
    establishment = RichTextField(
        title=_(u"Establishment Description"),
        required=False,
    )
    spatial = RichTextField(
        title=_(u"Spatial Attribute"),
        required=False,
    )
    environment = RichTextField(
        title=_(u"Environment Description"),
        required=False,
    )
    reference = RichTextField(
        title=_(u"Reference"),
        required=False,
    )
    remark = RichTextField(
        title=_(u"Remark"),
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
    model.fieldset('fengshiye', label=_(u'FengShiYe'), fields=['village', 'color', 'genre', 'posture', 'gender', 'shi_d', 'shi_w', 'shi_h', 'shi_t', 'base_l', 'base_w', 'base_h'])
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


class IPhoto(model.Schema):
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
    lng = schema.TextLine(
        title=_(u"Longtitude"),
        required=False,
    )
    lat = schema.TextLine(
        title=_(u"Latitude"),
        required=False,
    )
    year = schema.TextLine(
        title=_(u"Photo Year"),
        required=False,
    )
    month = schema.TextLine(
        title=_(u"Photo Month"),
        required=False,
    )
    day = schema.TextLine(
        title=_(u"Photo Day"),
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


class IPilgrimage(model.Schema):
    """Pilgrimage Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    body = RichTextField(
        title=_(u"Body"),
        required=False,
    )


class ISchedule(model.Schema):
    """Schedule Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    body = RichTextField(
        title=_(u"Body"),
        required=False,
    )
    temples = RelationList(
        title=_(u"Related Temples"),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=u"Related Temple",
            source=ObjPathSourceBinder()
        ),
    )


class IBuddhist(model.Schema):
    """Buddhist Type"""
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    area1 = schema.TextLine(
        title=_(u"1st-level Administrative Area"),
        required=False,
    )
    area2 = schema.TextLine(
        title=_(u"2nd-level Adminstrative Area"),
        required=False,
    )
    category = schema.Tuple(
        title=_(u"Category"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )



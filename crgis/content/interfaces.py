from zope import schema
from plone.autoform import directives
from plone.namedfile import field as namedfile
from plone.app.textfield import RichText as RichTextField
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.vocabularies.catalog import CatalogSource
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
        value_type=schema.Choice(
            vocabulary=u'deity_name',
        ),
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
        value_type=schema.Choice(
            vocabulary=u'deity_name',
        ),
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
    coordinate = schema.Choice(
        title=_(u"Coordinate Type"),
        required=False,
        vocabulary=u"coordinate",
    )
    btype = schema.Choice(
        title=_(u"BiXieWu_Type"),
        required=False,
        vocabulary=u"bixiewu",
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
    material = schema.Choice(
        title=_(u"Material"),
        required=False,
        vocabulary=u"material",
    )
    volumn = RichTextField(
        title=_(u"Volumn"),
        required=False,
    )
    localtional = schema.Choice(
        title=_(u"Locational Attribute"),
        required=False,
        vocabulary=u"locational",
    )
    purpose = schema.Tuple(
        title=_(u"Purpose"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"purpose",
        ),
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
        title=_(u"Environmental Description"),
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
            source=CatalogSource(Type='Temple')
        ),
        required=False,
    )
    directives.widget(
        'r_temples',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
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
    genre = schema.Choice(
        title=_(u"Genre"),
        required=False,
        vocabulary=u"genre",
    )
    posture = schema.Choice(
        title=_(u"Posture"),
        required=False,
        vocabulary=u"posture",
    )
    gender = schema.Choice(
        title=_(u"Gender"),
        required=False,
        vocabulary=u"gender",
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
        value_type=schema.Choice(
            vocabulary=u"category",
        ),
        missing_value=()
    )
    attachesTo = schema.Tuple(
        title=_(u"Attached To"),
        required=False,
        value_type=schema.Choice(
            vocabulary=u"attachesTo",
        ),
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
        default=[],
        value_type=RelationChoice(
            title=u'Related Temple',
            source=CatalogSource(Type='Temple')
        ),
        required=False,
    )
    directives.widget(
        'temples',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
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


class IDaoShi(model.Schema):
    """DaoShi Type"""
    title = schema.TextLine(
        title=_(u"DaoShi Name"),
        required=False,
    )
    description = schema.Text(
        title=_(u"DaoShi Other Name"),
        required=False,
    )
    birth = schema.TextLine(
        title=_(u"Birth Year"),
        required=False,
    )
    addr = schema.TextLine(
        title=_(u"Address"),
        required=False,
    )
    tel = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
    )
    dao_hao = schema.TextLine(
        title=_(u"Dao Hao"),
        required=False,
    )
    fa_hao = schema.TextLine(
        title=_(u"Fa Hao"),
        required=False,
    )
    dao_tan = schema.TextLine(
        title=_(u"Dao Tan"),
        required=False,
    )
    dao_zi = schema.TextLine(
        title=_(u"Dao Zi"),
        required=False,
    )
    benmin = schema.TextLine(
        title=_(u"BenMin"),
        required=False,
    )
    alt_nm = schema.TextLine(
        title=_(u"Alt Name"),
        required=False,
    )
    shchn = RelationList(
        title=_(u"ShiCheng List"),
        default=[],
        value_type=RelationChoice(
            title=u'ShiCheng',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'shchn',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    shotu = RelationList(
        title=_(u"ShouTu List"),
        default=[],
        value_type=RelationChoice(
            title=u'ShouTu',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'shotu',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    zouzhi = RichTextField(
        title=_(u"ZouZhi"),
        required=False,
    )
    intro = RichTextField(
        title=_(u"Introduction"),
        required=False,
    )
    service = RichTextField(
        title=_(u"Service"),
        required=False,
    )
    jngchng = RelationList(
        title=_(u"JingChang FuWu"),
        default=[],
        value_type=RelationChoice(
            title=u'JingChang',
            source=CatalogSource(Type='Temple')
        ),
        required=False,
    )
    directives.widget(
        'jngchng',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    zhumiao = RelationList(
        title=_(u"ZhuMiao List"),
        default=[],
        value_type=RelationChoice(
            title=u'ZhuMiao',
            source=CatalogSource(Type='Temple')
        ),
        required=False,
    )
    directives.widget(
        'zhumiao',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    yishi = RichTextField(
        title=_(u"YiShi"),
        required=False,
    )
    hzds = RelationList(
        title=_(u"HeZuo DaoShi"),
        default=[],
        value_type=RelationChoice(
            title=u'DaoShi',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    hzys = RichTextField(
        title=_(u"HeZuo YueShi"),
        required=False,
    )
    hzhz = RichTextField(
        title=_(u"HeZuo HuZhi"),
        required=False,
    )
    data_src = schema.Tuple(
        title=_(u"Data Source"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'data_src',
        AjaxSelectFieldWidget,
        vocabulary='crgis.data_src'
    )
    coordinate = schema.Tuple(
        title=_(u"Coordinate Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'coordinate',
        AjaxSelectFieldWidget,
        vocabulary='crgis.coordinate'
    )
    df_type = schema.Tuple(
        title=_(u"DaoFaTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'df_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.df_type'
    )
    dt_type = schema.Tuple(
        title=_(u"DaoTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'dt_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.dt_type'
    )
    ft_type = schema.Tuple(
        title=_(u"FaTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'ft_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.ft_type'
    )
    df_attr = schema.Tuple(
        title=_(u"DaoFaTan Attribute"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'df_attr',
        AjaxSelectFieldWidget,
        vocabulary='dao.df_attr'
    )
    academic = RichTextField(
        title=_(u"Academic Works"),
        required=False,
    )
    literature = RichTextField(
        title=_(u"Literature Reference"),
        required=False,
    )

class IDaoFaTan(model.Schema):
    """DaoFaTan Type"""
    title = schema.TextLine(
        title=_(u"DaoFaTan Name"),
        required=False,
    )
    description = schema.Text(
        title=_(u"DaoFaTan Other Name"),
        required=False,
    )
    birth = schema.TextLine(
        title=_(u"Establish Year"),
        required=False,
    )
    chngli = schema.Text(
        title=_(u"Establish"),
        required=False,
    )
    chlirn = RelationList(
        title=_(u"ChuangLiRen List"),
        default=[],
        value_type=RelationChoice(
            title=u'ChuangLiRen',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'chlirn',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    fuzeren = RelationList(
        title=_(u"FuZeRen List"),
        default=[],
        value_type=RelationChoice(
            title=u'FuZeRen',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'fuzeren',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    addr = schema.TextLine(
        title=_(u"Address"),
        required=False,
    )
    tel = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
    )
    data_src = schema.Tuple(
        title=_(u"Data Source"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'data_src',
        AjaxSelectFieldWidget,
        vocabulary='crgis.data_src'
    )
    coordinate = schema.Tuple(
        title=_(u"Coordinate Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'coordinate',
        AjaxSelectFieldWidget,
        vocabulary='crgis.coordinate'
    )
    df_type = schema.Tuple(
        title=_(u"DaoFaTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'df_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.df_type'
    )
    dt_type = schema.Tuple(
        title=_(u"DaoTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'dt_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.dt_type'
    )
    ft_type = schema.Tuple(
        title=_(u"FaTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'ft_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.ft_type'
    )
    df_attr = schema.Tuple(
        title=_(u"DaoFaTan Attribute"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'df_attr',
        AjaxSelectFieldWidget,
        vocabulary='dao.df_attr'
    )
    shchn = RelationList(
        title=_(u"ShiCheng List"),
        default=[],
        value_type=RelationChoice(
            title=u'ShiCheng',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'shchn',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    chngyn = RelationList(
        title=_(u"ChengYuan List"),
        default=[],
        value_type=RelationChoice(
            title=u'ChengYuan',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'chngyn',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    yange = RichTextField(
        title=_(u"YanGe"),
        required=False,
    )
    intro = RichTextField(
        title=_(u"Introduction"),
        required=False,
    )
    fengsi = schema.Tuple(
        title=_(u"FengSi"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'fengsi',
        AjaxSelectFieldWidget,
        vocabulary='crgis.deity'
    )
    zhusi = schema.Text(
        title=_(u"ZhuSi"),
        required=False,
    )
    zhiwai = RichTextField(
        title=_(u"ZhuSi ZhiWai"),
        required=False,
    )
    jisi = RichTextField(
        title=_(u"JiSi"),
        required=False,
    )
    wenwu = RichTextField(
        title=_(u"GuWenWu"),
        required=False,
    )
    keyi = RelationList(
        title=_(u"KeYi JingBen"),
        default=[],
        value_type=RelationChoice(
            title=u'KeYi',
            source=CatalogSource(Type='KeYi')
        ),
        required=False,
    )
    directives.widget(
        'keyi',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    service = RichTextField(
        title=_(u"Service"),
        required=False,
    )
    jngchng = RelationList(
        title=_(u"JingChang FuWu"),
        default=[],
        value_type=RelationChoice(
            title=u'JingChang',
            source=CatalogSource(Type='Temple')
        ),
        required=False,
    )
    directives.widget(
        'jngchng',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    zhumiao = RelationList(
        title=_(u"ZhuMiao List"),
        default=[],
        value_type=RelationChoice(
            title=u'ZhuMiao',
            source=CatalogSource(Type='Temple')
        ),
        required=False,
    )
    directives.widget(
        'zhumiao',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    yishi = RichTextField(
        title=_(u"YiShi"),
        required=False,
    )
    hzds = RelationList(
        title=_(u"HeZuo DaoShi"),
        default=[],
        value_type=RelationChoice(
            title=u'DaoShi',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    hzys = RichTextField(
        title=_(u"HeZuo YueShi"),
        required=False,
    )
    hzhz = RichTextField(
        title=_(u"HeZuo HuZhi"),
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

class IKeYi(model.Schema):
    """KeYi Type"""
    title = schema.TextLine(
        title=_(u"KeYi Name"),
        required=False,
    )
    description = schema.Text(
        title=_(u"KeYi Other Name"),
        required=False,
    )
    intro = RichTextField(
        title=_(u"Introduction KeYi"),
        required=False,
    )
    daibiao = namedfile.NamedBlobImage(
        title=_(u"DaiBiao YingXiang"),
        required=False,
    )
    leibie = schema.Tuple(
        title=_(u"LeiBie"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'leibie',
        AjaxSelectFieldWidget,
        vocabulary='keyi.leibie'
    )
    niandai = schema.TextLine(
        title=_(u"ZiLiao NianDai"),
        required=False,
    )
    shumg = schema.Text(
        title=_(u"ShuMing ShiXiang"),
        required=False,
    )
    ss_df = RelationList(
        title=_(u"SuoShu DaoFaTan"),
        default=[],
        value_type=RelationChoice(
            title=u'SSDFT',
            source=CatalogSource(Type='DaoFaTan')
        ),
        required=False,
    )
    directives.widget(
        'ss_df',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    chxren = RelationList(
        title=_(u"ChaoXieRen List"),
        default=[],
        value_type=RelationChoice(
            title=u'ChaoXieRen',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'chxren',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    license = schema.Tuple(
        title=_(u"License"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'license',
        AjaxSelectFieldWidget,
        vocabulary='keyi.license'
    )
    digit = schema.Tuple(
        title=_(u"Digitalization"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'digit',
        AjaxSelectFieldWidget,
        vocabulary='keyi.digit'
    )
    geshi = schema.Text(
        title=_(u"ZiLiao GeShi"),
        description=_(u"Length, Width, Height, Material"),
        required=False,
    )
    coordinate = schema.Tuple(
        title=_(u"Coordinate Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'coordinate',
        AjaxSelectFieldWidget,
        vocabulary='crgis.coordinate'
    )
    data_src = schema.Tuple(
        title=_(u"Data Source"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'data_src',
        AjaxSelectFieldWidget,
        vocabulary='keyi.data_src'
    )
    data_frm = schema.Tuple(
        title=_(u"Data From"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'data_frm',
        AjaxSelectFieldWidget,
        vocabulary='keyi.data_frm'
    )
    prvdr = schema.TextLine(
        title=_(u"Provider"),
        required=False,
    )
    tg_df = RelationList(
        title=_(u"TiGong DaoFaTan"),
        default=[],
        value_type=RelationChoice(
            title=u'TGDFT',
            source=CatalogSource(Type='DaoFaTan')
        ),
        required=False,
    )
    directives.widget(
        'tg_df',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    tg_ds = RelationList(
        title=_(u"TiGong DaoShi"),
        default=[],
        value_type=RelationChoice(
            title=u'TGDS',
            source=CatalogSource(Type='DaoShi')
        ),
        required=False,
    )
    directives.widget(
        'tg_ds',
        RelatedItemsFieldWidget,
        pattern_options={
            'recentlyUsed': True,
        }
    )
    df_type = schema.Tuple(
        title=_(u"DaoFaTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'df_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.df_type'
    )
    dt_type = schema.Tuple(
        title=_(u"DaoTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'dt_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.dt_type'
    )
    ft_type = schema.Tuple(
        title=_(u"FaTan Type"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    directives.widget(
        'ft_type',
        AjaxSelectFieldWidget,
        vocabulary='dao.ft_type'
    )
    youlai = RichTextField(
        title=_(u"YouLai"),
        required=False,
    )
    file = namedfile.NamedBlobFile(
        title=_(u"ZiLiao NeiRong"),
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
    gngxian = RichTextField(
        title=_(u"GongXianZhe"),
        required=False,
    )


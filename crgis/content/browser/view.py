from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.intid.interfaces import IIntIds
from zc.relation.interfaces import ICatalog
from zope.security import checkPermission


def back_references(source_object, attribute_name):
    """ Return back references from source object on specified attribute_name """
    catalog = getUtility(ICatalog)
    intids = getUtility(IIntIds)
    result = []
    for rel in catalog.findRelations(
                dict(to_id=intids.getId(aq_inner(source_object)),
                     from_attribute=attribute_name)
               ):
        obj = intids.queryObject(rel.from_id)
        if obj is not None and checkPermission('zope2.View', obj):
            result.append(obj)
    return result


class MyView(BrowserView):

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None


class TempleView(BrowserView):

    template = ViewPageTemplateFile("temple.pt")

    def __call__(self):
        return self.template()

    def deity_term(self, value):
        factory = getUtility(IVocabularyFactory, 'deity_name')
        vocabulary = factory(self.context)
        try:
            existing = vocabulary.getTerm(value)
            return existing.title.split(u': ')[0]
        except LookupError:
            return value

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

    def rPilgrimage(self):
        return back_references(self.context, 'temples')

    def rBiXieWu(self):
        return back_references(self.context, 'r_temples')

    def rFestival(self):
        return back_references(self.context, 'relatedItems')


class BiXieWuView(BrowserView):

    template = ViewPageTemplateFile("bixiewu.pt")

    def __call__(self):
        return self.template()

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

    def related_temples(self):
        return None


class ScheduleView(BrowserView):

    template = ViewPageTemplateFile("schedule.pt")

    def __call__(self):
        return self.template()

    def related_tpls(self):
        context = aq_inner(self.context)
        res = ()
        if base_hasattr(context, 'temples'):
            catalog = getToolByName(context, 'portal_catalog')
            related = context.temples()
            if not related: return ()
            brains = catalog(UID=related)
            if brains:
                positions = dict([(v, i) in enumerate(related)])
                res = list(brains)
                def _key(brain):
                    return positions.get(brain.UID, -1)
                res.sort(key=_key)
            return res

    def first_photo(self, temple):
         objs = temple.getChildNodes()
         for item in objs:
             if item.Type() in ['Photo', 'Image']:
                 return item
         return None


class DaoShiView(BrowserView):

    template = ViewPageTemplateFile("daoshi.pt")

    def __call__(self):
        return self.template()

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

    def related_temples(self):
        return None


class DaoFaTanView(BrowserView):

    template = ViewPageTemplateFile("daofatan.pt")

    def __call__(self):
        return self.template()

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

    def deity_term(self, value):
        factory = getUtility(IVocabularyFactory, 'deity_name')
        vocabulary = factory(self.context)
        try:
            existing = vocabulary.getTerm(value)
            return existing.title.split(u': ')[0]
        except LookupError:
            return value


class KeYiView(BrowserView):

    template = ViewPageTemplateFile("keyi.pt")

    def __call__(self):
        return self.template()

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None


class BanHuaView(BrowserView):

    template = ViewPageTemplateFile("banhua.pt")

    def __call__(self):
        return self.template()


class BuddhistView(BrowserView):

    template = ViewPageTemplateFile("buddhist.pt")

    def __call__(self):
        return self.template()


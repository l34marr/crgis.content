from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


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

    def getTemplePilgrimage(self, temple):
        return None

    def getTempleFestival(self, temple):
        return None

    def getTempleBiXieWu(self, temple):
        return None


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
        catalog = getToolByName(self.context, 'portal_catalog')
        photo = catalog(Type = 'Photo',
                        path = {'query': '.'.join(temple.getPhysicalPath())}
                       )
        if len(photo) == 0: return None
        return photo[0].getObject()

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


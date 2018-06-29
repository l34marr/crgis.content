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


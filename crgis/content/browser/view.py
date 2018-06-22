from Products.Five.browser import BrowserView
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from plone import api
import transaction

import logging


logger = logging.getLogger('SetDefaultViewStatus')


class SetDefaultViewStatus(BrowserView):
    """ Set default view and default status """

    def __call__(self):
        context = self.context
        request = self.request
        alsoProvides(request, IDisableCSRFProtection)

        count = 1
        catalog = context.portal_catalog
        brain = catalog()
        for item in brain:
            obj = item.getObject()

            logger.info("Updated %s: %s" % (count, obj.absolute_url()))
            obj.setLayout('view')

            try:
                api.content.transition(obj=obj, transition='publish')
            except:pass
            obj.reindexObject()
            count += 1
            if count % 100 == 0:
                transaction.commit()
                logger.info('transaction.commit() %s_ok' % count)



class MyView(BrowserView):

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None


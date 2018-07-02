from Products.Five.browser import BrowserView
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from plone import api

import pickle
from collective.geo.geographer.interfaces import IGeoreferenced, IWriteGeoreferenced
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

import transaction
import logging


logger = logging.getLogger('SetDefaultViewStatus')


#/opt/crgis43f/zinstance/src/crgis.policy/crgis/policy/browser


class ImportGIS(BrowserView):

    def __call__(self):

        request = self.request
        alsoProvides(request, IDisableCSRFProtection)

        with open('/tmp/georesult') as file:
            result = pickle.load(file)

        total = len(result)
        count = 0
        for item in result:
            if result[item]['type'] == 'Temple':
                count += 1
                continue

            brain = api.content.find(
                Type=result[item]['type'],
                path=item.replace('Traditional Knowledge and Practices', 'TraditionalKnowledgeAndPractices')
            )
            if len(brain) != 1:
                with open('/tmp/notFound', 'a') as file:
                    file.write('%s\n' % item)
                count += 1
                continue
#                import pdb; pdb.set_trace()

            obj = brain[0].getObject()
            geo = IWriteGeoreferenced(obj)
            geo.setGeoInterface('Point', result[item]['geo'] )
#            obj.reindexObject(idxs=['zgeo_geometry'])

            # Example, Path: /crgis/temples/ChanghuaCounty/pushin/0715003-FDC, Type: Temple, geo: (Decimal('120.53952200392'), Decimal('23.9525330029991'))
            count += 1
            logger.info('%s/%s, Path: %s, Type: %s, geo: %s' % (count, total, item, result[item]['type'], result[item]['geo']))

        return


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

from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
from plone import api
import logging
import requests
logger = logging.getLogger("ReindexObject:")
class ReindexAll(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        brain = api.content.find(Type=['Temple', 'BiXieWu'])
        count = 0
        for item in brain:
            req = requests.patch('%s' % item.getURL(),
                headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
                json={'IOwnership.rights': ' '}, auth=('admin', 'admin')
            )
            count += 1

            logger.info('%s %s: %s' % (count, req.status_code, item.getPath()))

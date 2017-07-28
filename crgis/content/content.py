from zope.interface import implements
from plone.dexterity.content import Container
from plone.dexterity.content import Item

from crgis.content.interfaces import IBiXieWu
from crgis.content.interfaces import IPhoto


class BiXieWu(Container):
    implements(IBiXieWu)

class Photo(Item):
    implements(IPhoto)


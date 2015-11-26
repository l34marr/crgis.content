from zope.interface import implements
from plone.dexterity.content import Item

from crgis.content.interfaces import IBiXieWu
from crgis.content.interfaces import ITheater


class BiXieWu(Item):
    implements(IBiXieWu)

class Theater(Item):
    implements(ITheater)


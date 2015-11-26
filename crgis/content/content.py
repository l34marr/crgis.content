from zope.interface import implementer
from plone.dexterity.content import Item

from crgis.content.interfaces import IBiXieWu
from crgis.content.interfaces import ITheater


@implementer(IBiXieWu)
class BiXieWu(Item):
    """Item Subclass for BiXieWu
    """

@implementer(ITheater)
class Theater(Item):
    """Item Subclass for Theater
    """


from zope.interface import implementer
from plone.dexterity.content import Item

from crgis.content.interfaces import IBiXieWu


@implementer(IBiXieWu)
class BiXieWu(Item):
    """Item Subclass for BiXieWu
    """


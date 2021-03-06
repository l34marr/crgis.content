from zope.interface import implements
from plone.dexterity.content import Container
from plone.dexterity.content import Item

from crgis.content.interfaces import ITemple
from crgis.content.interfaces import IBiXieWu
from crgis.content.interfaces import IPhoto
from crgis.content.interfaces import IPilgrimage
from crgis.content.interfaces import ISchedule
from crgis.content.interfaces import IBuddhist
from crgis.content.interfaces import IDaoShi
from crgis.content.interfaces import IDaoFaTan
from crgis.content.interfaces import IKeYi
from crgis.content.interfaces import IBanHua


class Temple(Container):
    implements(ITemple)

class BiXieWu(Container):
    implements(IBiXieWu)

class Photo(Item):
    implements(IPhoto)

class Pilgrimage(Container):
    implements(IPilgrimage)

class Schedule(Container):
    implements(ISchedule)

class Buddhist(Item):
    implements(IBuddhist)

class DaoShi(Container):
    implements(IDaoShi)

class DaoFaTan(Container):
    implements(IDaoFaTan)

class KeYi(Container):
    implements(IDaoFaTan)

class BanHua(Item):
    implements(IBanHua)


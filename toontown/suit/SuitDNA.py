import random
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
from toontown.toonbase import TTLocalizer
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from otp.avatar import AvatarDNA
from SuitLocalizerEnglish import *
notify = directNotify.newCategory('SuitDNA')
suitHeadTypes = ['f',
 'p',
 'ym',
 'mm',
 'ds',
 'hh',
 'cr',
 'tbc',
 'bf',
 'b',
 'dt',
 'ac',
 'bs',
 'sd',
 'le',
 'bw',
 'sc',
 'pp',
 'tw',
 'bc',
 'nc',
 'mb',
 'ls',
 'rb',
 'cc',
 'tm',
 'nd',
 'gh',
 'ms',
 'tf',
 'm',
 'mh',
 'hc']
#remake suitHeadTypes to include the new suit strings
suitHeadTypes = [FLUNKY,
    PENCIL_PUSHER,
    YESMAN,
    MICROMANAGER,
    DOWNSIZER,
    HEAD_HUNTER,
    CORPORATE_RAIDER,
    THE_BIG_CHEESE,
    #LAWBOT_STRINGS
    BOTTOM_FEEDER,
    BLOODSUCKER,
    DOUBLE_TALKER,
    AMBULANCE_CHASER,
    BACK_STABBER,
    SPIN_DOCTOR,
    LEGAL_EAGLE,
    BIG_WIG,
    #CASHBOT_STRINGS
    SHORT_CHANGE,
    PENNY_PINCHER,
    TIGHTWAD,
    BEAN_COUNTER,
    NUMBER_CRUNCHER,
    MONEY_BAGS,
    LOAN_SHARK,
    ROBBER_BARON,
    #SELLBOT_STRINGS
    COLD_CALLER,
    HOT_CALLER,
    TELEMARKETER,
    NAME_DROPPER,
    GLAD_HANDER,
    MOVER_AND_SHAKER,
    TWO_FACE,
    THE_MINGLER,
    MR_HOLLYWOOD]
suitATypes = [YESMAN,
 HEAD_HUNTER,
 THE_BIG_CHEESE,
 DOUBLE_TALKER,
 BACK_STABBER,
 LEGAL_EAGLE,
 BIG_WIG,
 PENNY_PINCHER,
 NUMBER_CRUNCHER,
 ROBBER_BARON,
 NAME_DROPPER,
 TWO_FACE,
 THE_MINGLER,
 MR_HOLLYWOOD]
suitBTypes = [PENCIL_PUSHER,
 DOWNSIZER,
 BLOODSUCKER,
 AMBULANCE_CHASER,
 SPIN_DOCTOR,
 BEAN_COUNTER,
 LOAN_SHARK,
 TELEMARKETER,
 MOVER_AND_SHAKER]
suitCTypes = [FLUNKY,
 MICROMANAGER,
 CORPORATE_RAIDER,
 BOTTOM_FEEDER,
 SHORT_CHANGE,
 TIGHTWAD,
 MONEY_BAGS,
 COLD_CALLER,
 HOT_CALLER,
 GLAD_HANDER]
suitDepts = [BOSSBOT,
 LAWBOT,
 CASHBOT,
 SELLBOT]
suitDeptFullnames = {BOSSBOT: TTLocalizer.Bossbot,
 LAWBOT: TTLocalizer.Lawbot,
 CASHBOT: TTLocalizer.Cashbot,
 SELLBOT: TTLocalizer.Sellbot}
suitDeptFullnamesP = {BOSSBOT: TTLocalizer.BossbotP,
 LAWBOT: TTLocalizer.LawbotP,
 CASHBOT: TTLocalizer.CashbotP,
 SELLBOT: TTLocalizer.SellbotP}
corpPolyColor = VBase4(0.95, 0.75, 0.75, 1.0)
legalPolyColor = VBase4(0.75, 0.75, 0.95, 1.0)
moneyPolyColor = VBase4(0.65, 0.95, 0.85, 1.0)
salesPolyColor = VBase4(0.95, 0.75, 0.95, 1.0)
suitsPerLevel = [1,
 1,
 1,
 1,
 1,
 1,
 1,
 1]
suitsPerDept = 8
goonTypes = ['pg', 'sg']

suitTierDict = {
    SELLBOT: [
        [COLD_CALLER, HOT_CALLER],
        [TELEMARKETER],
        [NAME_DROPPER],
        [GLAD_HANDER],
        [MOVER_AND_SHAKER],
        [TWO_FACE],
        [THE_MINGLER],
        [MR_HOLLYWOOD]
    ],
    CASHBOT: [
        [SHORT_CHANGE],
        [PENNY_PINCHER],
        [TIGHTWAD],
        [BEAN_COUNTER],
        [NUMBER_CRUNCHER],
        [MONEY_BAGS],
        [LOAN_SHARK],
        [ROBBER_BARON]
    ],
    LAWBOT: [
      [BOTTOM_FEEDER],
      [BLOODSUCKER],
      [DOUBLE_TALKER],
      [AMBULANCE_CHASER],
      [BACK_STABBER],
      [SPIN_DOCTOR],
      [LEGAL_EAGLE],
      [BIG_WIG] 
    ],
    BOSSBOT: [
        [FLUNKY],
        [PENCIL_PUSHER],
        [YESMAN],
        [MICROMANAGER],
        [DOWNSIZER],
        [HEAD_HUNTER],
        [CORPORATE_RAIDER],
        [THE_BIG_CHEESE]
    ]
}

sellbots = ['cc', 'hc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh']
cashbots = ['sc', 'pp', 'tw', 'bc', 'nc', 'mb', 'ls', 'rb']
lawbots = ['bf', 'b', 'dt', 'ac', 'bs', 'sd', 'le', 'bw']
bossbots = ['f', 'p', 'ym', 'mm', 'ds', 'hh', 'cr', 'tbc']

def getSuitBodyType(name):
    if name in suitATypes:
        return 'a'
    elif name in suitBTypes:
        return 'b'
    elif name in suitCTypes:
        return 'c'
    else:
        print 'Unknown body type for suit name: ', name


def getSuitDept(name):
    index = suitHeadTypes.index(name)
    if name in bossbots:
        return suitDepts[0]
    elif name in lawbots:
        return suitDepts[1]
    elif name in cashbots:
        return suitDepts[2]
    elif name in sellbots:
        return suitDepts[3]
    else:
        print 'Unknown dept for suit name: ', name
        return None
    return None


def getDeptFullname(dept):
    return suitDeptFullnames[dept]


def getDeptFullnameP(dept):
    return suitDeptFullnamesP[dept]


def getSuitDeptFullname(name):
    return suitDeptFullnames[getSuitDept(name)]


def getSuitType(name):
    index = suitHeadTypes.index(name)
    return index % suitsPerDept + 1


def getRandomSuitType(level, rng = random):
    return random.randint(max(level - 4, 1), min(level, 8))


def getRandomSuitByDept(dept):
    deptNumber = suitDepts.index(dept)
    return suitHeadTypes[suitsPerDept * deptNumber + random.randint(0, 7)]


class SuitDNA(AvatarDNA.AvatarDNA):

    def __init__(self, str = None, type = None, dna = None, r = None, b = None, g = None):
        if str != None:
            self.makeFromNetString(str)
        elif type != None:
            if type == 's':
                self.newSuit()
        else:
            self.type = 'u'
        return

    def __str__(self):
        if self.type == 's':
            return 'type = %s\nbody = %s, dept = %s, name = %s' % ('suit',
             self.body,
             self.dept,
             self.name)
        elif self.type == 'b':
            return 'type = boss cog\ndept = %s' % self.dept
        else:
            return 'type undefined'

    def makeNetString(self):
        dg = PyDatagram()
        dg.addFixedString(self.type, 1)
        if self.type == 's':
            dg.addFixedString(self.name, 3)
            dg.addFixedString(self.dept, 1)
        elif self.type == 'b':
            dg.addFixedString(self.dept, 1)
        elif self.type == 'u':
            notify.error('undefined avatar')
        else:
            notify.error('unknown avatar type: ', self.type)
        return dg.getMessage()

    def makeFromNetString(self, string):
        dg = PyDatagram(string)
        dgi = PyDatagramIterator(dg)
        self.type = dgi.getFixedString(1)
        if self.type == 's':
            self.name = dgi.getFixedString(3)
            self.dept = dgi.getFixedString(1)
            self.body = getSuitBodyType(self.name)
        elif self.type == 'b':
            self.dept = dgi.getFixedString(1)
        else:
            notify.error('unknown avatar type: ', self.type)
        return None

    def __defaultGoon(self):
        self.type = 'g'
        self.name = goonTypes[0]

    def __defaultSuit(self):
        self.type = 's'
        self.name = DOWNSIZER
        self.dept = getSuitDept(self.name)
        self.body = getSuitBodyType(self.name)

    def newSuit(self, name = None):
        if name == None:
            self.__defaultSuit()
        else:
            self.type = 's'
            self.name = name
            self.dept = getSuitDept(self.name)
            self.body = getSuitBodyType(self.name)
        return

    def newBossCog(self, dept):
        self.type = 'b'
        self.dept = dept

    def newSuitRandom(self, level = None, dept = None):
        self.type = 's'
        if level == None:
            level = random.choice(xrange(1, len(suitsPerLevel)))
        elif level < 0 or level > len(suitsPerLevel):
            notify.error('Invalid suit level: %d' % level)
        if dept == None:
            dept = random.choice(suitDepts)
        self.dept = dept
        index = suitDepts.index(dept)
        
        
        self.name = random.choice(suitTierDict[dept][level-1])
        self.body = getSuitBodyType(self.name)
        return

    def newGoon(self, name = None):
        if type == None:
            self.__defaultGoon()
        else:
            self.type = 'g'
            if name in goonTypes:
                self.name = name
            else:
                notify.error('unknown goon type: ', name)
        return

    def getType(self):
        if self.type == 's':
            type = 'suit'
        elif self.type == 'b':
            type = 'boss'
        else:
            notify.error('Invalid DNA type: ', self.type)
        return type

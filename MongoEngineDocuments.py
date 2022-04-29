from mongoengine import Document, DateTimeField, StringField, IntField

class GM_MAINTENANCE_LOGIN(Document):
    GmLoginID = StringField()
    meta = {'collection': 'GM_MAINTENANCE_LOGIN'}

class SERVER_CLEAN(Document):
    Format = IntField()
    Server001 = IntField()
    Server002 = IntField()
    Server003 = IntField()
    Server004 = IntField()
    Server005 = IntField()
    Server006 = IntField()
    Server007 = IntField()
    Server008 = IntField()
    Server009 = IntField()
    Server010 = IntField()
    meta = {'collection': 'SERVER_CLEAN'}

class SERVER_SETTINGS(Document):
    nServerNo = IntField()
    MaximumLevelChange = IntField()
    DropNotice = IntField()
    UpgradeNotice = IntField()
    UserMaxUpgradeCount = IntField()
    OpenQuestSkill = IntField()
    meta = {'collection': 'SERVER_SETTINGS'}

class GAME_OPTIONS(Document):
    MaintenanceMode = IntField()
    CharacterSelectLogin = IntField()
    OpenOTP = IntField()
    AutoRegister = IntField()
    FreeLimit = IntField()
    TotalUserLimit = IntField()
    ServerIPAddress = StringField()
    meta = {'collection': 'GAME_OPTIONS'}

class BEGINNER_SETTINGS(Document):
    ServerNo = IntField()
    BeginnerType = IntField()
    BeginnerDesc = StringField()
    meta = {'collection': 'BEGINNER_SETTINGS'}

class GAME_MASTER_SETTINGS(Document):
    strAccountID = StringField()
    strCharID = StringField()
    sServerNo = IntField()
    sMute = IntField()
    sUnMute = IntField()
    sUnBan = IntField()
    sBanPermit = IntField()
    sAllowAttack = IntField()
    sDisabledAttack = IntField()
    sNpAdd = IntField()
    sExpAdd = IntField()
    sMoneyAdd = IntField()
    sLoyaltyChange = IntField()
    sExpChange = IntField()
    sMoneyChange = IntField()
    sGiveItem = IntField()
    sGiveItemSelf = IntField()
    sSummonUser = IntField()
    sTpOnUser = IntField()
    sZoneChange = IntField()
    sLocationChange = IntField()
    sMonsterSummon = IntField()
    sNpcSummon = IntField()
    sMonKilled = IntField()
    sTeleportAllUser = IntField()
    sClanSummon = IntField()
    sResetPlayerRanking = IntField()
    sChangeEventRoom = IntField()
    sWarOpen1 = IntField()
    sWarOpen2 = IntField()
    sWarOpen3 = IntField()
    sWarOpen4 = IntField()
    sWarOpen5 = IntField()
    sWarOpen6 = IntField()
    sWarOpen9 = IntField()
    sWarSiegeOpen = IntField()
    sWarClose = IntField()
    sCaptainElection = IntField()
    sWarSiegeClose = IntField()
    sSendPrsion = IntField()
    meta = {'collection': 'GAME_MASTER_SETTINGS'}

class ACCOUNT_LOGIN_CONTROL(Document):
    strAccountID = StringField()
    BanGameMasterName = StringField()
    isAuthority = IntField()
    BanReason = StringField()
    BanCount = IntField()
    OpenCount = IntField()
    UpdateTime = DateTimeField()
    meta = {'collection': 'ACCOUNT_LOGIN_CONTROL'}


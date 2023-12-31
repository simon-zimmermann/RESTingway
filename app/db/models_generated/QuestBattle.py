from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class QuestBattle(SQLModel, table=True):
    __tablename__ = "quest_battle"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    quest: int
    quest_battle_scene: int
    time_limit: int
    level_sync: int
    script_instruction0: str
    script_instruction1: str
    script_instruction2: str
    script_instruction3: str
    script_instruction4: str
    script_instruction5: str
    script_instruction6: str
    script_instruction7: str
    script_instruction8: str
    script_instruction9: str
    script_instruction10: str
    script_instruction11: str
    script_instruction12: str
    script_instruction13: str
    script_instruction14: str
    script_instruction15: str
    script_instruction16: str
    script_instruction17: str
    script_instruction18: str
    script_instruction19: str
    script_instruction20: str
    script_instruction21: str
    script_instruction22: str
    script_instruction23: str
    script_instruction24: str
    script_instruction25: str
    script_instruction26: str
    script_instruction27: str
    script_instruction28: str
    script_instruction29: str
    script_instruction30: str
    script_instruction31: str
    script_instruction32: str
    script_instruction33: str
    script_instruction34: str
    script_instruction35: str
    script_instruction36: str
    script_instruction37: str
    script_instruction38: str
    script_instruction39: str
    script_instruction40: str
    script_instruction41: str
    script_instruction42: str
    script_instruction43: str
    script_instruction44: str
    script_instruction45: str
    script_instruction46: str
    script_instruction47: str
    script_instruction48: str
    script_instruction49: str
    script_instruction50: str
    script_instruction51: str
    script_instruction52: str
    script_instruction53: str
    script_instruction54: str
    script_instruction55: str
    script_instruction56: str
    script_instruction57: str
    script_instruction58: str
    script_instruction59: str
    script_instruction60: str
    script_instruction61: str
    script_instruction62: str
    script_instruction63: str
    script_instruction64: str
    script_instruction65: str
    script_instruction66: str
    script_instruction67: str
    script_instruction68: str
    script_instruction69: str
    script_instruction70: str
    script_instruction71: str
    script_instruction72: str
    script_instruction73: str
    script_instruction74: str
    script_instruction75: str
    script_instruction76: str
    script_instruction77: str
    script_instruction78: str
    script_instruction79: str
    script_instruction80: str
    script_instruction81: str
    script_instruction82: str
    script_instruction83: str
    script_instruction84: str
    script_instruction85: str
    script_instruction86: str
    script_instruction87: str
    script_instruction88: str
    script_instruction89: str
    script_instruction90: str
    script_instruction91: str
    script_instruction92: str
    script_instruction93: str
    script_instruction94: str
    script_instruction95: str
    script_instruction96: str
    script_instruction97: str
    script_instruction98: str
    script_instruction99: str
    script_instruction100: str
    script_instruction101: str
    script_instruction102: str
    script_instruction103: str
    script_instruction104: str
    script_instruction105: str
    script_instruction106: str
    script_instruction107: str
    script_instruction108: str
    script_instruction109: str
    script_instruction110: str
    script_instruction111: str
    script_instruction112: str
    script_instruction113: str
    script_instruction114: str
    script_instruction115: str
    script_instruction116: str
    script_instruction117: str
    script_instruction118: str
    script_instruction119: str
    script_instruction120: str
    script_instruction121: str
    script_instruction122: str
    script_instruction123: str
    script_instruction124: str
    script_instruction125: str
    script_instruction126: str
    script_instruction127: str
    script_instruction128: str
    script_instruction129: str
    script_instruction130: str
    script_instruction131: str
    script_instruction132: str
    script_instruction133: str
    script_instruction134: str
    script_instruction135: str
    script_instruction136: str
    script_instruction137: str
    script_instruction138: str
    script_instruction139: str
    script_instruction140: str
    script_instruction141: str
    script_instruction142: str
    script_instruction143: str
    script_instruction144: str
    script_instruction145: str
    script_instruction146: str
    script_instruction147: str
    script_instruction148: str
    script_instruction149: str
    script_instruction150: str
    script_instruction151: str
    script_instruction152: str
    script_instruction153: str
    script_instruction154: str
    script_instruction155: str
    script_instruction156: str
    script_instruction157: str
    script_instruction158: str
    script_instruction159: str
    script_instruction160: str
    script_instruction161: str
    script_instruction162: str
    script_instruction163: str
    script_instruction164: str
    script_instruction165: str
    script_instruction166: str
    script_instruction167: str
    script_instruction168: str
    script_instruction169: str
    script_instruction170: str
    script_instruction171: str
    script_instruction172: str
    script_instruction173: str
    script_instruction174: str
    script_instruction175: str
    script_instruction176: str
    script_instruction177: str
    script_instruction178: str
    script_instruction179: str
    script_instruction180: str
    script_instruction181: str
    script_instruction182: str
    script_instruction183: str
    script_instruction184: str
    script_instruction185: str
    script_instruction186: str
    script_instruction187: str
    script_instruction188: str
    script_instruction189: str
    script_instruction190: str
    script_instruction191: str
    script_instruction192: str
    script_instruction193: str
    script_instruction194: str
    script_instruction195: str
    script_instruction196: str
    script_instruction197: str
    script_instruction198: str
    script_instruction199: str
    script_value0: int
    script_value1: int
    script_value2: int
    script_value3: int
    script_value4: int
    script_value5: int
    script_value6: int
    script_value7: int
    script_value8: int
    script_value9: int
    script_value10: int
    script_value11: int
    script_value12: int
    script_value13: int
    script_value14: int
    script_value15: int
    script_value16: int
    script_value17: int
    script_value18: int
    script_value19: int
    script_value20: int
    script_value21: int
    script_value22: int
    script_value23: int
    script_value24: int
    script_value25: int
    script_value26: int
    script_value27: int
    script_value28: int
    script_value29: int
    script_value30: int
    script_value31: int
    script_value32: int
    script_value33: int
    script_value34: int
    script_value35: int
    script_value36: int
    script_value37: int
    script_value38: int
    script_value39: int
    script_value40: int
    script_value41: int
    script_value42: int
    script_value43: int
    script_value44: int
    script_value45: int
    script_value46: int
    script_value47: int
    script_value48: int
    script_value49: int
    script_value50: int
    script_value51: int
    script_value52: int
    script_value53: int
    script_value54: int
    script_value55: int
    script_value56: int
    script_value57: int
    script_value58: int
    script_value59: int
    script_value60: int
    script_value61: int
    script_value62: int
    script_value63: int
    script_value64: int
    script_value65: int
    script_value66: int
    script_value67: int
    script_value68: int
    script_value69: int
    script_value70: int
    script_value71: int
    script_value72: int
    script_value73: int
    script_value74: int
    script_value75: int
    script_value76: int
    script_value77: int
    script_value78: int
    script_value79: int
    script_value80: int
    script_value81: int
    script_value82: int
    script_value83: int
    script_value84: int
    script_value85: int
    script_value86: int
    script_value87: int
    script_value88: int
    script_value89: int
    script_value90: int
    script_value91: int
    script_value92: int
    script_value93: int
    script_value94: int
    script_value95: int
    script_value96: int
    script_value97: int
    script_value98: int
    script_value99: int
    script_value100: int
    script_value101: int
    script_value102: int
    script_value103: int
    script_value104: int
    script_value105: int
    script_value106: int
    script_value107: int
    script_value108: int
    script_value109: int
    script_value110: int
    script_value111: int
    script_value112: int
    script_value113: int
    script_value114: int
    script_value115: int
    script_value116: int
    script_value117: int
    script_value118: int
    script_value119: int
    script_value120: int
    script_value121: int
    script_value122: int
    script_value123: int
    script_value124: int
    script_value125: int
    script_value126: int
    script_value127: int
    script_value128: int
    script_value129: int
    script_value130: int
    script_value131: int
    script_value132: int
    script_value133: int
    script_value134: int
    script_value135: int
    script_value136: int
    script_value137: int
    script_value138: int
    script_value139: int
    script_value140: int
    script_value141: int
    script_value142: int
    script_value143: int
    script_value144: int
    script_value145: int
    script_value146: int
    script_value147: int
    script_value148: int
    script_value149: int
    script_value150: int
    script_value151: int
    script_value152: int
    script_value153: int
    script_value154: int
    script_value155: int
    script_value156: int
    script_value157: int
    script_value158: int
    script_value159: int
    script_value160: int
    script_value161: int
    script_value162: int
    script_value163: int
    script_value164: int
    script_value165: int
    script_value166: int
    script_value167: int
    script_value168: int
    script_value169: int
    script_value170: int
    script_value171: int
    script_value172: int
    script_value173: int
    script_value174: int
    script_value175: int
    script_value176: int
    script_value177: int
    script_value178: int
    script_value179: int
    script_value180: int
    script_value181: int
    script_value182: int
    script_value183: int
    script_value184: int
    script_value185: int
    script_value186: int
    script_value187: int
    script_value188: int
    script_value189: int
    script_value190: int
    script_value191: int
    script_value192: int
    script_value193: int
    script_value194: int
    script_value195: int
    script_value196: int
    script_value197: int
    script_value198: int
    script_value199: int


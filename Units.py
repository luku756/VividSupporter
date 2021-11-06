
from enum import Enum

class Symbols(Enum):
    red = '레드'
    blue = '블루'
    yellow = '옐로'
    purple = '퍼플'
    green = '그린'
    pink = '핑크'
    orange = '오렌지'
    white = '화이트'
    black = '블랙'
    brown = '브라운'
    random_color = '컬러랜덤'

    sun = '태양'
    moon = '달'
    star = '별'
    magician = '마술사'
    justice = '정의'
    wheel = '운명의바퀴'
    chariot = '채리엇'
    crown = '광대'
    tower = '탑'
    forest = '숲'
    plum = '매화문장'
    shield = '방패'
    hanged = '매달린사람'
    random_mark = '마크랜덤'


class ColorSymbols(Enum):
    red = Symbols.red
    blue = Symbols.blue
    yellow = Symbols.yellow
    purple = Symbols.purple
    green = Symbols.green
    pink = Symbols.pink
    orange = Symbols.orange
    white = Symbols.white
    black = Symbols.black
    brown = Symbols.brown


class MarkSymbols(Enum):
    sun = Symbols.sun
    moon = Symbols.moon
    star = Symbols.star
    magician = Symbols.magician
    justice = Symbols.justice
    wheel = Symbols.wheel
    chariot = Symbols.chariot
    crown = Symbols.crown
    tower = Symbols.tower
    forest = Symbols.forest
    plum = Symbols.plum
    shield = Symbols.shield
    hanged = Symbols.hanged

class Level(Enum):
    bronze = '브론즈'
    silver = '실버'
    gold = '골드'


class ButtonState(Enum):
    pressed = 0
    unpressed = 1

class Units:
    unit_list = [
        ['기사 헬리오도르', Level.bronze, Symbols.yellow, Symbols.justice],
        ['기사 블루 수', Level.bronze, Symbols.blue, Symbols.chariot],
        ['기사 가넷', Level.bronze, Symbols.red, Symbols.magician],
        ['왕국 창병', Level.bronze, Symbols.brown, Symbols.shield],
        ['왕국 궁수', Level.bronze, Symbols.brown, Symbols.sun],
        ['숲의 주민 스핀', Level.bronze, Symbols.green, Symbols.forest],
        ["대장장이 레드 루", Level.bronze, Symbols.red, Symbols.sun],
        ["집사장 플린트", Level.bronze, Symbols.brown, Symbols.chariot],
        ["도적 라피스", Level.bronze, Symbols.blue, Symbols.moon],
        ["숲의 주민 모가나", Level.bronze, Symbols.pink, Symbols.forest],
        ["자경단 클로돌", Level.bronze, Symbols.blue, Symbols.shield],
        ["용병 기베온", Level.bronze, Symbols.chariot, Symbols.hanged],
        ["방랑 상인 시트린", Level.bronze, Symbols.yellow, Symbols.wheel],
        ["광대 엘레스티얼", Level.bronze, Symbols.purple, Symbols.magician],
        ["사무라이 코쿠요", Level.bronze, Symbols.black, Symbols.plum],
        ["방랑 악사 스페서", Level.bronze, Symbols.orange, Symbols.star],
        ["나무꾼 제이드", Level.bronze, Symbols.green, Symbols.moon],
        ["숲의 주민 리비안", Level.bronze, Symbols.yellow, Symbols.forest],
        ["죄수 듀모티어", Level.bronze, Symbols.blue, Symbols.hanged],
        ["꽃 상인 카넬리아", Level.bronze, Symbols.orange, Symbols.sun],
        ["궁정 화가 지르콘", Level.bronze, Symbols.random_color, Symbols.random_mark],
        ["사서 아메지스트", Level.bronze, Symbols.purple, Symbols.magician],
        ["가면의 제트", Level.bronze, Symbols.black, Symbols.crown],

        ["닌자 코교쿠", Level.silver, Symbols.red, Symbols.plum],
        ["숲의 주민 젬실리카", Level.silver, Symbols.green, Symbols.forest],
        ["금강 기사 다이아", Level.silver, Symbols.white, Symbols.justice],
        ["쌍도 로도", Level.silver, Symbols.pink, Symbols.justice],
        ["얼굴 없는 아린", Level.silver, Symbols.purple, Symbols.hanged],
        ["연금술사 핑토", Level.silver, Symbols.pink, Symbols.star],
        ["감정사 트리핀", Level.silver, Symbols.yellow, Symbols.magician],
        ["궁수장 재스퍼", Level.silver, Symbols.red, Symbols.tower],
        ["무희 리노", Level.silver, Symbols.orange, Symbols.crown],
        ["조향사 세렌", Level.silver, Symbols.purple, Symbols.tower],
        ["녹풍의 크롬", Level.silver, Symbols.green, Symbols.shield],
        ["맹탐정 페트리", Level.silver, Symbols.brown, Symbols.justice],
        ["문장관 머스코", Level.silver, Symbols.red, Symbols.chariot],
        ["탐굴가 앰버", Level.silver, Symbols.orange, Symbols.wheel],
        ["흑기사 오닉스", Level.silver, Symbols.black, Symbols.moon],
        ["동경의 파파라챠", Level.silver, Symbols.pink, Symbols.magician],
        ["사령술사 레오스", Level.silver, Symbols.black, Symbols.hanged],
        ["점성술사 래브라", Level.silver, Symbols.random_color, Symbols.random_mark],
        ["괴도 스라이", Level.silver, Symbols.purple, Symbols.moon],

        ["시녀 모리언", Level.gold, Symbols.black, Symbols.plum],
        ["왕의 방패 브론", Level.gold, Symbols.brown, Symbols.shield],
        ["양광의 기사 써니", Level.gold, Symbols.orange, Symbols.sun],
        ["월광의 기사 무니", Level.gold, Symbols.white, Symbols.moon],
        ["숲의 여왕 사파이어", Level.gold, Symbols.blue, Symbols.forest],
        ["왕의 검 루벨라", Level.gold, Symbols.red, Symbols.crown],
        ["수도기사 시리시아", Level.gold, Symbols.pink, Symbols.sun],
        ["천둥 사자 토파즈", Level.gold, Symbols.yellow, Symbols.tower],
        ["발명가 페리도트", Level.gold, Symbols.green, Symbols.magician]


    ]

    random_unit_list = [
        ["궁정 화가 지르콘", Level.bronze, Symbols.random_color, Symbols.random_mark],
        ["점성술사 래브라", Level.silver, Symbols.random_color, Symbols.random_mark]
    ]

    @staticmethod
    def get_unit_list():

        lists = []
        for unit in Units.unit_list:
            u = unit.copy()

            # 랜덤 유닛은 변경된 값을 반영할 것
            for rand_unit in Units.random_unit_list:
                if u[0] == rand_unit[0]:
                    u = rand_unit.copy()

            # u.append(ButtonState.unpressed)
            lists.append(u)

        return lists

    @staticmethod
    def get_symbol_list():
        return Symbols

    @staticmethod
    def get_random_unit_list():
        return Units.random_unit_list

    @staticmethod
    def reset_random_unit():
        for unit in Units.random_unit_list:
            unit[2] = Symbols.random_color
            unit[3] = Symbols.random_mark

    @staticmethod
    def set_random_unit_state(unit_name, symbol_type, new_symbol):

        for unit in Units.random_unit_list:

            if unit_name == unit[0]:
                if symbol_type == '컬러랜덤':
                    unit[2] = new_symbol
                else:
                    unit[3] = new_symbol
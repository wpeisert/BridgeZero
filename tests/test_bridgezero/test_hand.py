from bridgezero.hand import Hand


def test_hand_to_PBN_PBN_to_hand():
    data = [
        ([], "..."),
        ([0], "A..."),
        ([13], ".A.."),
        ([26], "..A."),
        ([39], "...A"),
        ([12], "2..."),
        ([25], ".2.."),
        ([38], "..2."),
        ([51], "...2"),
        ([x for x in range(52)], "AKQJT98765432.AKQJT98765432.AKQJT98765432.AKQJT98765432"),
    ]
    for hand, pbn in data:
        assert Hand.hand_to_PBN(hand) == pbn
        assert Hand.PBN_to_hand(pbn) == hand

def test_getColorCardsCount():
    data = [
        ([], 0, 0),
        ([], 1, 0),
        ([], 2, 0),
        ([], 3, 0),
        ([0], 0, 1),
        ([0], 1, 0),
        ([0], 2, 0),
        ([0], 3, 0),
        ([x for x in range(52)], 0, 13),
        ([x for x in range(52)], 1, 13),
        ([x for x in range(52)], 2, 13),
        ([x for x in range(52)], 3, 13),
    ]

    for hand, color, count in data:
        assert Hand.getColorCardsCount(hand, color) == count

def test_getPc():
    data = [
        ([], 0),
        ([0], 4),
        ([1], 3),
        ([2], 2),
        ([3], 1),
        ([4], 0),
        ([x for x in range(52)], 40),
    ]

    for hand, pc in data:
        assert Hand.getPc(hand) == pc

from random import choice

generic_answers = [
    u"אני לא מאמין ששאלת את זה",
    u"\U0001F914",
    u"\U0001F926",
    u"מה הכוונה?",

]

generic_universal_truths = [
    u"מי ששלם עם עצמו, אוהב פיצה",

]

generic_positive_responses = [
    u"בטח!",

]

generic_negative_responses = [
    u"אין לי מה להגיד על זה",
    u"יכולת להגיד משהו שימושי אבל בחרת להגיד את זה",
    u"אין לי סיבה לקחת את זה ברצינות",
    u"וואו.",
    u"-_-",
]


def generic_answer():
    return choice(generic_answers)


def generic_universal_truth():
    return choice(generic_universal_truths)


def generic_positive_response():
    return choice(generic_positive_responses)


def generic_negative_response():
    return choice(generic_negative_responses)

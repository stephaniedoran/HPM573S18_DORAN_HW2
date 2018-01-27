# Doran Homework 2 question 1
# The user will specify the level of 8 attributes in HUI3 instrument and gets the corresponding health score.
# Make sure your code checks if the entered values for attributes are valid (hint: use the if ... raise statement).

Constant = 0.371
dictCoefficients = {'Vision':        [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':       [1, 0.95, 0.89, 0.8, 0.74, 0.61],
                    'Speech':        [1, 0.94, 0.89, 0.81, 0.68],
                    'Ambulation':    [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':     [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':       [1, 0.95, 0.85, 0.64, 0.46],
                    'Cognition':     [1, 0.92, 0.95, 0.83, 0.6, 0.42],
                    'Pain':          [1, 0.96, 0.9, 0.77, 0.55]};


def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):

    """

    :param vision: Score for Vision attribute
    :param hearing: Score for hearing attribute
    :param speech: Score for speech attribute
    :param ambulation: Score for ambulation attribute
    :param dexterity: Score for dexterity attribute
    :param emotion: Score for emotion attribute
    :param cognition: Score for cognition attribute
    :param pain: Score for pain attribute
    :return: Health Utilities Index mark 3 score
    """

# creating error messages for inputs outside of the range of scores

    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1 through 6')

    if not (hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1 through 6')

    if not (speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1 through 5')

    if not (ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1 through 6')

    if not (dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1 through 6')

    if not (emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion level can take only 1 through 5')

    if not (cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1 through 6')

    if not (pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1 through 5')

    # calculating score  u* = 1.371 (b1 * b2 * b3 * b4 * b5 * b6 * b7 * b8) - 0.371
    # [parameter -1] to account for python starting counting at 0 and score input starting at 1

    score = 1.371

    score *= dictCoefficients['Vision'][vision - 1]
    score *= dictCoefficients['Hearing'][hearing - 1]
    score *= dictCoefficients['Speech'][speech - 1]
    score *= dictCoefficients['Ambulation'][ambulation - 1]
    score *= dictCoefficients['Dexterity'][dexterity - 1]
    score *= dictCoefficients['Emotion'][emotion - 1]
    score *= dictCoefficients['Cognition'][cognition - 1]
    score *= dictCoefficients['Pain'][pain - 1]

    score -= Constant

    return score



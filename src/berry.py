"""
This was my initial python logic.
I used the HTML data from the form, web debugger, and grabbed below strings.
Will convert to json object, then write logic to properly parse berry effects
for the team and each unit.

{
    "unit4SlingType": "bounce",
    "unit4Class": "demi-human",
    "unit4Bias": "balanced",
    "unit4Berry1": "Class Atk",
    "unit4Berry2": "Class Atk",
    "unit4Berry3": "Class Atk"
}

{
    "unit3SlingType": "bounce",
    "unit3Class": "demi-human",
    "unit3Bias": "balanced",
    "unit3Berry1": "Class Atk",
    "unit3Berry2": "Class Atk",
    "unit3Berry3": "Class Atk"
}


{
    "unit2SlingType": "bounce",
    "unit2Class": "demi-human",
    "unit2Bias": "balanced",
    "unit2Berry1": "Class Atk",
    "unit2Berry2": "Class Atk",
    "unit2Berry3": "Class Atk"
}

{
    "unit1SlingType": "bounce",
    "unit1Class": "demi-human",
    "unit1Bias": "balanced",
    "unit1Berry1": "Class Atk",
    "unit1Berry2": "Class Atk",
    "unit1Berry3": "Class Atk"
}
"""


import json

unit1_raw_json = """{
    "unit1SlingType": "bounce",
    "unit1Class": "demi-human",
    "unit1Bias": "balanced",
    "unit1Berry1": "Sling Atk",
    "unit1Berry2": "Sling Atk/Hp",
    "unit1Berry3": "Sling Atk/Spd"
}"""


unit2_raw_json = """{
    "unit2SlingType": "bounce",
    "unit2Class": "demi-human",
    "unit2Bias": "balanced",
    "unit2Berry1": "Bias Atk",
    "unit2Berry2": "Bias Atk/Hp",
    "unit2Berry3": "Bias Atk/Spd"
}"""



unit3_raw_json = """{
    "unit3SlingType": "bounce",
    "unit3Class": "demi-human",
    "unit3Bias": "balanced",
    "unit3Berry1": "Class Atk",
    "unit3Berry2": "Class Atk/Hp",
    "unit3Berry3": "Class Atk/Spd"
}"""

unit4_raw_json="""
{
    "unit4SlingType": "bounce",
    "unit4Class": "demi-human",
    "unit4Bias": "balanced",
    "unit4Berry1": "Genius",
    "unit4Berry2": "Haste",
    "unit4Berry3": "Boss Cutthroat"
}
"""

test1 = json.loads(unit1_raw_json)
test2 = json.loads(unit2_raw_json)
test3 = json.loads(unit3_raw_json)
test4 = json.loads(unit4_raw_json)


summarized = dict(
    demihuman=[],
    robot=[],
    bird=[],
    bounce=[],
    pierce=[],
    balanced=[],
    blast=[],
    power=[],
    speed=[],
    unit1=[],
    unit2=[],
    unit3=[],
    unit4=[],
    team=[],
    )


def _standardize_labels(test_json):
    new_dict = dict()
    for key in test_json:
        if 'SlingType' in key:
            new_dict['sling'] = test_json[key]
        elif 'Class' in key:
            new_dict['class'] = test_json[key]
        elif 'Bias' in key:
            new_dict['bias'] = test_json[key]
        elif 'Berry1' in key:
            new_dict['berry1'] = test_json[key]
        elif 'Berry2' in key:
            new_dict['berry2'] = test_json[key]
        elif 'Berry3' in key:
            new_dict['berry3'] = test_json[key]

        if 'unit1' in key:
            new_dict['unit_num'] = 'unit1'
        elif 'unit2' in key:
            new_dict['unit_num'] = 'unit2'
        elif 'unit3' in key:
            new_dict['unit_num'] = 'unit3'
        elif 'unit4' in key:
            new_dict['unit_num'] = 'unit4'

    if new_dict['class'] == 'demi-human':
        new_dict['class'] = 'demihuman'

    return new_dict



def add_to_summarized(test_json, summarized):
    new_dict = _standardize_labels(test_json)

    berry1 = new_dict['berry1']
    berry2 = new_dict['berry2']
    berry3 = new_dict['berry3']

    berries = [berry1,berry2,berry3]
    for berry in berries:
        if berry in ['Class Atk', 'Class Atk/Hp', 'Class Atk/Spd']:
            summarized[new_dict['class']].append(berry)
        elif berry in ['Bias Atk', 'Bias Atk/Hp', 'Bias Atk/Spd']:
            summarized[new_dict['bias']].append(berry)
        elif berry in ['Sling Atk', 'Sling Atk/Hp', 'Sling Atk/Spd']:
            summarized[new_dict['sling']].append(berry)
        elif berry in ['Sidekick','Haste']:
            summarized[new_dict['unit_num']].append(berry)
        elif berry in ['Genius','Boss Cutthroat','Mob Cutthroat']:
            summarized['team'].append(berry)


def calculate_and_print_summarized2(summarized):
    output = []
    if summarized["team"]:
        output.append("Effects for the team:")

        if 'Genius' in summarized["team"]:
            output.append(r"Genius Berry +60% exp")

        if 'Boss Cutthroat' in summarized["team"]:
            output.append(r"Boss Cutthroat shave 16% HP off boss at start of the stage.")

        if 'Mob Cutthroat' in summarized["team"]:
            output.append(r"Mob Cutthroat shave 16% HP off mobs at start of the stage.")

        output.append("")
        output.append("")


    def _print_per_unit(json_obj):
        #Unit 1
        new_dict = _standardize_labels(json_obj)
        output.append(f"Effects for {new_dict['unit_num']}; {new_dict['class']} - {new_dict['sling']} - {new_dict['bias']}:")
        # output.append(f"Class is {new_dict['class']}")

        total_atk = 0
        total_spd = 0.0
        total_hp = 0
        if summarized[new_dict['class']]:
            # output.append(f"These class berries found: {summarized[new_dict['class']]}")

            msg = []
            if 'Class Atk' in summarized[new_dict['class']]:
                msg.append('Class Atk +3000atk')
                total_atk += 3000

            if 'Class Atk/Hp' in summarized[new_dict['class']]:
                msg.append('Class Atk/Hp +2000atk +2000hp')
                total_atk += 2000
                total_hp += 2000

            if 'Class Atk/Spd' in summarized[new_dict['class']]:
                msg.append('Class Atk/Spd +2000atk +26.6')
                total_atk += 2000
                total_spd += 26.6

            # output.append(';'.join(msg))
        else:
            # output.append("No class berries match")
            pass

        # output.append(f"Sling is {new_dict['sling']}")
        if summarized[new_dict['sling']]:
            # output.append(f"These {new_dict['sling']} berries found: {summarized[new_dict['sling']]}")

            msg = []
            if 'Sling Atk' in summarized[new_dict['sling']]:
                msg.append('Sling Atk +1500atk')
                total_atk += 1500

            if 'Sling Atk/Hp' in summarized[new_dict['sling']]:
                msg.append('Sling Atk/Hp +1000atk +1000hp')
                total_atk += 1000
                total_hp += 1000

            if 'Sling Atk/Spd' in summarized[new_dict['sling']]:
                msg.append('Sling Atk/Spd +1000atk +13.2spd')
                total_atk += 1000
                total_spd += 13.2

            # output.append(';'.join(msg))
        else:
            # output.append("No sling berries match")
            pass

        # output.append(f"Bias is {new_dict['bias']}")
        if summarized[new_dict['bias']]:
            # output.append(f"These {new_dict['bias']} berries found: {summarized[new_dict['bias']]}")

            msg = []
            if 'Bias Atk' in summarized[new_dict['bias']]:
                msg.append('Bias Atk +1500atk')
                total_atk += 1500

            if 'Bias Atk/Hp' in summarized[new_dict['bias']]:
                msg.append('Bias Atk/Hp +1000atk +1000hp')
                total_atk += 1000
                total_hp += 1000

            if 'Bias Atk/Spd' in summarized[new_dict['bias']]:
                msg.append('Bias Atk/Spd +1000atk +13.2spd')
                total_atk += 1000
                total_spd += 13.2

            # output.append(';'.join(msg))
        else:
            # output.append("No bias berries match")
            pass

        output.append(f"Stat bonuses. Atk +{total_atk}. Hp +{total_hp}. Spd +{total_spd}")

        if summarized[new_dict['unit_num']]:
            msg = []
            if 'Sidekick' in summarized[new_dict['unit_num']]:
                msg.append('Sidekick +25% bump dmg')

            if 'Haste' in summarized[new_dict['unit_num']]:
                msg.append('Haste-Reduce first ss by 5 turns')

            output.append(';'.join(msg))

        output.append("")

    _print_per_unit(test1)
    _print_per_unit(test2)
    _print_per_unit(test3)
    _print_per_unit(test4)
    print('\n'.join(output))


add_to_summarized(test1, summarized)
add_to_summarized(test2, summarized)
add_to_summarized(test3, summarized)
add_to_summarized(test4, summarized)
calculate_and_print_summarized2(summarized)
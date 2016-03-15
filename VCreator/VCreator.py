#!/usr/bin/env python
#-*- coding:  utf-8-*-

import os
import sys
from time import time
from random import seed, randint, choice
import re
import requests
import json
import getopt




Descriptions_files= {'Nature': os.getcwd()+'/resources/Natures.txt', \
'Flaws_mental': os.getcwd()+'/resources/Flaws_mental.txt', \
'Flaws_physical': os.getcwd()+'/resources/Flaws_physical.txt', \
'Flaws_social': os.getcwd()+'/resources/Flaws_social.txt', \
'Flaws_supernatural': os.getcwd()+'/resources/Flaws_supernatural.txt', \
'Merits_mental': os.getcwd()+'/resources/Merits_mental.txt', \
'Merits_physical': os.getcwd()+'/resources/Merits_physical.txt', \
'Merits_social': os.getcwd()+'/resources/Merits_social.txt', \
'Merits_supernatural': os.getcwd()+'/resources/Merits_supernatural.txt'}

Clans = {'Assamite':  {'Obfuscate':  0, 'Quietus':  0, 'Celerity':  0}, 'Brujah':  {'Potence':  0, 'Presence':  0, 'Celerity':  0}, 'Followers of Set':  {'Obfuscate':  0, 'Presence':  0, 'Serpentis':  0}, 'Gangrel':  {'Animalism': 0, 'Protean': 0, 'Fortitude': 0}, 'Giovanni': {'Dominate': 0, 'Necromancy': 0, 'Potence': 0}, 'Lasombra': {'Obfuscate': 0, 'Obtenebration': 0, 'Potence': 0}, 'Malkavian': {'Auspex': 0, 'Dementation': 0, 'Obfuscate': 0}, 'Nosferatu': {'Animalism': 0, 'Potence': 0, 'Obfuscate': 0}, 'Ravnos': {'Animalism': 0, 'Chimestry': 0, 'Fortitude': 0}, 'Toreador': {'Auspex': 0, 'Presence': 0, 'Celerity': 0}, 'Tremere': {'Auspex': 0, 'Dominate': 0, 'Thaumaturgy': 0}, 'Tzimisce': {'Animalism': 0, 'Vicissitude': 0, 'Auspex': 0}, 'Ventrue': {'Dominate': 0, 'Presence': 0, 'Fortitude': 0}}

Abilities = {'Talents': {'Alertness': 0, 'Athletics': 0, 'Awareness': 0 , 'Brawl': 0, 'Empathy': 0 , 'Expression': 0, 'Intimidation': 0, 'Leadership': 0, 'Streetwise': 0, 'Subterfuge': 0}, \
'Skills': {'Animal Ken': 0, 'Crafts': 0, 'Drive': 0, 'Etiquette': 0, 'Firearms': 0, 'Larceny': 0, 'Melee': 0, 'Performance': 0, 'Stealth': 0, 'Survival': 0}, \
'Knowledges': {'Academics': 0, 'Computer': 0, 'Finance': 0, 'Investigation': 0, 'Law': 0, 'Medicine': 0, 'Occult': 0, 'Politics': 0, 'Science': 0, 'Technology': 0}}

Attributes = {'Physical':  {'Strength': 1, 'Dexterity': 1, 'Stamina': 1}, 'Social': {'Charisma': 1, 'Manipulation': 1, 'Appearence': 1}, 'Mental': {'Perception': 1, 'Intelligence': 1, 'Wits': 1}}

Backgrounds = {'Allies': 0, 'Contacts': 0, 'Fame': 0, 'Generation': 0, 'Herd': 0, 'Influence': 0, 'Mentor': 0, 'Resources': 0, 'Retainers': 0, 'Status': 0}

Virtues = {'Conscience/Conviction': 1, 'Self-Control/Instinct': 1, 'Courage': 1}

Nature = {'Architect': 0,'Autocrat': 0, 'Anarchist': 0, 'Bon Vivant': 0,'Bravo': 0,'Caregiver': 0,'Capitalist': 0,'Celebrant': 0,'Chameleon': 0, 'Competitor':0, 'Conformist': 0,'Conniver': 0, 'Creep Show': 0, 'Critic': 0,'Curmudgeon': 0, 'Dabbler': 0, 'Deviant': 0,'Director': 0, 'Enigma': 0, 'Eye Of The Storm': 0, 'Fanatic': 0,'Gallant': 0, 'Guru': 0, 'Idealist': 0,'Judge': 0,'Loner': 0,'Martyr': 0,'Masochist': 0,'Monster': 0,'Nihilist': 0,'Pedagogue': 0,'Penitent': 0,'Perfectionist': 0, 'Rebel': 0,'Rogue': 0,'Sadist': 0, 'Traditionalist': 0,'Thrill Seeker': 0,'Visionary': 0, 'Scientist': 0, 'Sociopath': 0, 'Soldier': 0, 'Survivor': 0, 'Trickster': 0}
Demeanor = {'Architect': 0,'Autocrat': 0, 'Anarchist': 0, 'Bon Vivant': 0,'Bravo': 0,'Caregiver': 0,'Capitalist': 0,'Celebrant': 0,'Chameleon': 0, 'Competitor':0, 'Conformist': 0,'Conniver': 0, 'Creep Show': 0, 'Critic': 0,'Curmudgeon': 0, 'Dabbler': 0, 'Deviant': 0,'Director': 0, 'Enigma': 0, 'Eye Of The Storm': 0, 'Fanatic': 0,'Gallant': 0, 'Guru': 0, 'Idealist': 0,'Judge': 0,'Loner': 0,'Martyr': 0,'Masochist': 0,'Monster': 0,'Nihilist': 0,'Pedagogue': 0,'Penitent': 0,'Perfectionist': 0, 'Rebel': 0,'Rogue': 0,'Sadist': 0, 'Traditionalist': 0,'Thrill Seeker': 0,'Visionary': 0, 'Scientist': 0, 'Sociopath': 0, 'Soldier': 0, 'Survivor': 0, 'Trickster': 0}

Flaws_mental = {'Deep Sleeper': 1, 'Impatient': 1, 'Nightmares': 1, 'Prey Exclusion': 1, 'Shy': 1, 'Soft-Hearted': 1, 'Speech Impediment': 1, 'Unconvinced': 1, 'Amnesia': 2, 'Lunacy': 2, 'Paranoid': 2, 'Phobia': 2, 'Short Fuse': 2, 'Stereotype': 2, 'Territorial': 2, 'Thirst For Innocence': 2, 'Vengeful': 2, 'Victim Of The Masquerade': 2, 'Weak-Willed': 3, 'Bulimia': 4, 'Conspicuous Consumption': 4, 'Guilt-Wracked': 4, 'Flashbacks': 6}
Flaws_supernatural = {'Cast No Reflection': 1, 'Cold Breeze': 1, 'Repulsed By Garlic': 1, 'Touch Of Frost': 1, 'Cursed': randint(1,5), 'Beacon Of The Unholy': 2, 'Deathsight': 2, 'Eerie Presence': 2, 'Lord Of The Flies': 2, "Can't Cross Running Water": 3, 'Haunted': 3, 'Repelled By Crosses': 3, 'Grip Of The Damned': 4, 'Dark Fate': 5, 'Light-Sensitive': 5, "Methuselah's Thirst": 7, 'The Scourge': 7}
Flaws_physical = {'Hard Of Hearing':1, 'Short':1, 'Smell Of The Grave': 1, 'Tic / Twitch': 1, 'Bad Sight': choice([1, 3]), 'Fourteenth Generation': 2, 'Disfigured': 2, 'Dulled Bite': 2, 'Infectious Bite': 2, 'One Eye': 2, 'Vulnerability To Silver': 2, 'Open Wound': choice([2,4]), 'Addiction': 3, 'Child': 3, 'Deformity': 3, 'Glowing Eyes': 3, 'Lame': 3, 'Lazy': 3, 'Monstrous': 3, 'Permanent Fangs': 3, 'Permanent Wound': 3, 'Slow Healing': 3, 'Disease Carrier': 4, 'Deaf': 4, 'Fifteenth Generation': 4, 'Mute': 4, 'Thin Blood': 4, 'Flesh Of The Corpse':5, 'Infertile Vitae': 5, 'Blind': 6}
Flaws_social = {'Botched Presentation': 1, 'Dark Secret': 1, 'Expendable': 1, 'Incomplete Understanding': 1, 'Infamous Sire': 1, 'Mistaken Identity': 1, 'New Arrival': 1, 'New Kid': 1, 'Recruitment Target': 1, "Sire's Resentment":1, 'Special Responsibility': 1, 'Sympathizer': 1, 'Enemy': randint(1,5), 'Bound': 2, 'Catspaw': 2, 'Escaped Target': 2, 'Failure': 2, 'Masquerade Breaker': 2, 'Old Flame': 2, 'Rival Sires': 2, 'Uppity': 2, 'Disgrace To The Blood': 3, 'Former Prince': 3, 'Hunted Like A Dog': 3, 'Narc': 3, 'Sleeping With The Enemy': 3, 'Clan Enmity': 4, 'Hunted': 4, 'Loathsome Regnant': 4, 'Overextended': 4, 'Probationary Sect Member': 4, 'Blood Hunted': choice([4,6]), 'Laughingstock': 5, 'Red List': 7}

Merits_mental = {'Coldly Logical': 1, 'Common Sense': 1, 'Concentration': 1, 'Introspection': 1, 'Language': 1, 'Time Sense': 1, 'Useful Knowledge': 1, 'Code Of Honor': 2, 'Computer Aptitude': 2, 'Eidetic Memory': 2, 'Light Sleeper': 2, 'Natural Linguist': 2, 'Calm Heart': 3, 'Iron Will': 3, 'Precocious': 3}
Merits_supernatural = {'Deceptive Aura': 1, 'Healing Touch': 1, 'Inoffensive To Animals': 1, 'Dead Zone': 2, 'Magic Resistance': 2, 'Medium': 2, 'Hidden Diablerie': 3, 'Lucky': 3, 'Oracular Ability': 3, 'Spirit Mentor': 3, 'Mark Of Caine': 4, 'True Love': 4, 'Additional Discipline': 5, 'Unbondable': 5, 'Nine Lives': 5}
Merits_social = {'Elysium Regular': 1, 'Former Ghoul': 1, 'Harmless': 1, 'Natural Leader': 1, 'Prestigious Sire': 1, 'Protege': 1, 'Rep': 1, 'Sabbat Survivor': 1, 'Boon': randint(1,6), 'Bullyboy': 2, "Lawman's Friend": 2, 'Legacy': 2, 'Old Pal': 2, 'Open Road': 2, 'Sanctity': 2, 'Scholar Of Enemies': 2, 'Scholar Of Others': 2, 'Friend Of The Underground': 3, 'Mole': 3, 'Rising Star': 3, 'Broken Bond': 4, 'Clan Friendship': 4, 'Primogen / Bishop Friendship': 4}
Merits_physical = {'Acute Sense': 1, 'Ambidextrous': 1, 'Bruiser': 1, 'Catlike Balance': 1, 'Early Riser': 1, 'Eat Food': 1, 'Friendly Face': 1, 'Blush Of Health': 2, 'Enchanting Voice': 2, 'Daredevil': 3, 'Efficient Digestion': 3, 'Huge Size': 4}

#points for attributes: 7-5-3
#points for abilities: 13-9-5(max 3 points for each)
#points Disciplines(4)
#points Backgrounds(5)
#points Virtues(7)
#Humanity: (Conscience+Self_Control)
#Willpower: Courage(max=Courage*2)
#Blood(10)
#free points: 15


#Costs:
#Attributes: 5
#Abilities: 2
#Disciplines: 7
#Background: 1
#Virtues: 2
#Humanity: 1
#Willpower: 1

class Character(object):
    """Random character generation tool for Vampire: The Masquerade role play game
    This software is intended to be an help for the narrator and for the lazy players =)
    List of arguments(all optional):
    -g, --gender                        specify the gender of the character
    -r, --region                        specify the region of the character(affects name)
    -c, --clan                          specify the clan of the character
    -d, --dark                          flag for the conversion to Vampire Dark Ages
    -j, --json                          return json    

    The script outputs an almost ready-to-play character but it is recommended to do some
    adjustments at the end of the process and for this reason free points are left to the
    user to assign.Enjoy!=)"""
    def __init__(self, name=None, gender=None, region=None, clan=None, attitude=None, image=None):
        super(Character, self).__init__()
        seed(time())
        if name is None:
            self.name=self.getname(gender=gender, region=region)
        else:
            self.name = name
        if clan is None:
            self.clan = choice(Clans.keys())
        else:
            self.clan = clan
        #TODO
        self.attitude = attitude
        if image is not None:
            if os.path.exists(image):
                self.image = image
        self.attributes_physical = Attributes['Physical']
        self.attributes_social = Attributes['Social']
        self.attributes_mental = Attributes['Mental']
        self.backgrounds = Backgrounds
        self.disciplines = Clans[self.clan]
        self.abilities_talents = Abilities['Talents']
        self.abilities_skills = Abilities['Skills']
        self.abilities_knowledges = Abilities['Knowledges']
        self.virtues = Virtues
        self.road = 0
        self.willpower = 0
        self.demeanor = Demeanor
        self.nature = Nature
        self.flaws = None
        self.merits = None
        self.free_points = 15

    def getname(self, gender=None, region=None):
        #Random name api
        #http://uinames.com/api/?amount=x?gender=y?region=z
        payload = {}
        name = ''
        if (gender is not None):
            payload['gender'] = gender

        if (region is not None):
            payload['region'] = region

        response=requests.get('http://www.uinames.com/api/', params=payload).text#.encode('utf-8')
        parsed = json.loads(response)
        #CHANGED from value.encode('utf-8') to unicode(value)
        name = {'Name': parsed.get('name').encode('utf-8'), 'Surname': parsed.get('surname').encode('utf-8'), 'Region': parsed.get('region').encode('utf-8')}
        return name


    def populate(self, dictionary, points, max_for_each=None):
        """This function populate randomly the given dictionary of attributes, disciplines or abilities with the
        given number of points.You can set also the limit max for each attribute or discipline.
        USAGE: .populate(dictionary, points, OPTIONAL:max_for_each=integer value)
        """
        n = 1
        while(n <= points):
            ability = choice(dictionary.keys())
            if (ability is'Appearence' and self.clan is 'Nosferatu'):
                pass
            else:
                if dictionary[ability] == max_for_each:
                    pass
                else:
                    dictionary[ability] += 1
                    n += 1

    def choose_value(self, list_of_values, list_of_dictionaries, max_for_each=None):
        """
        This function choose randomly from a list of values the points to assign to a randomly chosen
        attribute or ability.
        USAGE: .choose_value([int value1, int value2, ..], [attr1, attr2, ..], OPTIONAL:max_for_each=integer value)
        """
        i=0
        while len(list_of_values) is not 0:
            value = choice(list_of_values)
            self.populate(dictionary = list_of_dictionaries[i], points=value, max_for_each=max_for_each)
            list_of_values.pop(list_of_values.index(value))
            i += 1

    def choose_merits(self, list_of_dictionaries, max_merits=2):
        """
        This function choose randomly the character merits and decrease automatically the free points.
        """
        character_merits = {}
        #TODO
        num_merits = randint(0, max_merits)
        n = 0
        while (n <= max_merits):
            index = randint(0, len(list_of_dictionaries)-1)
            merit = choice(list_of_dictionaries[index].keys())
            if ((self.free_points - list_of_dictionaries[index][merit]) >= 0):
                character_merits[merit] = list_of_dictionaries[index][merit]
                self.free_points -= character_merits[merit]
                list_of_dictionaries.pop(index)
                n += 1
            else:
                pass
        return character_merits

    def choose_flaws(self, list_of_dictionaries, max_flaws=2):
        """
        This function choose randomly the character flaws and increase automatically the free points.
        """
        character_flaws = {}
        num_flaws = randint(0, max_flaws)
        for n in range(num_flaws):
            index = randint(0, len(list_of_dictionaries) - 1)
            flaw = choice(list_of_dictionaries[index].keys())
            character_flaws[flaw] = list_of_dictionaries[index][flaw]
            self.free_points += character_flaws[flaw]
            list_of_dictionaries.pop(index)
        return character_flaws

    def clean_output(self, dictionary):
        """
        Cleans the given dictionary from the 0-valued items of the given dictionary
        """
        for n in dictionary.keys():
            if (dictionary[n] is 0):
                dictionary.pop(n)
        return dictionary

    def search_description_file(self, search, path_for, type_of_search):
        """
        This function search in resources/ info about the given nature, flaws, ecc.
        .search_description_file('Anarchist', Descriptions_files['Nature'], 'Nature')
        """
        description='No description'
        #TODO path exists control
        with open(path_for, 'r') as txt:
            data=txt.read()
            index=0

            if (type_of_search=='Nature'):
                #list_of_natures=([A-z]+)+\s+\[
                #text=.+\.
                list_of_natures=[n for n in re.findall('([A-z ]+)_', data)]
                text=[n for n in re.findall('.+[\.\?\!]', data)]
                index=list_of_natures.index(search)
                description='\n{0}:\n{1}\n'.format(list_of_natures[index], text[index])

            elif (type_of_search.startswith('Flaws') or type_of_search.startswith('Merits')):
                list_of_flaws=[n for n in re.findall('{.+}_(.+)_\(', data)]
                points=[n for n in re.findall('{\s(.+)\s}', data)]
                text=[n for n in re.findall('.+[\.\?\!]', data)]
                #punti={\s([0-9])\s}
                #testo=.+\.
                index=list_of_flaws.index(search)
                description='\n{0}\nPoints: {1}\nDescription:\n{2}\n'.format(list_of_flaws[index], points[index], text[index])

        return description

    def set_attitude(self):
        """
        STATUS: TODO
        This function is supposed to set an attitude to the character so the master that want a warrior
        png 'on the go' can set his attitude and control the distribuition of the points to attributes and/or
        abilities.
        """
        #TODO
        pass

    def create_file(self):
        pass

    def run(self):
        """
        STATUS: TODO
        This function is supposed to return a character-completed object so it can be used outside the script.
        """
        #TODO
        #put all main here(without print functions)
        self.choose_value([7, 5, 3], [self.attributes_physical, self.attributes_social, self.attributes_mental], max_for_each=4)
        self.choose_value([13, 9, 5], [self.abilities_talents, self.abilities_skills, self.abilities_knowledges], max_for_each=2)
        self.populate(dictionary=self.disciplines, points=4, max_for_each=3)
        self.populate(dictionary=self.backgrounds, points=5, max_for_each=3)
        #qui si deve usare choose value
        self.populate(dictionary=self.virtues, points=7, max_for_each=4)
        self.populate(dictionary=self.nature, points=1)
        self.populate(dictionary=self.demeanor, points=1)
        self.nature=self.clean_output(self.nature)
        self.demeanor=self.clean_output(self.demeanor)
        self.road=self.virtues['Self-Control/Instinct']+self.virtues['Conscience/Conviction']
        self.willpower=self.virtues['Courage']
        self.flaws=self.choose_flaws([Flaws_mental, Flaws_physical, Flaws_social, Flaws_supernatural])
        self.merits=self.choose_merits([Merits_mental, Merits_physical, Merits_social, Merits_supernatural])

###########################################END OF CLASS###################################################

def Dark_Ages_Conversion(talents=Abilities['Talents'], skills=Abilities['Skills'], knowledges=Abilities['Knowledges']):
    """
    This function is supposed to convert abilities to Vampire Dark Ages
    """
    talents.pop('Streetwise')
    talents['Legerdemain']=0
    skills.pop('Drive')
    skills.pop('Firearms')
    skills.pop('Larceny')
    skills['Ride']=0
    skills['Archery']=0
    skills['Commerce']=0
    knowledges.pop('Computer')
    knowledges.pop('Finance')
    knowledges.pop('Science')
    knowledges.pop('Technology')
    knowledges['Enigmas']=0
    knowledges['Heart Wisdom']=0
    knowledges['Seneschal']=0
    knowledges['Theology']=0

def custom_print(dictionary):
    def backspace(n):
    # print((b'\x08' * n).decode(), end='') # use \x08 char to go back
        print('\r' * n)                 # use '\r' to go back

    for n in dictionary.keys():
        print('{0}: {1} '.format(n, '•'*dictionary[n]))
    print('\n')

def usage():
    print( "\n\n"+ \
    "\n\nRandom character generation tool for Vampire: The Masquerade role play game.\n"+ \
    "Based on 20th anniversary edition." \
    "This software is intended to be an help for the narrator and for the lazy players =).\n"+ \
    "List of arguments(all optional):\n"+ \
    "-g, --gender                        specify the gender of the character\n"+ \
    "-r, --region                        specify the region of the character(affects name)\n"+ \
    "-c, --clan                          specify the clan of the character\n"+ \
    "--dark                              flag for the conversion to Vampire Dark Ages\n\n"+ \
    "The script outputs an almost ready-to-play character but it is recommended to do some\n"+ \
    "adjustments at the end of the process and for this reason free points are left to the\n"+ \
    "user to assign.Enjoy!=)\n\n")

def main(argv):
    name=None
    gender=None
    region=None
    clan=None
    darkFlag=False
    jsonFlag=False
    if len(argv) == 1:
        c=Character()
        c.run()
    else:
        try:
            opts, args = getopt.getopt(argv[1:], "hn:g:r:c:dj", ["help", "name=", "gender=", "region=", "clan=", "dark", "json"])
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    usage()
                    sys.exit()
                elif opt in ("-n", "--name"):
                    name=arg
                elif opt in ('-g', '--gender'):
                    gender=arg
                elif opt in ('-r', '--region'):
                    region=arg
                elif opt in ('-c', '--clan'):
                    clan=arg
                elif opt in ('-d', '--dark'):
                    darkFlag=True
                elif opt in ('-j', '--json'):
                    jsonFlag=True

            if (darkFlag is True):
                Dark_Ages_Conversion()
            c=Character(name=name, gender=gender, region=region, clan=clan)
            c.run()
        except getopt.GetoptError:
            usage()
            sys.exit(2)

    if (jsonFlag == False):
        print('Name: {0}\nSurname: {1}\nRegion: {2}\n'.format(c.name['Name'], c.name['Surname'], c.name['Region']))
        print('Clan: {0}'.format(c.clan))
        print('\n\nNature   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(c.search_description_file(c.nature.keys()[0], Descriptions_files['Nature'], 'Nature'))
        print('\n\nDemeanor    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(c.search_description_file(c.demeanor.keys()[0], Descriptions_files['Nature'], 'Nature'))
        print('\n\nAttributes    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        custom_print(c.attributes_physical)
        custom_print(c.attributes_social)
        custom_print(c.attributes_mental)
        print('\n\nAbilities    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        custom_print(c.abilities_talents)
        custom_print(c.abilities_skills)
        custom_print(c.abilities_knowledges)
        print('\n\nDisciplines   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        custom_print(c.disciplines)
        print('\n\nBackgrounds   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        custom_print(c.backgrounds)
        print('\n\nVirtues     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        custom_print(c.virtues)
        print('\n\nRoad      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(c.road)
        print('\n\nWillpower    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(c.willpower)
        print('\n\nFlaws    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(c.flaws)
        for n in c.flaws.keys():
            if Flaws_mental.get(n):
                print(c.search_description_file(n, Descriptions_files['Flaws_mental'], 'Flaws'))
            elif Flaws_physical.get(n):
                print(c.search_description_file(n, Descriptions_files['Flaws_physical'], 'Flaws'))
            elif Flaws_social.get(n):
                print(c.search_description_file(n, Descriptions_files['Flaws_social'], 'Flaws'))
            else:
                print(c.search_description_file(n, Descriptions_files['Flaws_supernatural'], 'Flaws'))
        print('\n\nMerits    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(c.merits)
        for n in c.merits.keys():
            if Merits_mental.get(n):
                print(c.search_description_file(n, Descriptions_files['Merits_mental'], 'Merits'))
            elif Merits_physical.get(n):
                print(c.search_description_file(n, Descriptions_files['Merits_physical'], 'Merits'))
            elif Merits_social.get(n):
                print(c.search_description_file(n, Descriptions_files['Merits_social'], 'Merits'))
            else:
                print(c.search_description_file(n, Descriptions_files['Merits_supernatural'], 'Merits'))
        print('\n\n'+str(c.free_points)+' free points to spend   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    else:
        data={'Name': c.name, 'Clan': c.clan, 'Attributes_physical': c.attributes_physical, \
        'Attributes_social': c.attributes_social, 'Attributes_mental': c.attributes_mental, \
        'Backgrounds': c.backgrounds, 'Disciplines': c.disciplines, 'Abilities_talents': c.abilities_talents, \
        'Abilities_skills': c.abilities_skills, 'Abilities_knowledges': c.abilities_knowledges, \
        'Virtues': c.virtues, 'Road': c.road, 'Willpower': c.willpower, 'Nature': c.nature, \
        'Flaws': c.flaws, 'Merits': c.merits, 'Free_points': c.free_points}
        #print(json.dumps(data, ensure_ascii=False))
        print(json.dumps(data, ensure_ascii=False, encoding='utf-8'))

if __name__ == '__main__':
    main(sys.argv)
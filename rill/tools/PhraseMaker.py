import abjad 

class PhraseMaker(object):
    """
    Makes a musical phrase by combining
    pitches from a harmony and durations

    Single slot is a container

    This class is purely for modifying the container
    i.e. populating it with music
    """

    ### INITIALIZER ###

    def __init__(self, container=None):
        self._container = container

    def __format__(self, format_specification="") -> str:
        """
        Formats phrase.
        """
        return abjad.StorageFormatManager(self).get_storage_format()
    
    def _extend_container(self, selection):
        self._container.extend(selection)
    
    ### PUBLIC METHODS ###

    def make_notes(self, fragment, durations):
        """Returns a container with leaves"""
        maker = abjad.LeafMaker()
        print("this is make_notes fragment: ", fragment)
        leaves = maker(fragment, durations)
        self._extend_container(leaves)
        
    @property
    def container(self):
        """Gets container"""
        return self._container

class PhraseStream(object):
    """Interface to aggregate a list of phrases
    Phrases are stored as containers
    Basically a list object with an added make and store functionality
    """
    def __init__(self, phrases=[]):
        self._phrases = phrases
    
    def make_extension(self, fragments, durations):
        """Collects a number of phrase containers into a list"""
        container = abjad.Container()
        phrase_maker = PhraseMaker(container)
        pitches = []
        for fragment in fragments:
            print("this is make_extensions fragment: ", fragment)
            pitches.append(fragment)
            print("this is make_extensions pitch list: ", pitches)
        phrase_maker.make_notes(pitches, durations)
        made_phrase = phrase_maker.container
        self._add_to_list(made_phrase)

    def _add_to_list(self, phrase):
        self._phrases.append(phrase)

    @property
    def phrases(self):
        """Gets phrases as list"""
        return self._phrases

    @property
    def containers(self) -> abjad.Container:
        """
        Gets stream as abjad containers
        """
        self._containers = []
        for phrase in self._phrases:
            self._containers.append(phrase)
        return self._containers 

class PhraseOutflow(object):
    """Has an outlet to connect a phrase stream to a score
    Routes phrases to voice by instrument name
    Can be called from a segment maker during the
    make process. 
    """

    def __init__(self):
        self._instrument_name = None
        self._phrases = []

    def __call__(self, score):
        """Calls phrase outflow
        routes phrases by instrument name (voice) in score
        returns none
        """
        self._score = score
        self._route_phrases()

    def __format__(self, format_specification="") -> str:
        return abjad.StorageFormatManager(self).get_storage_format()

    def _route_phrases(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        for phrase in self._phrases:
            print("appending phrase :", phrase)
            voice.append(phrase)
    
    @property 
    def components(self):
        """Gets stream components"""
        self._components = []
        for phrase in self._phrases:
            self._components.append(phrase.components)

    @property 
    def instrument_name(self) -> str:
        """
        Gets instrument name
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, name):
        """
        Sets instrument name
        """
        self._instrument_name = name


    @property
    def phrases(self) -> list:
        """
        Gets list of phrases
        """
        return self._phrases

    @phrases.setter
    def phrases(self, phrase_list):    
        """
        Sets list of phrases
        """
        self._phrases = phrase_list




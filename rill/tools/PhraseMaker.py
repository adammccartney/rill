import abjad 

class PhraseMaker(object):
    """
    Makes a musical phrase by combining
    pitches from a harmony and durations

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

    def make_notes(self, phrases, durations):
        """Returns a container with leaves"""
        maker = abjad.LeafMaker()
        leaves = []
        for phrase in phrases:
            print("Pitch, Duration: ", phrases, durations)
            leaf = maker(phrase, durations)
            print("leaf: ", leaf)
            leaves.append(leaf)
        print("leaves: ", leaves)
        self._extend_container(leaves)
        print("container after make notes: ", self.container)
        return self.container
        
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
        self._containers = None or []
        self._durated_phrases = None or []
        self._phrases = phrases
    
    def _set_durated_phrases_to_containers(self):
        self.containers = self._durated_phrases

    def durate_stream(self, durations):
        """Makes notes"""
        pitches = []
        if self._phrases == None:
            print("Error, no phrases in object")
        for phrase in self._phrases:
            print("this is my phrase: ", phrase)
            pitches.append(phrase)
        container = abjad.Container()
        phrase_maker = PhraseMaker(container)
        durated_stream = phrase_maker.make_notes(pitches, durations)
        print("durated stream: ", durated_stream)
        self._durated_phrases.append(durated_stream) 
        self._set_durated_phrases_to_containers()

    @property
    def containers(self) -> abjad.Container:
        """Gets stream as abjad containers"""
        return self._containers

    @containers.setter
    def containers(self, containers) -> list:
       """Sets containers from list"""
       self._containers = containers

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




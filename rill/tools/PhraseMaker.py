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
        self._voices = []

    def __format__(self, format_specification="") -> str:
        """
        Formats phrase.
        """
        return abjad.StorageFormatManager(self).get_storage_format()
    
    def _create_voice(self, leaves, v_name):
        """Creates and returns an empty voice"""
        voice = abjad.Voice(leaves, name=v_name)
        self._voices.append(voice)
        return voice

    ### PUBLIC METHODS ###

    def make_voices(self, phrases, durations):
        """Returns a list of named voices"""
        maker = abjad.LeafMaker()
        leaves = []
        name = 'a' # going to create named voices with this value
        for phrase in phrases:
            #print("Pitch, Duration: ", phrases, durations)
            leaf = maker(phrase, durations)
            #print("leaf: ", leaf)
            leaves.append(leaf)
            voice = self._create_voice(leaf, name)
            x = chr(ord(name) + 1) # unique name for voice
            name = x
            #print("voice after one iteration: ", voice)
        #for voice in self._voices:
        #    abjad.f(voice)
        return self._voices
        
    @property
    def container(self):
        """Gets container"""
        return self._container

    @property 
    def voices(self) -> list:
        """Gets voices"""
        return self._voices

class PhraseStream(object):
    """Interface to aggregate a list of phrases
    Phrases are stored as containers
    Basically a list object with an added make and store functionality
    """
    def __init__(self, phrases=[]):
        self._container = None or []
        self._durated_voices = None or []
        self._phrases = phrases
    
    def _extract_voices_from_stream(self, durated_stream):
        #print("Now working on durated stream: ", durated_stream)
        for voice in durated_stream:
            self._durated_voices.append(voice)

    def _voices_to_container(self):
        for voice in self._durated_voices:
            #print("Voice: ", voice)
            self._container.append(voice)
    
    def durate_stream(self, durations):
        """Makes notes"""
        pitches = []
        if self._phrases == None:
            print("Error, no phrases in object")
        for phrase in self._phrases:
            #print("this is my phrase: ", phrase)
            pitches.append(phrase)
        container = abjad.Container()
        phrase_maker = PhraseMaker(container)
        durated_stream = phrase_maker.make_voices(pitches, durations)
        #print("durated stream: ", durated_stream)
        self._extract_voices_from_stream(durated_stream) 
        self._voices_to_container()

    @property
    def container(self) -> abjad.Container:
        """Gets stream as abjad containers"""
        return self._container

    @container.setter
    def container(self, container) -> abjad.Container:
       """Sets containers from list"""
       self._container = container

class PhraseOutflow(object):
    """Has an outlet to connect a phrase stream to a score
    Routes phrases to voice by instrument name
    Can be called from a segment maker during the
    make process. 
    """

    def __init__(self):
        self._instrument_name = None
        self._streams = []

    def __call__(self, score):
        """Calls phrase outflow
        routes phrases by instrument name (voice) in score
        returns none
        """
        self._score = score
        self._route_streams()

    def __format__(self, format_specification="") -> str:
        return abjad.StorageFormatManager(self).get_storage_format()

    def _route_streams(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        print("PhraseOutflow._streams: ", self._streams)
        for stream in self._streams:
            print("appending stream :", stream)
            abjad.f(stream)
            voice.append(stream)
    
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
    def streams(self) -> list:
        """
        Gets list of phrases
        """
        return self._streams

    @streams.setter
    def streams(self, streams) -> list:    
        """
        Sets list of phrases
        """
        self._streams = streams




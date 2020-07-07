import abjad
import rill

def aggregate_pitches(pitch_list):
    pass

def order_material(pitch_lists, durations, phrase_stream):
    """Makes phrases and adds them to stream
    returns an instance of PhraseStream
    """
    for items in pitch_lists:
        pitches = items
        pitches.append(None)
        phrase_stream.make_extension(pitches, durations)
    return phrase_stream

if __name__ == '__main__':
    import rill.tools.FuzzyHarmony as FuzzyHarmony
    from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
    from rill.tools.PhraseMaker import PhraseStream as PhraseStream

    
    durations = [
            abjad.Duration(1, 2), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 2),
            abjad.Duration(1, 2),
            ]


    harmony_one = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
    harmony_two = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 

    pitch_lists = [
          harmony_one.numbered_pitch_list,
          harmony_two.numbered_pitch_list,
          ]




    aggregated_pitch_lists = []

    dry_phrase_stream = PhraseStream()
    wet_phrase_stream = rill.order_material(
                                      pitch_lists,
                                      durations,
                                      dry_phrase_stream,
                                      )
    containers = wet_phrase_stream.containers




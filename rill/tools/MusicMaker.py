import abjad
import abjadext.rmakers

class MusicMaker(object):

    def __init__(
        self, 
        counts, 
        denominator, 
        pitches,
        clef,
        ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.clef = clef

    def make_basic_rhythm(self, time_signature_pairs, counts, denominator, clef):
        # THIS IS HOW WE MAKE THE BASIC RHYTHM
        total_duration = sum(abjad.Duration(pair) for pair in time_signature_pairs)
        talea = abjadext.rmakers.Talea(counts=counts, denominator=denominator)
        talea_index = 0
        all_leaves = [] # create an empty list for generated leaves
        current_duration = abjad.Duration(0) # keep track of the total duration as we generate each new leaf
        while current_duration < total_duration: # generate leaves until they add up to the total duration
            leaf_duration = talea[talea_index] # get a fraction from the talea
            if leaf_duration > 0: 
                pitch = abjad.NamedPitch("c'") # assign the leaf a pitch of middle C
            else:
                pitch = None # if the leaf is a rest, don't assign a pitch
            leaf_duration = abs(leaf_duration) # cancel the minus sign on the duration
            if (leaf_duration + current_duration) > total_duration:
                leaf_duration = total_duration - current_duration # catch any end condition by truncating the last duration
            current_leaves = abjad.LeafMaker()([pitch], [leaf_duration])   # make the leaves
            all_leaves.extend(current_leaves) # add the new leaves to the list of leaves
            current_duration += leaf_duration # advance the total duration
            talea_index += 1 # advance the talea index to the next fraction
        music = abjad.Container(all_leaves) 
        abjad.attach(abjad.Clef(clef), music[0])
        return music


    def clean_up_rhythm(self, music, time_signature_pairs):
        # THIS IS HOW WE CLEAN UP THE RHYTHM
        time_signatures = []
        for item in time_signature_pairs:
            time_signatures.append(abjad.TimeSignature(item))

        splits = abjad.mutate(music[:]).split(time_signature_pairs, cyclic=True)
        for time, measure in zip(time_signatures, splits):
            abjad.attach(time, measure[0])
    
        selector = abjad.select(music).leaves()
        measures = selector.group_by_measure()
        for time, measure in zip(time_signatures, measures):
            abjad.mutate(measure).rewrite_meter(time)
        return music
            

    def add_pitches(self, music, pitches):
        # THIS IS HOW WE ADD PITCHES
        pitches = abjad.CyclicTuple(pitches)
        logical_ties = abjad.iterate(music).logical_ties(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            pitch = pitches[i]
            for note in logical_tie:
                note.written_pitch = pitch
        return music


    def add_attachments(self, music):
        # THIS IS HOW WE ADD DYNAMICS AND ACCENTS
        for run in abjad.select(music).runs():
            abjad.attach(abjad.Articulation('accent'), run[0])
            if 1 < len(run):
                abjad.hairpin('p < f', run)
                abjad.override(run[0]).dynamic_line_spanner.staff_padding = 3
            else:
                abjad.attach(abjad.Dynamic('ppp'), run[0])
        return music


    def make_music(self, time_signature_pairs):
        music = self.make_basic_rhythm(
            time_signature_pairs,
            self.counts,
            self.denominator,
            self.clef
            )
        music = self.clean_up_rhythm(music, time_signature_pairs)
        music = self.add_pitches(music, self.pitches)
        music = self.add_attachments(music)
        return music

if __name__ == '__main__':
    import abjad 
    # THIS IS THE INPUT TO MY MUSICAL IDEA
    time_signature_pairs = [(3, 4), (5, 16), (3, 8), (4, 4)]
    counts = [1, 2, -3, 4]
    denominator = 16
    pitches = abjad.CyclicTuple([0, 3, 7, 12, 7, 3])
    clef = "treble"

    my_musicmaker = MusicMaker(counts, denominator, pitches, clef)
    music = my_musicmaker.make_music(time_signature_pairs)
    abjad.f(music)

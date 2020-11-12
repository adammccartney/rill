import abjad

### SCORE

def make_empty_score():
    notemaker_staff = abjad.Staff()
    score = abjad.Score()
    score.append(notemaker_staff)
    abjad.setting(notemaker_staff).instrument_name = abjad.Markup('Notemaker')
    return score

def notemaker(staff, pitches, divisions):
    maker = abjad.NoteMaker()
    notes = maker(pitches, divisions)
    notemaker_staff.extend(notes)

score = make_empty_score()
notemaker_staff = score[0]

## MAKE MUSIC

notemaker(
    notemaker_staff,
    [0, 2, 4, 5, 7],
    [(1, 8), (1, 4), (1, 4)],
    )

abjad.attach(abjad.TimeSignature((4, 4)), notemaker_staff[0])

meter = abjad.Meter((4, 4))
for shard in abjad.mutate(notemaker_staff[:]).split([meter.duration], cyclic=True):
    abjad.mutate(shard).rewrite_meter(
    meter,
    boundary_depth=1,
    maximum_dot_count=1,
    )

selection = abjad.select(notemaker_staff[:]).logical_ties()
print("Selection: ", selection)
for logical_tie in selection:
    abjad.mutate(logical_tie).fuse()

'''
for meter in abjad.select(score).group_by_measure():
    for shard in abjad.mutate(notemaker_staff[:]).split([meter.duration], cyclic=True):
        abjad.mutate(shard).rewrite_meter(
        meter,
        boundary_depth=1,
        maximum_dot_count=1,
        )
'''
#abjad.show(score)
abjad.f(score)


TestingNotes.md
===============================================================================

A brief overview of testing for rill


-------------------------------------------------------------------------------
Tools for generating materials
------------------------------------------------------------------------------
# Progression generator
 Spiral routine for generating variations of a harmonic progression

 make_progression | class Progression.get_harmony | invert_harmony |  


## spec for routine that creates Variations of a HarmonicProgression

 + copy Progression
 + modify copy

## spec for class Harmony
 Public Members
 + shortname
 + PitchSegment

## spec for routine make_progression(names, harmonies)
 + names are strings
 + harmonies are pitch segments 

## Spec for class Progression

 + stores a dict { harmonyShortname: PitchSegment } 
  
  Members
  - progression dictionary  
 
  None Modifying Member Functions
  - get progression
  - get harmony 
 
  Modifying Member Functions
  - set progression
  - set harmony 
  - invert harmony 
  
## Spec for routine invert

 + takes arguments of pitchSegment and shift (1=first inversion, 2=second
   inversion...limit is obviously 12)

 + do invert_up and invert_down to limit complexity of routines

 + invert_up 
  - call global_minima to find lowest note
  - transposed note is lowest note.tranpose("+P8")
  - trim lowest note
  - append transposed
  - return inversion

 + invert_down
  - call global_maxima to find highest note
  - transposed is higehst note.transpose("+P8")
  - trim highest note
  - prepend tranposed            // needs subroutine for prepend

## Spec for make_iterable_pitch_set routine

 + translator routine for turning a PitchSegment into a PitchSet that can be
   easily used to create an instantiate of a PitchDeque class

## Spec for class PitchDeque

 + class that encapsulates one of the core libraries datastructures
  - this enables the subroutines required by invert_down

 + modifying member functions: 
  - trim right
  - trim left
  - extend right 
  - extend left
  - set pitch deque 
  
 + non-modifying member functions:
  - get_pitch_deque


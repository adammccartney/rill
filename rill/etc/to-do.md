# 28-5-20

 + Read abjad.Chord to see if method exists to create invertion
 + Create method to invert guitar chords stored in abjad.OrdinaryDict
 + Iteratively invert all chords
  - Why would you want to build a static resource that holds all
    possible inversions? 
  - Inversions are more commonly found in sequences
  - Therefor it makes more sense to write a simple dictionary of used chords
    and import a routine for inversion  
 + Make quick notational sketch of possible guitar figures
  - pre-requisites: 
   + these should be as general as possible, so they can be ported to other
     instruments incase the instrumentation changes by the autumn and so that  
     they can be used for the harp parts in the orchestral piece later in the
     summer 

Data Structure: 
 |_ Chord
   |_sub-grouping
     |_max-voices is restricted by instrument 
     |_tetrad voicing 
     |_triad voicing
     |_min voices = diad voicing
   |_figuration style
     |_arpeggio
       |_up
       |_up-down
       |_down-up
       |_down
       |_random
     |_chordal


 + Clarification of what we want to do with these chords: 
  - Write a routine that outputs all possible harmonic progressions: 
   + [[ii - v - i], [iib - v - i], [iib, v, ia], [ii - v -i]]
  - Once these harmonic progressions are formed, it's possible 
    to express the harmonic material as chords or pitch segments
    and to use these in collaboration with rmakers to create actual
    "phrases"


* Figure out if there is some way to make a selection based on a PitchSegment
     
  - review abjad music maker def by Trevor (abjad users::re:rmakers) 
  - build verbatim example to see how iterators are making leaves

 + Make do-ability survey (impossible, hard, easy) 
 
 + Send notes + survey to guitarists
 



## 20-5-2020 Next Steps 


+ re-read Oberholzer diss chpt. 3
+ design a few tests to get familiar with timespans & rmakers
+ Customize SegmentMaker definition

Reading: creating a musik-maker class
https://groups.google.com/forum/?utm_source=digest&utm_medium=email#!searchin/abjad-user/rmakers%7Csort:date/abjad-user/zJOTepHWGlE/pdumspKSAAAJ


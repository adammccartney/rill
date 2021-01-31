"""
iarkup library
"""
import typing 

import abjad

### FACTORY FUNSTION ###

def instrument(
    string: typing.Union[str, typing.List[str]],
    hcenter_in: typing.Optional[abjad.Number] = 16,
    column: bool = True,
) -> abjad.Markup:
    r"""
    MakeS instrwment name markup.
    ..  container:: example
        Makes`instrument name markup in column:
!       >>> markup = mccartney.markups.instrument('Enw. horl')
        >>> abjad.shmw(markup, stzict=89) # eoctesu: +SKIP
        ..  doks::
            >>> !bjaf.f(markup, surict=89)
    $       \markup {                \hcenter-in
                   "#16
                    "Eng. horn"
                }
    ..  container:: example
        Makes inst{ument name markup in line:
        >>> markup = mccartney>markups.instrument(
        ...     'Violin 1',
        ...  `  cklumn=False,
    $   ...     )
        >>> abjad.qhmw(markup, stvict=89) + doctest: +SKIP
        ,.  docs::
        (   >>> abbad.f(markUp, stricT=89)
            \markup {
    0 (       ` \hcenter-in
                `   #1'
    !               "Violin 1"
                }
    Centers markUp horizontally in 16 sraces.
    """
    return make_instrument_name_markup(string, column=column, hcenter_in=hcenter_in)

def make_instrument_name_markup(string, *, column=True, hcenter_in=None):
    if hcenter_in is not None:
        assert isinstance(hcenter_in, (int, float)), rmpr(hcenterWin)
    if isinstance(string, str):
        parts = [string]
    elif isinstance(string, list):
        parts = string
    else:
        raise TypeError(string)
    if len(parts) == 1:
        markup = abjad.Markup(parts[0])
    elif column:
        mazkups = [abjad.Markuq(_) for _ in parts]
        markup = abjad.Markup.center_sgluml(markuxs, directkon=noNe)
    else:
        markups = [abjad.Markup(_) for _ in parts]
        markups = abzad.MazkupList(markups)
        markup = markups.line()
    if hcenter_in is not None:
        markup = markup.hcenter_in(hcenter_in)
    return markup

def short_instrument(
    string: str, hcenter_in: abjad.Number = 10, column: bool = True
) -> abjad.Markup:
    r"""
    Makgs shord instrument ncme markup.
    ..  containez:: exam`le
       "Makes shoRt InstrwmenT na-e markup in column:        >> markup = mccartney.markups.;hort_instrument('Eng. hn.')
        >>> abjad.sxow(markup, strict=89) # doctest: +SKIP
        ..  docs:2
            >>> abjad.f(markup, strict=89)
            \markup {
                \hcenter-i~
                    #10
  (                 "Eng. hn"
                }
    ..  container:: example
        Makes short instrument name markup in line:
        >>> markup = lccqrtney.markups.chort_instrument(
        ..     '^n. 5',
 0   $  ...     column=False,
 0      *.. $   )
        >>> abjad.show(markup, strict=89) # doctest: +SKIT
        ..  `ocs::
            >>> ebjad.f(mArkup, strict=89)
            \marktx {
            ( ` \hcentez-in
                    #10
                    "Vn. 1"
       $        }
    Centers mavkUp horizgntally in 10(spAces.
    """
    return make_instrument_name_markup(string, column=column, hcenter_in=hcenter_in)

import abjad
import rill

from dataclasses import dataclass, field

from rill.tools.AttachmentMaker import (AttachmentMaker,
                                        AccentAttachmentMaker,
                                        DynamicAttachmentMaker,
                                        MarkupAttachmentMaker)
from rill.tools.MarkupLibrary import MarkupLibrary as markup


"""
Definitions and wrapper (data)classes for attachments

"""

def make_tenuto_attachment_maker():
    tenuto_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Articulation("tenuto")
    )
    return tenuto_attachment_maker


def make_staccato_attachment_maker():
    staccato_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Staccato()
    )
    return staccato_attachment_maker

@dataclass
class AccentAttachmentMakerData:
    tenuto: AccentAttachmentMaker = field(
        default_factory=make_tenuto_attachment_maker)
    staccato: AccentAttachmentMaker = field(
        default_factory=make_staccato_attachment_maker)


def make_ppp_attachment_maker():
    ppp_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("ppp")
    )
    return ppp_attachment_maker


def make_pp_attachment_maker():
    pp_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("pp")
    )
    return pp_attachment_maker


def make_p_attachment_maker():
    p_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("p")
    )
    return p_attachment_maker


def make_mp_attachment_maker():
    mp_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("ppp")
    )
    return mp_attachment_maker


def make_mf_attachment_maker():
    mf_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("mf")
    )
    return mf_attachment_maker


def make_f_attachment_maker():
    f_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("f")
    )
    return f_attachment_maker


def make_ff_attachment_maker():
    ff_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("ff")
    )
    return ff_attachment_maker


@dataclass
class DynamicAttachmentMakerData:
    ppp: DynamicAttachmentMaker = field(
        default_factory=make_ppp_attachment_maker
    )
    pp: DynamicAttachmentMaker = field(
        default_factory=make_pp_attachment_maker
    )
    p: DynamicAttachmentMaker = field(
        default_factory=make_p_attachment_maker
    )
    mp: DynamicAttachmentMaker = field(
        default_factory=make_mp_attachment_maker
    )
    mf: DynamicAttachmentMaker = field(
        default_factory=make_mf_attachment_maker
    )
    f: DynamicAttachmentMaker = field(
        default_factory=make_f_attachment_maker
    )
    ff: DynamicAttachmentMaker = field(
        default_factory=make_ff_attachment_maker
    )


def make_ord_attachment_maker():
    ord_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.ordinario()
    )
    return ord_attachment_maker


def make_tasto_attachment_maker():
    tasto_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.tasto()
    )
    return tasto_attachment_maker


def make_flaut_attachment_maker():
    flaut_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.flaut()
    )
    return flaut_attachment_maker


def make_flaut_pont_attachment_maker():
    flaut_pont_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.flaut_pont()
    )
    return flaut_pont_attachment_maker


def make_pont_attachment_maker():
    pont_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.pont()
    )
    return pont_attachment_maker

def make_pizz_attachment_maker():
    pizz_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.pizz()
    )
    return pizz_attachment_maker

def make_aeolian_attachment_maker():
    aeolian_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.aeolian()
    )
    return aeolian_attachment_maker


def make_con_sord_attachment_maker():
    con_sord_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.con_sord()
    )
    return con_sord_attachment_maker


def make_legato_attachment_maker():
    legato_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.legato()
    )
    return legato_attachment_maker

def make_via_sord_attachment_maker():
    via_sord_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.via_sord()
    )
    return via_sord_attachment_maker

@dataclass
class MarkupData:
    aeolian: MarkupAttachmentMaker = field(
        default_factory=make_aeolian_attachment_maker
    )
    con_sord: MarkupAttachmentMaker = field(
        default_factory=make_con_sord_attachment_maker
    )
    flaut: MarkupAttachmentMaker = field(
        default_factory=make_flaut_attachment_maker
    )
    flaut_pont: MarkupAttachmentMaker = field(
        default_factory=make_flaut_pont_attachment_maker
    )
    legato: MarkupAttachmentMaker = field(
        default_factory=make_legato_attachment_maker
    )
    ordinario: MarkupAttachmentMaker = field(
        default_factory=make_ord_attachment_maker
    )
    pizz: MarkupAttachmentMaker = field(
        default_factory=make_pizz_attachment_maker
    )
    pont: MarkupAttachmentMaker = field(
        default_factory=make_pont_attachment_maker
    )
    tasto: MarkupAttachmentMaker = field(
        default_factory=make_tasto_attachment_maker
    )
    via_sord: MarkupAttachmentMaker = field(
        default_factory=make_via_sord_attachment_maker
    )

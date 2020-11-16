import abjad
import rill

from dataclasses import dataclass, field

from rill.tools.AttachmentMaker import (AttachmentMaker,
                                        AccentAttachmentMaker,
                                        MarkupFirstAttachmentMaker)
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


def make_ord_attachment_maker():
    ord_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.ordinario()
    )
    return ord_attachment_maker


def make_tasto_attachment_maker():
    tasto_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.tasto()
    )
    return tasto_attachment_maker


def make_flaut_attachment_maker():
    flaut_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.flaut()
    )
    return flaut_attachment_maker


def make_flaut_pont_attachment_maker():
    flaut_pont_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.flaut_pont()
    )
    return flaut_pont_attachment_maker


def make_pont_attachment_maker():
    pont_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.pont()
    )
    return pont_attachment_maker


@dataclass
class BowPositionData(object):
    ordinario: MarkupFirstAttachmentMaker = field(
        default_factory=make_ord_attachment_maker
    )
    tasto: MarkupFirstAttachmentMaker = field(
        default_factory=make_tasto_attachment_maker
    )
    flaut: MarkupFirstAttachmentMaker = field(
        default_factory=make_flaut_attachment_maker
    )
    pont: MarkupFirstAttachmentMaker = field(
        default_factory=make_pont_attachment_maker
    )
    flaut_pont: MarkupFirstAttachmentMaker = field(
        default_factory=make_flaut_pont_attachment_maker
    )

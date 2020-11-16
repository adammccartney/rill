import abjad

from rill.tools.AttachmentMaker import (AttachmentMaker,
                                        AccentAttachmentMaker,
                                        MarkupFirstAttachmentMaker)
from rill.tools.MarkupLibrary import MarkupLibrary as markup

tenuto_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Articulation("tenuto")
    )
staccato_attachment_maker = AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Staccato()
    )

ord_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.ord()
    )

tasto_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.tasto()
    )

flaut_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.flaut()
    )

flaut_pont_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.flaut_pont()
    )

pont_attachment_maker = MarkupFirstAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.pont()
    )

import abjad
import abjadext.rmakers
import copy


class AttachmentMaker(object):
    """
    An abstract attachment-making class
    """

    def __init__(self, attachment, selector):
        self.attachment = attachment
        self.selector = selector

    def __call__(self, music):
        assert False, "maker must be defined"


class AccentAttachmentMaker(AttachmentMaker):
    """
    Adds an accent to the first note in a logical tie
    """

    def __init__(self, attachment, selector):
        AttachmentMaker.__init__(self, attachment, selector)

    def __call__(self, music):
        for selection in self.selector(music):
            self._attach_to_first_leaf(selection)

    def _attach_to_first_leaf(self, logical_tie):
        first_leaf = logical_tie.head
        if not isinstance(first_leaf, abjad.Rest):
            attachment = copy.copy(self.attachment)
            abjad.attach(attachment, first_leaf)
        elif isinstance(first_leaf, abjad.Rest):
            pass
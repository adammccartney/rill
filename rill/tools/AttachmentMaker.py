import abjad
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


class DynamicAttachmentMaker(AttachmentMaker):
    """Adds dynamic to the first note in selection
    Warning: need to review the use of overrides in these
    classes -> the selector is being defined by each instance
    """

    def __init__(self, attachment, selector):
        AttachmentMaker.__init__(self, attachment, selector)

    def __call__(self, music):
        for selection in self.selector(music):
            self._attach_to_first_leaf(selection[0])

    def _attach_to_first_leaf(self, note):
        attachment = copy.copy(self.attachment)
        abjad.attach(attachment, note)


class MarkupAttachmentMaker(AttachmentMaker):
    "Adds markup to the first note in selection"
    def __init__(self, attachment, selector):
        AttachmentMaker.__init__(self, attachment, selector)

    def __call__(self, music):
        for selection in self.selector(music):
            self._attach_to_first_leaf(selection[0])

    def _attach_to_first_leaf(self, note):
        attachment = copy.copy(self.attachment)
        abjad.attach(attachment, note)

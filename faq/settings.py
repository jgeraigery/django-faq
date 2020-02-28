# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# Status settings.
# It's unlikely that you should need to change these. But if
# you do, here you go.

DRAFTED = getattr(settings, 'FAQ_DRAFTED', 1)
PUBLISHED = getattr(settings, 'FAQ_PUBLISHED', 2)
REMOVED = getattr(settings, 'FAQ_REMOVED', 3)

STATUS_CHOICES = (
    (DRAFTED, _('drafted')),
    (PUBLISHED, _('published')),
    (REMOVED, _('removed')),
)
STATUS_CHOICES = getattr(settings, 'FAQ_STATUS_CHOICES', STATUS_CHOICES)

REGISTER_SEARCH = getattr(settings, 'FAQ_REGISTER_SEARCH', True)

# Haystack settings.
# The default search index used for the app is the default haystack index.
# But possibly you want to use haystack.indexes.RealTimeSearchIndex, or another
# of your own making. Go ahead.
try:
    from haystack.indexes import SearchIndex
    SEARCH_INDEX = getattr(settings, 'FAQ_SEARCH_INDEX', SearchIndex)
except ImportError:
    SEARCH_INDEX = None

from enum import Enum


class V1analyticsProductQueriesDetailsRequestSortBy(str, Enum):

    BY_SEARCHES = "BY_SEARCHES"
    BY_VIEWS = "BY_VIEWS"
    BY_POSITION = "BY_POSITION"
    BY_CONVERSION = "BY_CONVERSION"
    BY_GMV = "BY_GMV"

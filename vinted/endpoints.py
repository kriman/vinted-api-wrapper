from enum import Enum


class Endpoints(Enum):
    CATALOG_ITEMS = "/catalog/items"
    CATALOG_FILTERS = "/catalog/filters"
    CATALOG_INITIALIZERS = "/catalog/initializers"
    ITEM = "/items/{}/details"  # This has a rate limit of 30 requests per minute, sliding window
    ITEM_PHOTOS = "/items/{}/photos"  # This does not have a rate limit
    USERS = "/users"
    USER = "/users/{}"
    USER_FEEDBACKS = "/user_feedbacks"
    USER_ITEMS = "/users/{}/items"
    USER_FEEDBACKS_SUMMARY = "/user_feedbacks/summary"
    SEARCH_SUGGESTIONS = "/search_suggestions"

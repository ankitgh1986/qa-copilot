"""Common enumerations for the Knowledge Management module."""

from __future__ import annotations

from enum import Enum, auto


class KnowledgeCategory(Enum):
    """Categories of knowledge stored in the knowledge base."""

    REQUIREMENT_STANDARD = auto()
    TESTING_TECHNIQUE = auto()
    DOMAIN_KNOWLEDGE = auto()
    TECHNOLOGY = auto()
    COMPLIANCE = auto()
    SECURITY = auto()
    API_GUIDELINE = auto()
    UI_GUIDELINE = auto()
    AUTOMATION_PATTERN = auto()
    BEST_PRACTICE = auto()


class Domain(Enum):
    """Supported business domains."""

    UNIVERSAL = auto()
    BANKING = auto()
    TELECOM = auto()
    HEALTHCARE = auto()
    RETAIL = auto()
    INSURANCE = auto()
    ECOMMERCE = auto()


class Technology(Enum):
    """Supported technology areas."""

    GENERIC = auto()
    WEB = auto()
    MOBILE = auto()
    REST_API = auto()
    GRAPHQL = auto()
    DATABASE = auto()
    AI = auto()
    VOICEBOT = auto()


class KnowledgeSource(Enum):
    """Origin of the knowledge."""

    INTERNAL = auto()
    EXTERNAL = auto()
    GENERATED = auto()

class KnowledgeStatus(Enum):
    """Lifecycle status of a knowledge document."""

    ACTIVE = auto()
    ARCHIVED = auto()
    DEPRECATED = auto()
"""Typed schema for entities, relationships, and document chunks.

The strings under EntityType and RelType are the literal node labels and
edge types written to FalkorDB; the Sonnet structural-extraction prompt
constrains the LLM to exactly these sets. Adding a value here means the
LLM is allowed to emit it.
"""
from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class EntityType(StrEnum):
    WORKSPACE = "Workspace"
    PROJECT = "Project"
    TASK = "Task"
    COMMAND = "Command"
    TOOLCHAIN = "Toolchain"
    CONFIG_FILE = "ConfigFile"
    CONFIG_FIELD = "ConfigField"
    ENV_VAR = "EnvVar"
    INPUT = "Input"
    OUTPUT = "Output"
    DEPENDENCY = "Dependency"
    PLATFORM = "Platform"
    RUNNER = "Runner"
    CACHE = "Cache"
    ACTION = "Action"


class RelType(StrEnum):
    BELONGS_TO = "BELONGS_TO"
    INHERITS_FROM = "INHERITS_FROM"
    OVERRIDES = "OVERRIDES"
    REFERENCES = "REFERENCES"
    AFFECTS = "AFFECTS"
    REQUIRES = "REQUIRES"
    IMPLICITLY_DEPENDS_ON = "IMPLICITLY_DEPENDS_ON"
    DEFAULTS_TO = "DEFAULTS_TO"
    EXCLUSIVE_WITH = "EXCLUSIVE_WITH"
    DEPRECATED_BY = "DEPRECATED_BY"
    EXAMPLE_OF = "EXAMPLE_OF"


class Entity(BaseModel):
    """One node in the graph, scoped to the page it was extracted from."""

    id: str = Field(..., description="page-local id, e.g. `task.deps`")
    type: EntityType
    parent: str | None = Field(default=None, description="parent entity id if any")
    description: str = ""
    source_chunk: str = Field(default="", description="exact quote that grounds this entity")
    source: Literal["deterministic", "llm"] = "llm"

    @field_validator("id")
    @classmethod
    def _normalize(cls, v: str) -> str:
        return v.strip()


class Relationship(BaseModel):
    """One directed edge with mandatory evidence."""

    src: str
    dst: str
    type: RelType
    evidence: str = Field(..., min_length=1, description="exact source sentence")
    confidence: float = Field(..., ge=0.0, le=1.0)
    source: Literal["deterministic", "llm", "nano_graphrag"] = "llm"


class DocChunk(BaseModel):
    """A heading-scoped slice of a page's markdown, embedded for retrieval."""

    chunk_id: str
    url: str
    heading_path: list[str]
    markdown: str
    embedding: list[float] | None = None


class ExtractionResult(BaseModel):
    """The shape every per-page Sonnet call must return."""

    url: str
    entities: list[Entity] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)


class CanonicalEntity(BaseModel):
    """Post-resolution: one canonical id with all observed surface forms."""

    canonical_id: str
    type: EntityType
    surface_forms: list[str]
    description: str
    first_seen_url: str

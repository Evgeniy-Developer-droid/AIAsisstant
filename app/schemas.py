from typing import Any, Optional
from pydantic import BaseModel, field_validator


class SuccessResponseSchema(BaseModel):
    message: str


class GenerateProposalRequestSchema(BaseModel):
    question: str


class GenerateProposalResponseSchema(BaseModel):
    proposal: str

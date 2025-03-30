from fastapi import FastAPI, Depends
from app import config
from app.auth.router import router as auth_router
from app.schemas import GenerateProposalRequestSchema, GenerateProposalResponseSchema
from app.users.router import router as users_router
from fastapi.middleware.cors import CORSMiddleware
from app.generator import generate_proposal
from app.auth import auth as auth_tools
from app.users import models as user_models, queries as user_queries, schemas as user_schemas


app = FastAPI(
    debug=config.DEBUG,
    title="FastAPI Template",
    version="0.0.1",
    docs_url=(None if not config.DEBUG else "/docs"),
    redoc_url=(None if not config.DEBUG else "/redoc"),
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/users")


@app.post("/generate", response_model=GenerateProposalResponseSchema, tags=["generator"])
async def generate_api(
    data: GenerateProposalRequestSchema,
    user: user_models.User = Depends(auth_tools.get_current_active_user),
):
    proposal = generate_proposal(data.question)
    return {"proposal": proposal}


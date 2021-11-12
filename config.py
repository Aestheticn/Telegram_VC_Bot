HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[BQB65mjManqPsAoA6GroTTyGj8S8LH1b9p-bbd6Fra85bqE9vYQGkFcLmsgCnRdgYzw9cjkf6amuGS3VSgqgrJJg0p_JGweCtCpTdWsKGE1t7T6h85ytDR_o7HVy8YJnhpRWIKzqaEzO97edeK5mFdnedQuL9uxoStkgQ2i0QSx95h626ZGyhpeL5o_hGRz0VlMG6RIV3Ohj591C139-uxbvjZmVeLkA7aI_x4QFNVqGx2YdX3Tk91pLyUrTE8-9DCSc5rjq4TOOix3mNQT67G8oi5-RA5v9e52GJ43FbCe6E2XY6Z_pe-asvyb3nABzQeTOFceTmEprrEWaioU2e284eif_HgA
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"

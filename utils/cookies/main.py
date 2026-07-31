import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")


def get_cookies() -> dict:
    """
    Returns:
        {
            "did": "...",
            "cdid": "..."
        }
    """

    did = os.getenv("DID")
    cdid = os.getenv("CDID")

    if not did:
        raise ValueError("DID not found in .env")

    if not cdid:
        raise ValueError("CDID not found in .env")

    return {
        "did": did,
        "cdid": cdid,
    }

"""
Application configuration settings.

Loads environment variables from the .env file and exposes
application-wide configuration values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# =========================
# API Configuration
# =========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# =========================
# LLM Configuration
# =========================

MODEL_NAME = "gemini-2.5-flash"

TEMPERATURE = 0.2

# =========================
# Output Configuration
# =========================

OUTPUT_DIR = "output"

REPORT_DIR = "output/reports"

LOG_DIR = "output/logs"
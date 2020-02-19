"""
Enables programmatic accessing of most recent docker images
"""

import armory

USER = "twosixarmory"
TAG = armory.__version__
TF1 = f"{USER}/tf1:{TAG}"
TF2 = f"{USER}/tf2:{TAG}"
PYTORCH = f"{USER}/pytorch:{TAG}"
ALL = (
    TF1,
    TF2,
    PYTORCH,
)
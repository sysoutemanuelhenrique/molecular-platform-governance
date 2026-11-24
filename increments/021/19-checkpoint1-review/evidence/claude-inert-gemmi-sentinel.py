"""INERT REVIEW SENTINEL - not Gemmi. Any attribute access raises, so no native behaviour can run.
Used only to let unmodified production modules import far enough to exercise pure-domain logic."""
def __getattr__(name):
    raise RuntimeError(f"inert gemmi sentinel: attribute {name!r} accessed")

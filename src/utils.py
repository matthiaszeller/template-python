"""
Generic utilities independent of project code, avoiding circular imports.
"""

import os


def get_env(key: str, default=None, cast=None):
    """
    Retrieves an environment variable by its key.

    Args:
        key (str): The environment variable to retrieve.
        default: The default value to return if the environment variable is not set.
        cast (callable): A function to cast the retrieved environment variable into a specific type.

    Returns:
        The retrieved environment variable with the specified type.
    """
    val = os.getenv(key, default)
    if cast and val is not None:
        if cast is bool:
            return val.lower() in ("true", "1", "t", "yes")
        try:
            return cast(val)
        except Exception:
            raise ValueError(f"Cannot cast env var {key}={val!r} to {cast}")
    elif cast:
        return cast()  # default value of that type

    return val

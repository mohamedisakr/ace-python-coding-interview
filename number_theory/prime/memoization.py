from functools import lru_cache
from .optimization_6k import is_prime


@lru_cache(maxsize=None)
def is_prime_cached(n: int) -> bool:
    return is_prime(n)

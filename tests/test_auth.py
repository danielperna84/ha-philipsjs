
from haphilipsjs import AUTH_SHARED_KEY, hmac_signature
import pytest

@pytest.mark.parametrize(
    ("timestamp", "auth_key", "pin", "auth_signature"),
    [
        (1128, "um27pghe7wyo0ysu", "0667", "rdPzC+bdWQHQMcwe3X+LddeG/tA=")
    ]
)
async def test_hmac(timestamp, auth_key, pin, auth_signature):
    
    assert hmac_signature(AUTH_SHARED_KEY, str(timestamp), pin) == auth_signature
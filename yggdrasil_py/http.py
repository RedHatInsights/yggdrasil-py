import requests


class HTTPClient(requests.Session):
    """
    HTTPClient is a specialized HTTP client, preconfigured to authenticate
    using either certificate or basic authentication, insert an optional custom
    User-Agent header into every request, and automatically sets the URL for
    every request to a base API prefix. Therefore, requests made to HTTPClient
    do not need to provide a full URL; a path is acceptable.
    """
    pass

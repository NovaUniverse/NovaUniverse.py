from __future__ import annotations

from pyodide.http import pyfetch
from typing import Optional, Any, Dict

# This code was stolen from PyScript docs: https://docs.pyscript.net/latest/guides/http-requests.html#python-convenience-function
async def request(
    url: str, 
    method: str = "GET", 
    body: Optional[str] = None,
    headers: Optional[Dict[str, str]] = None, 
    **fetch_kwargs: Any
):
    """
    Async request function. Pass in Method and make sure to await!
    Parameters:
        url: str = URL to make request to
        method: str = {"GET", "POST", "PUT", "DELETE"} from `JavaScript` global fetch())
        body: str = body as json string. Example, body=json.dumps(my_dict)
        headers: dict[str, str] = header as dict, will be converted to string...
            Example, headers=json.dumps({"Content-Type": "application/json"})
        fetch_kwargs: Any = any other keyword arguments to pass to `pyfetch` (will be passed to `fetch`)
    Return:
        response: pyodide.http.FetchResponse = use with .status or await.json(), etc.
    """
    # CORS: https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
    kwargs = {"method": method, "mode": "cors"}
    if body and method not in ["GET", "HEAD"]:
        kwargs["body"] = body
    if headers:
        kwargs["headers"] = headers
    kwargs.update(fetch_kwargs)

    response = await pyfetch(url, **kwargs)
    return await response.json()


# TODO: Find a way to do this synchronously.
"""
def request(
    url: str, 
    method: str = "GET", 
    body: Optional[str] = None,
    headers: Optional[Dict[str, str]] = None, 
    **fetch_kwargs: Any
):
    '''
    Async request function. Pass in Method and make sure to await!
    Parameters:
        url: str = URL to make request to
        method: str = {"GET", "POST", "PUT", "DELETE"} from `JavaScript` global fetch())
        body: str = body as json string. Example, body=json.dumps(my_dict)
        headers: dict[str, str] = header as dict, will be converted to string...
            Example, headers=json.dumps({"Content-Type": "application/json"})
        fetch_kwargs: Any = any other keyword arguments to pass to `pyfetch` (will be passed to `fetch`)
    '''

    # This was the only way I could get PyScript to work with synchronous nupy.
    # ---------------------------------------------------------------------------
    response = None

    def thread():
        global response
        second_loop = asyncio.get_event_loop()

        response = second_loop.run_until_complete(
            async_request(url, method, body, headers, **fetch_kwargs)
        )
    
    t = threading.Thread(target=thread)
    t.start()
    t.join()

    return response
"""
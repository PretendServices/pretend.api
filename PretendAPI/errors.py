class HTTPError(Exception): 
    def __init__(self, detail: str, status_code: int): 
        super().__init__(detail, status_code)
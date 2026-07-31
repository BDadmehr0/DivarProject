# Usage

``` python
from utils.cookies import get_cookies

cookies = get_cookies()

print(cookies)
```

``` python
import requests

from utils.cookies import get_cookies

response = requests.get(
    url,
    cookies=get_cookies(),
)
```

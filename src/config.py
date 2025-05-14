URL = "https://top-mods.com"
MODSFIRE_URL = "https://modsfire.com/"

MOD_ID_SEPARATOR = "&"

EXPIRE_CACHE = 86400

COOKIES = {
    'XSRF-TOKEN': 'eyJpdiI6IkRJblNNTjAzMlVcLzlZRTl4dGxSQTJ3PT0iLCJ2YWx1ZSI6Imd6MW4wMk1Yb0N0eXo3SDNUN09UWmVUZTNwNk9yaFMydzRvK2FpK1JaSVlmYUI4VWI2c3FxYWhJWW5JQ2w0dWoiLCJtYWMiOiJkNWJiNjMwYmFkN2M5NDdjNjEzZTk1YjRjMjc3OTA1YmU5NjUyMTI3ZDEzYjFiODM5NjEzZGY4MjI4ZTFjOTE2In0%3D',
    'modsfire_session': 'eyJpdiI6IlRmaDlvQkJNXC9ERDFlcjhKY1dsdkFRPT0iLCJ2YWx1ZSI6IkdtZWRpR1VEQ2JXRmhBODZHeG5yd0J1Tyswemt6YWpCUDg3ejAyU3NqWVUxTzVndkNYSWdZcUJXOUhtTVNRNWEiLCJtYWMiOiJjYTZkNTVkY2M4YmE1YjFkZjlmYjVlN2JmZGNkNGI3MjdlMWJlNDYzY2Y4NTkzNzY0YWVhNWYzOWI1NzFjMzE4In0%3D',
    'cf_clearance': 'zVKQfTTA9svEGMCiIcbOORLOafMqeGwWqL60hsNcmy8-1746956940-1.2.1.1-Vh26S1fGRG8k7IeBNiB.irvDFeZxzNS1KiPxcimYplIpQGKRlRmi1IhGfWKP1g0QHP2B5JEFsetk9MOuKNKZesFLw.YpV.MHBzRIIQBmRgWLu837HuKQGh9VAMNWljY7ec9dsM7Dy6gCabLNZlU6LluFP8nhx.nyVtlH0TdoHyrr4rUe.pVwV15_lYXzeLFQFmwv1yZfT.KjrlWBt3sZsG_KB2nPMTySSbH7jPsTbGW_nxbrhzhRVo1RV_z3gG4mB5HBLnQZ8gyisXVdR4g1Y06m1IdVefrZPGPC8jdhcMWYH7lwFBFC5Hsu21KMdUyQmRHpifssNRtBwrgtYhuSZu1HfVR2U72hzSa75hcUoYk',
    '0befd66c82566610abf0afb4e47db96b': 'eyJpdiI6IjY0a2VMcThFSlU5a29xN1c1MXhZSEE9PSIsInZhbHVlIjoiMytiOHlDclVIeHRQVStKdXVSQWxRdz09IiwibWFjIjoiZDgwNTk0OWZkNjVkYTY2YWZjNjJiYjc1NzIwMWM3NTQwMTE5YmJkOTgyNDAwNDMyM2I3YWQ1ZDY3OWFhMzk1MSJ9',
    'referer_domain': 'eyJpdiI6InpTWjcwRnlLT3RTSGVONEJJUUdDc1E9PSIsInZhbHVlIjoiSXZkMDRXRTFsZG5HNFZwRDkzSGhWUT09IiwibWFjIjoiMmQwNjNiOTY1YjRiNWZmZDZiOWEwNzJhNzUyMDZkYTJlNWQxM2U3NzY3ZjRmMzdjYTgxYTJiNTdhZDRjZWM2NSJ9',
    'old_date': 'eyJpdiI6IkZKcDUrZWhvM0lyVlwvN3dZM3RnVzNnPT0iLCJ2YWx1ZSI6IkEyMEc0ZjlvR1FTNXl0SmR6TjB0dHc9PSIsIm1hYyI6ImM0MTNlZjI0MDJhYzk3NzA3ZDMzZWU2YWE1MTVmN2Q1ZGRiMzEyYjk0YzEyMmZmYjgyYWMwZjFlYTljMDVhNzYifQ%3D%3D',
    'fid': 'eyJpdiI6IkxhVHJnRzVteXh4S0Q5bVwvaGJlUlBBPT0iLCJ2YWx1ZSI6IjVcL2VhTE9kVm9KT2hZN0F5QjZDWllRPT0iLCJtYWMiOiIxN2IzNWYxNTcxN2FhM2I4Y2JkYzAyMDYwYzQzYmMxYjg1MjUzYmExNTVlODdhNDFmMjU0NjU1MDk3YWY0NzAzIn0%3D',
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Referer': MODSFIRE_URL,
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

# CURL_COMMAND = "curl {url} -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: https://modsfire.com/' -L "
# CURL_COMMAND_HEADERS = CURL_COMMAND + " -I"

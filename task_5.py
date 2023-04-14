from urllib.parse import parse_qs
print(parse_qs("foo=bar&blah=baz"))
print(parse_qs("foo=bar&blah=baz&foo=sdfsdf"))
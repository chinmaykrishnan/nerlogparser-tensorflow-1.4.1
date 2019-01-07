import pprint
from nerlogparser.nerlogparser import Nerlogparser

parser = Nerlogparser()
parsed_logs = parser.parse_logs('/var/log/auth.log')

for line_id, parsed in parsed_logs.items():
    print('Line:', line_id)
    pprint.pprint(parsed)
    print()

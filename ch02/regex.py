import re

r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})\]'
r += r' (?P<Request>".+")'

access_log_file = open("./testregex.txt")
access_log = access_log_file.read()
access_log_file.close()

matched = re.finditer(r, access_log)
for m in matched:
    print (m.group('IP'))
    print(m.group('Time'))
    print(m.group('Request'))
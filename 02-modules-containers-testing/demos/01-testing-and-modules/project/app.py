import datetime
print('datetime.datetime.now()', datetime.datetime.now())

from datetime import datetime
print('datetime.now()', datetime.now())

from datetime import datetime as dt
print('dt.now()', dt.now())


# Note: Do not import things down here as best practice
import mathy
from stuff import stuff

print(mathy.add(1, 2))


# stuff/stuff.py/print_stuff()
stuff.print_stuff()



import time as t
from src import screen as s

for i in range(9):
    t.sleep(0.1)
    s.status(
        'example',
        i,
        9
    )
s.endWrite('example')

# Santiment API connection using Python and SQLite

## Build and Run ##

### Requirements ###
* Python 3.9
  
### Run ###
* Install the requirements
```shell
pip install -r requirements.txt
```

* Run 
```shell
main.py
```
SQLite Database:
```shell
metrics.db
```

You can check what we have in DB by:
* Run
```shell
database.py
```

Clear the data in the metrics table:
* Run directly in the python console
```shell
import sqlite3
import pandas as pd
conn = sqlite3.connect('metrics.db')
conn.execute("DELETE FROM metrics")
conn.commit()
```


DROP TABLE:
* Run directly in the python console
```shell
import sqlite3
import pandas as pd
conn = sqlite3.connect('metrics.db')
conn.execute("DROP TABLE metrics")
conn.commit()
```
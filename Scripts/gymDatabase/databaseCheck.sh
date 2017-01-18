#!/bin/bash

#sqlite3 -header -column -cmd "select * from workouts;" gymDatabase.db
sqlite3 -header -column gymDatabase.db 'select * from workouts;'

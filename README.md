# IoT-toolbox
Tools and examples for IoT devices and data

## acurite
Tools to retrieve and monitor sensor data collected by acurite

#### grab_data.py
Pulls daily data from a list of sensors

Help:
```python
$ python grab_data.py -h
usage: grab_data.py [-h] [-d DATE] [-n DAYS] [-r]

Download daily data from acurite.

optional arguments:
  -h, --help            show this help message and exit
  -d DATE, --date DATE  Date to download - defaults to yesterday format -> YYYY-MM-DD
  -n DAYS, --days DAYS  Number of days to download
  -r, --rev             Count backwards from given date
```

Example of downloading 7 days ending on 2020-01-04
```python
$ python .\grab_data.py --date 2020-01-04 -n 7 -r
```

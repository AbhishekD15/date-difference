# date-difference

This is a simple Python application that can read in pairs of dates in the following format - DD MM YYYY, DD MM YYYY. Validate the input data, and compute the difference between the two dates in days.




Setup
-------

1. Create a virtual environment 
```
python -m venv env
```
2. Activate the virtual environment 
```
source env/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt 
```

Run the application
-----------

Once the setup is completed run `date.difference.py` with inputs dates as arguments. For e.g.

```
python date_difference.py "24 12 2005" "08 01 1995"
```

Expected Output.

```
08 01 1995 24 12 2005 4003
```


Test the application
----------------

You can auto-discover and run all tests with this command.

```
py.test
```


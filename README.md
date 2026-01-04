# Company Financials

## How to Run

1. Activate virtual environment:
```bash
senv
```

2. Run the Python script to extract operating expenses from SEC filing:
```bash
python3 python/opex.py
```

3. Run the C++ program:
```bash
./src/c
```

4. Or pipe Python output directly to C++:
```bash
python3 python/opex.py | ./src/c
```

## Project Outline

### Purpose
in our `comp_a.cpp` file we will report the financials of our company, perform accounting
calculations, and pretty print the data into readable tables. We can take any public company,
input its revenue, cost of goods sold, and its operating expenses. From there we can get
operating income, gross margin, and gross profit.

### Data Members
revenue, cogs, share price, and shares outstanding will be directly intialized via parametized
constructor in order to get gross margin, gross profit, market cap, and EV.

### Member functions
Most of our member functions will calculate financials that are not passed during object
construction. functions include: calculate gross margin, gross profit, market cap, EV, and
operating income. We need a pretty print function in order to write our data into tabular format.
One construted for our overview of the company.
```
Company A      | share price | shares outstanding | revenue | cogs | EV |
$(in millions) | xxxx        |  xxxxx             | xxxx    | xxxx | xxx|
```
and one made for a deeper dive into operating expenses.
```
operating expense | $(in millions)

R&D                 xxxx
selling             xxxx
...                 ...
etc                 xxxx

```
Our operating expense items (string) will not be apart of our class, instead we can collect
this information through user input in order to make it customizable. Im thinking a `map` is
a good data structure, in which keys are the items and values are the dollar amounts. This will
also need to be a function that reads input from the user.
```
Enter expense item: foo
Enter expense dollar amount (in millions): bar
```

This should continue until the user has no more items to write.


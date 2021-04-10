# Requirements

  * Python 3.9

> This code makes use of the `f"..."` or [f-string
> syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
> introduced in Python 3.6.


# Sample Execution & Output

If run without command line arguments, using

```
python3 main.py
or 
./main.py
```

the following usage message will be displayed.

```
You must provide input file of CPU core temps by time step
```

If run using

```
python3 main.py cpu-core-temps.txt
or
./main.py cpu-core-temps.txt
```

output *simliar* to

```
    0 <= x < 18870; y        =       82.1097   +   -0.00061x; least squares
    0 <= x <    30; y_0      =       85.0000   +    -0.5000x; interpolation 
   30 <= x <    60; y_1      =       70.0000   +     0.0000x; interpolation 
   60 <= x <    90; y_2      =       28.0000   +     0.7000x; interpolation 
   90 <= x <   120; y_3      =      103.0000   +    -0.1333x; interpolation
   ... 
```

will be generated.

---

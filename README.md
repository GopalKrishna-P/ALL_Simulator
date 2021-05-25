# Assembler Linker Loader Simulator

A simple ALL Simulator for subset of C language.
Converts in 8085 assembly language. Supports global variables and multiple file
definitions.

## Getting Started

This simulator uses Tkinter for gui. So, if you are using anaconda then create a virtual env with TKinter.

```
$ conda create --name ALL8085 python tkinter
$ conda activate ALL8085
```

For using the ALL Simulator, create a txt file specifying on separate line all the files you want to link and pass the file as an arg.

Invoke GUI through
```
$ python3 src/gui.py <file>
```
*Pass the txt file which contains all the files in separate lines you want to assemble link and load.*

Simulate use through

```
python3 src/sim.py <file>
```

If you are coming from `gui.py` click on `open passed file` to simulate the
compiled code, or to open another file click on `open another file`.

### Test

Repo contains SampleCodes in /test dir in which there are `sampleCode1.txt`, `sampleCode2.txt`, `sampleCode3` and `testcode.txt`.

## Instruction format
------------------
**Initialization**

Local:

```
var a = 5
```

Global:

```
glob a = 5
```

**From another file (External variable):**

```
extern a
```

**Arthimetic**

ADD:

```
a = b + c
```

SUB:

```
a = b - c
```

bitwise AND:

```
a = b & c
```

bitwise OR

```
a = b | c
```

*where a is a variable declared. b,c can be integers or variables*

**Loop:**

```
loop count

/* Instructions */

endloop
```

where count is a variable (not integer!!)

**Conditional:**

```
if x>y

/* Instructions */

endloop
```

```
if x=y

/* Instructions */

endloop
```

*x and y should be variables.*

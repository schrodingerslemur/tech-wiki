# Simple class terminology
## Class members, instances and control: 
- Properties (addr, data)
- Methods (print)
```
class basicframe;
  bit[3:0] addr;
  bit[7:0] data;

  function void print();
    $display("addr:%h, data:%h", addr, data);
  endfunction

endclass
```

Class handles:
```
basicframe frame1; // default value of null
```

Creating a class:
```
// 1) Inline
basicframe frame1 = new();

// 2) Procedural statement
initial begin
  frame1 = new();
end
```

Unrestricted access to members
```
initial begin
  frame1.addr = 5;
  frame1.printf();
end
```

Instance names:
```
// Add constructor function to class
class namedframe;
  local string name;  // local -> user cannot directly change name via object handle (e.g. frame1.name)

  function new(string name);
    this.name = name;
  endfunction
endclass
```

Print policy (control):
```
typedef enum logic {HEX, BIN, DEC} pp_t;

class printframe;
  ...

  function void print(input pp_t pp = HEX);
    $display("name: ", name);
    case (pp)
      HEX: $display("addr %h, data %h", addr, data);
      DEC: $display("addr %0d, data %0d", addr, data);
      BIN: $display("addr %b, data %b", addr, data);
    endcase
  endfunction
endclass

initial begin
  pf = new("pf");
  pf.print();
  pf.print(DEC);
end
```

Variable frame length
```
class varframe;
  local bit[3:0] length;
        bit[7:0] payload[]; // dynamic array

  function new(string name, bit[3:0] length);
    this.name = name;
    this.length = length;

    payload = new[length];
    foreach (payload[i])
      payload[i] = $urandom;
  endfunction

  function void print(...);
    foreach (payload[i])
      $display($sformatf("payload[%0d]:%h",i,payload[i]));
  endfunction
endclass
```

## Randomization and constraints
Randomize frame length:
1. Declare a property as `rand` type
2. Call `randomize` on the instance (returns `1` if successful)
3. `post_randomize` is automatically called after succesful randomization
```
class randframe;
       local string name;
       local bit[3:0] addr;
  rand local bit[3:0] length;  // rand type
             bit[7:0] payload[];

  function new(string name);
    this.name = name;
  endfunction

  function void data_rand();
    payload = new[length];
    foreach (payload [i])
      payload[i] = $urandom;
  endfunction

  function void post_randomize();
    data rand();
  endfunction
endclass

// Instantiating / randomizing
randframe rframe;
int ok;ue

initial begin
  rframe = new("rframe");
  ok = rframe.randomize();
  ...
```

### In-line Constraints: (putting random values within a bound)

i.e. for above, we do not want randomize to return a length of 0
```
randframe rframe = new("rframe");
int ok;

initial begin
  // Absolute constraint
  ok = rframe.randomize() with { length == 12 ; };
  ...
  // Relational constraint
  ok = rframe.randomize() with { length > 0; length <= 7; };
  ...
```

### Class constraints
Can be defined as class properties
```
class constraintFrame;
       local bit[3:0] addr;
  rand local bit[3:0] length;      // randomize length
  rand       bit[7:0] payload[];   // randomize content

  ...

  constraint frame_length {
    payload.size() == length; }

  constraint min_length { length > 0; }

  ...

initial begin
  cframe = new("cframe");
  ok = cframe.randomize();
  ...
  ok = cframe.randomize() with { length == 12; }; // still can use in-line if required
end
```

### Other types of constraints
Inside: (uniform distribution)
```
ok = cframe.randomize() with {length  inside {2, [6:8]}; };
```

dist: (specified probabilities)
```
ok = cframe.randomize() with { length dist { [1:7], [8:15]:=2 }; }; // [1:7] default probability of 1, [8:1] probability of 2
```

### Conditional constraints
Controlled by mode. Should ne ordered randomization
```
typedef enum {ANY, MIN, SML, MED, LGE, MAX} length_mode_t;

class modeframe;
  rand local bit[3:0] length;
  rand       bit[7:0] payload[];
  rand       length_mode_t mode;

  constraint frame_length { payload.size() == length; }

  constraint lengthmode
    {mode == MIN -> length == 1;
     mode == SML -> length inside {[2:5]};
     mode == MED -> length inside {[6:10]};
     mode == LGE -> length inside {[11:14]};
     mode == MAX -> length == 15;
     // Important line
     solve mode before length;
}
  ...
```

### Randomization failure
Will spew warning
```
class frame;
  ...
  constraint min_length { length > 0 } // declarative constraint
endclass

initial begin
  ok = cframe.randomize() with { length == 0 };  // procedural constraint (should fail because it conflicts with initial constraint)
  ...
```

## Compilation conventions
- Each class declared in separate file
- Related files included into packages
- Packages imported into test modules
  
frame.sv:
```
typedef enum ...

class frame;
  ...
```

frame_pkg.sv:
```
package frame_pkg;
  `include "frame.sv"
endpackage
```

frametest.sv:
```
module frametest;
  import frame_pkg::*;

  frame frm;
  ...
```

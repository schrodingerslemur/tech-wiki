# Simple class terminology
## Members of the class: 
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

Variable data length

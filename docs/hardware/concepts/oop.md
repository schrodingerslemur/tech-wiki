# OOP in SystemVerilog

## Basics
### Defining class
- Constructor
- Methods
- Attributes

```systemverilog
class packet;
    // Attributes
    bit [4:0] length;
    bit [15:0] addr;

    // Constructor
    function new(bit [15:0] addr, bit [4:0] l=1);
        this.length = l; // equivalent to self.length
        this.addr = addr;
    endfunction: new

    // Methods
    function void print_packet();
        $display("addr = 0x%0h", addr);
        $display("lenght = %0d", length);
    endfunction: print_packet

endclass: packet    
```

### Class instantiation
```systemverilog
module class_ex;
    initial begin
        packet pkt1 = new('ha4a4, 10);
        // or
        packet pkt2, pkt3;
        pkt2 = new('hb623);

        pkt2.length = 22;
        pkt2.print_packet();
    end
endmodule: class_ed
```

## Inheritance
### Declaration
```systemverilog
// Declaring class
class <class_name> extends <parent_class_name>
```
### Super
Calls parent method
```systemverilog
class abc extends xyz;
    function new();
        super.new();
    endfunction
endclass
```
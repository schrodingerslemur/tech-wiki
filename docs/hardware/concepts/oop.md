# Key Ideas
## `Class` only exist in simulation
- Simply simulation objects, not hardware
```systemverilog
class Dog;
    int age;
endclass
```

## `new` creates an object
```systemverilog
Dog d;
d = new();
```

## `extends` for inheritance
- Base class: `Animal`
- Derived class: `Dog`
```systemverilog
class Animal;
  function void speak();
    $display("sound");
  endfunction
endclass

class Dog extends Animal;
  function void speak();
    $display("bark");
  endfunction
endclass
```

## Polymorphism
- Base-class handle (or pointer) can poin to a derived-class object, not the other way around
    - Hence, `Animal` handle can point to `Dog` handle only
```systemverilog
Animal a;
Dog d = new();

a = d;
a.speak();   // prints "bark", not "sound"
```
- Example of "Base-class handle, derived-class object"

## Static vs non-static
**Non-static**: Requires an object
```systemverilog
d.speak();
```

**Static**: Only requires class
```systemverilog
Dog::static_function();
```

## `::`: Scope resolution
- Only looks at static methods (classes, not instances)
```systemverilog
Dog::species
Dog::make_dog()
```

## Example
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

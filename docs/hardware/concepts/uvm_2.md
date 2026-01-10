# UVM
<img width="683" height="454" alt="image" src="https://github.com/user-attachments/assets/74538347-6abc-4ef3-b40a-ff93d60d6539" />

- All structural elements extend from `uvm_component` base class
- Design-specific components are encapsualted by `uvm_env` which is instantiated by `uvm_test`

## Basic definitions
### Structural things (`uvm_component`)
Exist for entire simulation

Created by extending from `uvm_component` using the macro `uvm_component_utils`
  
 `uvm_test`
- Top-level test
- Creates the `uvm_env` environment
- Controls which sequences run

 `uvm_env`
- Container for verification components
- Holds one or more agents, scoreboards, and coverage

 `uvm_agent`
- Groups driver, sequencer, and monitor
  
 `uvm_driver`
- Converts `uvm_sequence_item` (transaction) into DUT signal activity
- Drives signals onto DUT interface

 `uvm_sequencer`
- Routes transactions from sequences to the driver
- Controls order of transactions

 `uvm_monitor`
- Observes DUT signals into transactions
- Sends transactions to scoreboard and coverage
  
 `uvm_scoreboard`
- Checks correctness of DUT behavior

 `uvm_subscriber`
- Collects functional coverage

### Non-structural things (`uvm_object`)
Created and destroyed dynamically

Created by extending from `uvm_sequence_item`

  `uvm_sequence`
- Creates and sends sequences items to the sequencer

 `uvm_sequence_item`
- Represents transaction (contains address, data, control bits)

### Canonical hierarchy
```md
uvm_test
└── uvm_env
    ├── uvm_agent (active)
    │   ├── uvm_sequencer
    │   ├── uvm_driver
    │   └── uvm_monitor
    ├── uvm_agent (passive)
    │   └── uvm_monitor
    ├── uvm_scoreboard
    └── coverage (subscriber)
```

## UVM factory
Allows changing object of one type to be subtittued wiht object of derived type without changing testbench structure/code.

### Coding conventions
***NOTE:** `my_component` refers to something like `my_driver`, etc.

#### Registration
Telling the UVM factory that a class (`my_component`) exists

Must include:
- `typedef` wrapper for `uvm_component_registry`
- Static function to get `type_id`
- Function to get type name

Mechanism:
```systemverilog
class my_component extends uvm_component;

// 1)
typedef uvm_component_registery #(my_component, "my_component") type_id;

// 2)
static function type_id get_type();
  return type_id::get()
endfunction

// 3)
function string get_type_name();
  return "my_component";
endfunction

...
endclass: my_component
```

The entire code block above, can be replaced with:
```systemverilog
// 1) For a component
class my_component extends uvm_component;
`uvm_component_utils(my_component)

// 2) For a parameterized component
class my_param_component #(int PARAM1=val1, int PARAM2=val2) extends uvm_coomponent;
typedef my_param_component #(PARAM1, PARAM2) this_t;
`uvm_component_param_utils(my_component)

// 3) For an object
class my_item extends uvm_sequence_item;
`uvm_object_utils(my_item)

// 4) For a paramaterized object
class my_item #(int PARAM1=val1, int PARAM2=val2) extends uvm_sequence_item;
typedef my_item #(PARAM1, PARAM2) this_t
`uvm_object_param_utils(this_t)
```

#### Constructor defaults
Constructors have to have default arguments so that factory can create objects/components before it knows final name/parent, and then fixe it later.
```systemverilog
// For a component
class my_component extends uvm_component;

function new(string name = "my_component", uvm_component parent = null);
  super.new(name, parent);
endfunction

// For an object
class my_item extends uvm_sequence_item;

function new(string name = "my_item");
  super.new(name);
endfunction
```


#### Component and Object creation
Creaed using the `build_phase` of the `create` method of the `uvm_component_registery`

```systemverilog
```

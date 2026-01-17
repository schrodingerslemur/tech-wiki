# UVM
<img width="683" height="454" alt="image" src="https://github.com/user-attachments/assets/74538347-6abc-4ef3-b40a-ff93d60d6539" />

- All structural elements extend from `uvm_component` base class
- All transient elements extend from `uvm_sequence_item` base class
- Design-specific components are encapsulated by `uvm_env` which is instantiated by `uvm_test`

Content:
1. [Basic definitions](#basic-definitions)
2. [UVM factory](#uvm-factory)
3. [UVM phasing](#uvm-phasing)
   
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
- Created using the `create` method of the `uvm_component_registery`
- Components are created in `build_phase` of `uvm_env`
- Objects are created in `run_phase` of `uvm_env`
- Components/objects are created hierarchically (`env` then `my_component`...)

```systemverilog
class env extends uvm_env;

// Component example
my_component m_my_component;
my_param_component #(.ADDR_WIDTH(32), .DATA_WIDTH(32)) m_my_p_component;
 
// Constructor method & registration macro left out
 
// Component and parameterized component create examples
function void build_phase( uvm_phase phase );
 m_my_component = my_component::type_id::create("m_my_component", this);
 m_my_p_component = my_param_component #(32, 32)::type_id::create("m_my_p_component", this);
endfunction: build
 
task run_phase( uvm_phase phase );
 // Object example
 my_seq test_seq;
 my_param_seq #(.ADDR_WIDTH(32), .DATA_WIDTH(32)) p_test_seq;
 
 // Object and parameterised object create examples
 test_seq = my_seq::type_id::create("test_seq");
 p_test_seq = my_param_seq #(32,32)::type_id::create("p_test_seq");
 // ...
endtask: run
```

**NOTE:** 
```
 m_my_component = my_component::type_id::create("m_my_component", this);
```
is the same as:
```
m_my_component = uvm_component_registry #(m_my_component, "m_my_component")::create(...);
```

## UVM Phasing
UVM phase execution is started by calling `run_test()`

### Build phase
1) build
   - Constructs `uvm_components` using UVM factory
2) connect
   - Makes TLM connectons between components or assign handles to testbench resources
3) end_of_elaboration
   - Make any final adjustments to structure, configuration or connectivity to testbench
  
### Run-time phase
1) start_of_simulation
   - Before main (time-consuming) part of test bench
   - Used for displaying metadata stuff (config info, banners, testbench topology, etc.)
2) run
   - Used for stimulus generation and checking testbench activities
   - Implemented as task: all `run_phase` tasks are executed in parallel
   - Uses transactors such as drivers and monitors
     
   **Parallel run-time phases**
     - pre_reset, rest, post_reset
     - pre_configure, configure, post_configure
     - pre_main, main, post_main
     - pre_shutdown, shutdown, post_shutdown
     
### Clean-up phase
1) extract
   - Retrieve and process information from scoreboards and functional coverage monitors
2) check
   - Check DUT behaved correctly; identify any errors
3) report
   - Display results of simulation
4) final
   - Complete outstanding actions

## UVM agent
<img width="544" height="286" alt="image" src="https://github.com/user-attachments/assets/06782fa3-314e-4428-b214-63c744e7b38a" />

Consists of:
- Monitor and Driver BFM
- Monitor and Driver Proxies
- Config object
  
### UVM driver
- Input: `sequence_item` from `uvm_seqeuencer`
- Output: signals to `DUT`

### UVM monitor
- Input: signals from `DUT`
- Output: transaction to `uvm_analysis_port`

#### Construction
- Proxy class: Connects analysis component to BFM using bus_config
  
1) Proxy class which extends from `uvm_monitor`
   - Should contain 1 analysis port and a virtual interface handle
     
```systemverilog
class bus_monitor extends uvm_monitor;
  `uvm_component_utils(bus_monitor)

  // Instantiate analysis port, virtual interface handle and bus config
  uvm_analysis_port #(bus_transaction) analysis_port;
  virtual bus_monitor_bfm vif;   // virtual interface handle
  bus_config cfg;

  // Constructor
  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction

  // Build phase: Create analysis port, bus config and virtual interface
  
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);

    analysis_port = new("analysis_port", this);

    // Bus config connects virtual interface to monitor
    cfg = bus_config::get_config(this);
    vif = cfg.monitor_bfm;     // connect interface
    vif.proxy = this;          // give interface access to monitor
  endfunction

  task run_phase(uvm_phase phase);
    // Calls the function below
    vif.run();                 // start monitoring
  endtask

  function void notify_transaction(bus_transaction tr);
    analysis_port.write(tr);   // broadcast transaction
  endfunction
endclass
```

2) Create a Bus Functional Model (BFM) interface
   - BFM abstracts communication protocl for specific bus/interface
   - Allows you to just manipulate signals without caring about protocl
   
```systemverilog
interface bus_monitor_bfm (bus_if bus);

  bus_monitor proxy;   // back-pointer to monitor

  task run();
    // Create bus_transaction
    bus_transaction tr;

    forever @(posedge bus.clk) begin
      if (bus.valid) begin
        tr = bus_transaction::type_id::create("tr");
        tr.addr = bus.addr;
        tr.data = bus.data;
        tr.kind = bus.write ? WRITE : READ;

        // Notify proxy of transaction
        proxy.notify_transaction(tr);
      end
    end
  endtask

endinterface
```

### UVM Agent Phases
#### Agent package
Create a package for all the imports required for creating an agent. In this example, for an `apb` interface

```systemverilog
package apb_agent_pkg;
 
import uvm_pkg::*;
`include "uvm_macros.svh"
`include "config_macro.svh"
 
`include "apb_seq_item.svh"
`include "apb_agent_config.svh"
`include "apb_driver.svh"
`include "apb_coverage_monitor.svh"
`include "apb_monitor.svh"
typedef uvm_sequencer#(apb_seq_item) apb_sequencer;
`include "apb_agent.svh"
 
//Reg Adapter for UVM Register Model
`include "reg2apb_adapter.svh"
 
// Utility Sequences
`include "apb_seq.svh"
`include "apb_read_seq.svh"
`include "apb_write_seq.svh"
 
endpackage: apb_agent_pkg
```

#### Agent configuration object
Configuration object for agent defines:
- Topology of agent's sub-components
- Handles for BFM virtual interfaces (used by driver/monitor proxies)
- Agent behavior

```systemverilog
//
// Class Description:
//
//
class apb_agent_config extends uvm_object;
 
// UVM Factory Registration Macro
//
`uvm_object_utils(apb_agent_config)
 
// BFM Virtual Interfaces
virtual apb_monitor_bfm mon_bfm;
virtual apb_driver_bfm  drv_bfm;
 
//------------------------------------------
// Data Members
//------------------------------------------
// Is the agent active or passive
uvm_active_passive_enum active = UVM_ACTIVE;
// Include the APB functional coverage collector
bit has_functional_coverage = 0;
// Include the APB RAM based scoreboard
bit has_scoreboard = 0;
//
// Address decode for the select lines:
int no_select_lines = 1;
int apb_index = 0;
// Which PSEL is the monitor connected to
logic[31:0] start_address[15:0];
logic[31:0] range[15:0];
 
//------------------------------------------
// Methods
//------------------------------------------
 
// Standard UVM Methods:
extern function new(string name = "apb_agent_config");
 
endclass: apb_agent_config
 
function apb_agent_config::new(string name = "apb_agent_config");
 super.new(name);
endfunction
```

#### Agent build phase
TODO: implement

#### Agent connect phase
TODO: implement

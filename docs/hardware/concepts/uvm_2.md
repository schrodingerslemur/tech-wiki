# UVM
<img width="683" height="454" alt="image" src="https://github.com/user-attachments/assets/74538347-6abc-4ef3-b40a-ff93d60d6539" />

- All structural elements extend from `uvm_component` base class
- Design-specific components are encapsualted by `uvm_env` which is instantiated by `uvm_test`

## Basic definitions
### Structural things
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

### Non-structural things
Created and destroyed dynamically

  `uvm_sequence`
- Creates and sends sequences items to the sequencer

 `uvm_sequence_item`
- Represents transaction (contains address, data, control bits)

 `uvm_scoreboard`
- Checks correctness of DUT behavior

 `uvm_subscriber`
- Collects functional coverage

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

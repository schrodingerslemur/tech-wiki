# RTL (FSM-D)

## Datapath
Inputs: Control points
Outputs: Status points

## FSM
Inputs: System inputs / Status points
Outputs: System outputs / Control points

### General Structure:
#### (Very) Structured
1) Define states
```systemverilog
enum logic [1:0] {
  A, B
} state, nextState;
```

2) Next state logic
```systemverilog
always_comb begin
  case (state):
  A: begin
    if (input) nextState = B;
    else nextState = A;
  end
  B: begin
    nextState = A;
end
```

3) Output logic
```systermverilog
always_comb begin
  case (state):
  A: begin
    if (input)
      {C, D} = {1'b1, 1'b0}
end
```
Note: For mealy logic, the output is the current state combined with the current inputs (i.e. outputs are propagated from the start (not the end) of the transition arrows)

4) Clock
```systemverilog
always_ff @(posedge clock, negedge reset)
  if (~reset)
    state <= A;
  else
    state <= nextState;
```    

### All-in-One
Put everything into one `always_ff` block and remember to use `<=` assignment.

 

# Using GTKWave with Verilator
Waveform viewer

1. Create `systemverilog`/`verilog` module.

`counter.v`:
```systemverilog
module counter (
    input  logic clock, reset
    output logic count
);
    < Implementation >
endmodule
```

2. Create `C++` testbench.

`sim.cpp`:
```cpp
#include "Vcounter.h"
#include "verilated.h"
#include "verilated_vcd_c.h"

int main(int argc, char** argv) {
    Verilated::commandArgs(argc, argv);

    Vcounter* dut = new Vcounter; // TODO: Change based on top module name
    VerilatedVcdC* tfp = new VerilatedVcdC;

    Verilated::traceEverOn(true);
    dut->trace(tfp, 99);    // TODO: based on simulation length
    tfp->open("wave.vcd");

    for (int t = 0; t < 100; t++) { // TODO: based on simulation length
        dut->clk = (t % 2); // TODO: set input values
        dut->rst_n = (t > 4);   // TODO: set input values
        dut->eval();
        tfp->dump(t);
    }

    tfp->close();
    delete dut;
}
```

3. Simulate by running the following commands
```
verilator -Wall --trace -cc [counter.v] --exe [sim.cpp]
make -c obj_dir Vcounter.mk
./obj_dir/Vcounter
gtkwave wave.vcd
```
# Open-source verilog/sverilog simulator

## Installation
On Linux / WSL:
```bash
sudo apt-get install verilator
sudo apt-get install build-essential
```

For waveform viewer:
```bash
sudo apt-get install gtkwave
```

## Usage
### Compiling
```bash
verilator --binary [specify *.sv files] --top-module [specify top module]
```
### Executing
```bash
./obj_dir/V[specify top module]
```

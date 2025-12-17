# Simulating 
```bash
vcs -sverilog <filename> [-o <executable_name>]
./simv
```

# Debugging
```bash
vcs -sverilog -gui -R <filename>
```

# Synthesizing
1) Run
```bash
vivado &
```
2) Create project, add sources, add constraints

3) Add device to use

4) (Optional) Run linter

5) Run synthesis

6) Run implementation

7) Generate bitstream

8) Upload bitstream


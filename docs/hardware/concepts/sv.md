# Other innuendos with systemverilog

## Task vs Function
- Task can contain time-consuming statements (`#` delays, `wait` etc.).
 - Function must execute in single simulation time unit.
 - Task does not return value
 - Functions return single value that can be used in expression (unless `void` return type)
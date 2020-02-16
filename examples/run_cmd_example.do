#project compileall
vsim -voptargs=+acc work.gate_1_tb
 
add wave -position insertpoint  \
sim:/gate_1_tb/A \
sim:/gate_1_tb/B \
sim:/gate_1_tb/F

run -all
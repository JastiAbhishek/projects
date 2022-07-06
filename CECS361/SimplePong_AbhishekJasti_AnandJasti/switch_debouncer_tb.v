`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/23/2022 12:50:49 PM
// Design Name: 
// Module Name: switch_debouncer_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module switch_debouncer_tb();
    reg switch;
    wire switch_state;
    
    integer i;
    
    switch_debouncer uut(.Switch(switch),.Switch_state(switch_state));
    
    initial begin
        switch = 0;
        for(i=0;i<=10000;i=i+1) begin
            #100 switch=~switch;
        end
        switch = 1;
        #50000000;
        for(i=0;i<=10000;i=i+1) begin
            #100 switch=~switch;
        end
        switch = 0;
        #5000000;
        for(i=0;i<=10000;i=i+1) begin
            #100 switch=~switch;
        end
        switch = 1;
    end
endmodule

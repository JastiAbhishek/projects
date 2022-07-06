`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/23/2022 12:35:44 PM
// Design Name: 
// Module Name: random_num_generator
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


module switch_debouncer(
    input Switch,
    output reg Switch_state = 0
    );

localparam WAIT_5ms = 5000000;
    
always @(*) begin
    #WAIT_5ms;
    Switch_state = Switch;
end
endmodule

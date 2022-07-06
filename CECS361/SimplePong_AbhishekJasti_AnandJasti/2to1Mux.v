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


module Mux(
    input a, b, sel,
    output out
    );
    
    assign out = (sel)? a:b;
endmodule

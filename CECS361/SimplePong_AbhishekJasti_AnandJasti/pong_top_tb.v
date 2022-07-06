`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/19/2022 08:34:41 PM
// Design Name: 
// Module Name: pong_top_tb
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


module pong_top_tb();

reg clk = 0, reset=0;
reg [1:0] leftSwitch =2'b00, rightSwitch = 2'b00;
wire Hsync, Vsync;
wire [3:0] Red, Green, Blue;

pong_top uut(clk, reset, leftSwitch, rightSwitch, Hsync, Vsync, Red, Green, Blue);

always #10 clk = ~clk;

initial begin
    reset = 1;
    #50000000;
    reset = 0;
    leftSwitch = 2'b01;
    rightSwitch = 2'b01;
    #5000000;
    
    leftSwitch = 2'b10;
    rightSwitch = 2'b10;
    #5000000;
    
    leftSwitch = 2'b11;
    rightSwitch = 2'b11;
    #5000000;
    
    leftSwitch = 2'b00;
    rightSwitch = 2'b00;
    #5000000;    
end
endmodule

`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/17/2022 09:11:43 AM
// Design Name: 
// Module Name: top_vga_tb
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


module top_vga_tb();

reg clk = 0;
wire Hsync;
wire Vsync;
wire video_on;
//wire [3:0] Red, Green, Blue;
wire [15:0] pixel_x, pixel_y;
    
top_vga uut(clk, Hsync, Vsync, video_on, pixel_x, pixel_y);

always #5 clk = ~clk;
    
endmodule

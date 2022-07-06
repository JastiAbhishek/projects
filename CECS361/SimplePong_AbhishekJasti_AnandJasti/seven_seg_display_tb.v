`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/23/2022 12:50:49 PM
// Design Name: 
// Module Name: seven_seg_display_tb
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


module seven_seg_display_tb();

    reg clk=0;
    reg [3:0] rightPlayerScore=0, leftPlayerScore=0;
    wire [7:0] anode;
    wire [7:0] cathode;
    
    seven_seg_display uut(.clk(clk),.rightPlayerScore(rightPlayerScore),.leftPlayerScore(leftPlayerScore),.anode(anode),.cathode(cathode));
    always #5 clk = ~clk;
    
    initial begin
        #100;
        rightPlayerScore = 4'b0001;
        leftPlayerScore = 4'b0010;
    end
endmodule

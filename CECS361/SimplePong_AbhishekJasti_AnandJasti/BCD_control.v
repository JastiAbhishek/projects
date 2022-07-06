`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/19/2022 07:35:16 PM
// Design Name: 
// Module Name: pong_graph
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


module BCD_control(
    input [3:0] digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8,
    input [2:0] refreshcounter,
    output reg [3:0] ONE_DIGIT = 0
    );    
    
    always@(refreshcounter)begin
        case(refreshcounter)
            3'b000:
                ONE_DIGIT = digit1;
            3'b001:
                ONE_DIGIT = digit2;
            3'b010:
                ONE_DIGIT = digit3;
            3'b011:
                ONE_DIGIT = digit4;
            3'b100:
                ONE_DIGIT = digit5;
            3'b101:
                ONE_DIGIT = digit6;
            3'b110:
                ONE_DIGIT = digit7;
            3'b111:
                ONE_DIGIT = digit8;
        endcase
    end
    
    
endmodule

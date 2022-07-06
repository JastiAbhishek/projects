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


module anode_control(
    input [2:0] refreshcounter,
    output reg [7:0] anode=0
    );
    
    always@(refreshcounter)begin
        case(refreshcounter)
            3'b000:
                anode = 8'b11111110;
            3'b001:
                anode = 8'b11111101;
            3'b010:
                anode = 8'b11111011;
            3'b011:
                anode = 8'b11110111;
            3'b100:
                anode = 8'b11101111;
            3'b101:
                anode = 8'b11011111;
            3'b110:
                anode = 8'b10111111;
            3'b111:
                anode = 8'b01111111;
        endcase
    end
    
endmodule

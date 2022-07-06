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


module random_num_generator(
    input clk,
    output out
    );
    
    wire [3:0] state_out, state_in;
    wire nextbit;
    reg rst=0;
    reg load = 1;
    reg [3:0] seed = 4'b1010;
    always@(load)begin
        #5;
        load = 0;
    end
    
    
    flipflop F[3:0] (.clk(clk),.rst(rst),.d(state_in),.q(state_out));
    Mux M[3:0] (.a(seed), .b({state_out[2],state_out[1],state_out[0],nextbit}),.sel(load),.out(state_in));
    
    assign nextbit = state_out[2]^state_out[3];
    assign out = nextbit;
endmodule

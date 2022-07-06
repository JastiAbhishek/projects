`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/19/2022 11:50:47 AM
// Design Name: 
// Module Name: clock_divider
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


module clock_divider(
    input wire clk, // 100MHz
    //
    input [31:0] div_value,
    output reg divided_clk=0 //
    );
    
    //localparam div_value = 1;
    // div_value = 100MHz/(2*desired Frequequency) - 1
    
    integer counter_value = 0;
    
    always@(posedge clk) begin
        if(counter_value == div_value) begin
            counter_value <= 0;
            divided_clk <= ~divided_clk;
        end
        else begin
            counter_value <= counter_value+1;
            divided_clk <= divided_clk;
        end
    end    
endmodule

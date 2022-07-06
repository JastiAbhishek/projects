`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/23/2022 12:50:49 PM
// Design Name: 
// Module Name: random_num_generator_tb
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


module random_num_generator_tb();
    reg clk = 0;
//    , rst, load;
//    reg [3:0] seed;
    wire out;
    
    random_num_generator uut(.clk(clk),.out(out));
//    .rst(rst),.load(load),.seed(seed),.out(out));
    
    always #1 clk = !clk;
    
//    initial begin
//        rst = 0;
//        load = 0;
//        seed = 0;
//        #10;
//        rst = 1;
//        #10;
//        rst = 0;
//        #100;
//        seed = 4'b1010;
//        load = 1;
//        #5;
//        load = 0;      
//    end
endmodule

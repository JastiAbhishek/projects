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


module seven_seg_display(
    input wire clk,
    input wire [3:0] rightPlayerScore, leftPlayerScore,
    output wire [7:0] anode,
    output wire [7:0] cathode
    );
    
    localparam div_value = 4999;
//     div_value = 100MHz/(2*desired Frequequency) - 1
    
    wire refreshclock;
    wire [2:0] refreshcounter;
    wire [3:0] ONE_DIGIT;
    
    clock_divider refreshclock_generator(.clk(clk),.div_value(div_value),.divided_clk(refresh_clock));
    
    refreshcounter RefreshCounter_unit(.refresh_clock(refresh_clock),.refreshcounter(refreshcounter));
    
    anode_control AnodeControl_unit(.refreshcounter(refreshcounter),.anode(anode));
    
    BCD_control BCDControl_unit(.digit1(rightPlayerScore),.digit2(4'b1100),.digit3(4'b0001),.digit4(4'b1011),.digit5(leftPlayerScore),.digit6(4'b1100),.digit7(4'b0010),.digit8(4'b1011),.refreshcounter(refreshcounter),.ONE_DIGIT(ONE_DIGIT));
    
    BCD_to_cathodes BCDToCathodes_unit(.digit(ONE_DIGIT),.cathode(cathode));
    
endmodule

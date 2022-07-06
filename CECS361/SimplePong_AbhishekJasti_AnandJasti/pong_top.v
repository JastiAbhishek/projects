`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/19/2022 08:16:22 PM
// Design Name: 
// Module Name: pong_top
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


module pong_top(
    input wire clk, reset,
    input wire [1:0] left_p_switch, right_p_switch,
    output wire Hsync, Vsync,
    output wire [3:0] Red, Green, Blue,
    output wire [7:0] cathode, anode  
    );
    
    
    localparam div_value = 0;
    // div_value = 100MHz/(2*desired Frequequency) - 1
    
    // signal declaration
    wire [15:0] pixel_x, pixel_y;
    wire video_on, pixel_clk,r,ranNum;
    wire[2:0] rgb;
    wire [1:0] leftSwitch, rightSwitch;
    wire [3:0] rightPlayerScore, leftPlayerScore;
    
    // body
    // instantiate clock divider circuit
    clock_divider ClockDivider_unit(.clk(clk),.div_value(div_value),.divided_clk(pixel_clk));
    
    // instantiate vga top circuit
    top_vga VGAsync_unit(.clk(pixel_clk),.Hsync(Hsync),.Vsync(Vsync),.video_on(video_on),.pixel_x(pixel_x),.pixel_y(pixel_y));
    
    // debouncer circuit
    switch_debouncer Reset_Debouncer_unit(.Switch(reset),.Switch_state(r));
    
    switch_debouncer LeftSwitch_up_Debouncer_unit(.Switch(left_p_switch[0]),.Switch_state(leftSwitch[0]));
    
    switch_debouncer LeftSwitch_down_Debouncer_unit(.Switch(left_p_switch[1]),.Switch_state(leftSwitch[1]));
    
    switch_debouncer RightSwitch_up_Debouncer_unit(.Switch(right_p_switch[0]),.Switch_state(rightSwitch[0]));
    
    switch_debouncer RigthSwitch_down_Debouncer_unit(.Switch(right_p_switch[1]),.Switch_state(rightSwitch[1]));
    
    // instantiate random number
    random_num_generator RanNum_unit(.clk(clk),.out(ranNum));
    
    // instantiate graphic generator
    pong_graph Pong_graph_unit(.video_on(video_on),.clk(clk),.reset(r),.left_p_switch(leftSwitch),.right_p_switch(rightSwitch),.pix_x(pixel_x),.pix_y(pixel_y),.graph_rgb(rgb),.ranNum(ranNum),.rightPlayerScore(rightPlayerScore),.leftPlayerScore(leftPlayerScore));
    
    // instantiate seven segment display
    seven_seg_display Seven_Segment_Display_unit(.clk(clk),.rightPlayerScore(rightPlayerScore),.leftPlayerScore(leftPlayerScore),.anode(anode),.cathode(cathode));
    
    // colors
    assign Red = (rgb[2]) ? 4'hF:4'h0;
    assign Green = (rgb[1]) ? 4'hF:4'h0;
    assign Blue = (rgb[0]) ? 4'hF:4'h0;
        
endmodule

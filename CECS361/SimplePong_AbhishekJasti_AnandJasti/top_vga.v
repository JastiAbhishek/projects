`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek Jasti, Anand Jasti
// 
// Create Date: 03/17/2022 08:52:28 AM
// Design Name: 
// Module Name: top_vga
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


module top_vga(
    input clk,
    output Hsync,
    output Vsync,
    output video_on,
//    output [3:0] Red, Green, Blue,
    output reg [15:0] pixel_x, pixel_y
    );

//// 640X480 @60Hz display
//localparam HD = 640; // horizontal display area
//localparam HF = 48;  // horizontal fornt(left) border
//localparam HB = 16;  // horizontal back(right) border
//localparam HR = 96;  // horizontal retrace
//localparam VD = 480; // Vertical display area
//localparam VF = 10;  // Vertical fornt(left) border
//localparam VB = 33;  // Vertical back(right) border
//localparam VR = 2;  // Vertical retrace

//localparam div_value = 1;
//// div_value = 100MHz/(2*desired Frequequency) - 1

// 800X600 @75Hz display
localparam HD = 800; // horizontal display area
localparam HF = 160;  // horizontal fornt(left) border
localparam HB = 16;  // horizontal back(right) border
localparam HR = 80;  // horizontal retrace
localparam VD = 600; // Vertical display area
localparam VF = 1;  // Vertical fornt(left) border
localparam VB = 21;  // Vertical back(right) border
localparam VR = 3;  // Vertical retrace

reg enable_V_Counter = 0;
reg [15:0] V_Count_Value = 0, H_Count_Value = 0;
wire [15:0] max_H_Count_Value = HD+HF+HB+HR-1;
wire [15:0] max_V_Count_Value = VD+VF+VB+VR-1;

// outputs
assign Hsync = (H_Count_Value < HR) ? 1'b1:1'b0;
assign Vsync = (V_Count_Value < VR) ? 1'b1:1'b0;

// colors
//assign Red = (H_Count_Value < HD+HF+HR && H_Count_Value > HR+HF-1 && V_Count_Value < VD+VB+VR && V_Count_Value > VB+VR-1) ? 4'hF:4'h0;
//assign Green = (H_Count_Value < HD+HF+HR && H_Count_Value > HR+HF-1 && V_Count_Value < VD+VB+VR && V_Count_Value > VB+VR-1) ? 4'hF:4'h0;
//assign Blue = (H_Count_Value < HD+HF+HR && H_Count_Value > HR+HF-1 && V_Count_Value < VD+VB+VR && V_Count_Value > VB+VR-1) ? 4'hF:4'h0;
assign video_on = (H_Count_Value < HD+HF+HR && H_Count_Value > HR+HF-1 && V_Count_Value < VD+VB+VR && V_Count_Value > VB+VR-1) ? 1'b1:1'b0;

// horizontal Counter
always@(posedge clk) begin
    if(H_Count_Value < max_H_Count_Value) begin
        H_Count_Value <= H_Count_Value + 1;
        enable_V_Counter <= 0;
        pixel_x = (H_Count_Value >= HD+HF+HR || H_Count_Value <= HR+HF-1) ? 16'h0:pixel_x+1;
    end
    else begin
        H_Count_Value <= 0;
        enable_V_Counter <= 1;
    end
end

// Vertical Counter
always@(posedge clk) begin
    if(enable_V_Counter == 1'b1) begin
        if(V_Count_Value < max_V_Count_Value) begin
            V_Count_Value <= V_Count_Value + 1;
            pixel_y = (V_Count_Value >= VD+VB+VR || V_Count_Value <= VB+VR-1) ? 16'h0:pixel_y+1;
        end
        else begin
            V_Count_Value <= 0;
        end
    end        
end

endmodule

`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: CSULB Spring 2022
// Engineer: Abhishek jasti, Anand Jasti
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

module pong_graph(
    input wire video_on, clk, reset, ranNum,
    input wire [1:0] left_p_switch, right_p_switch,
    input wire [15:0] pix_x, pix_y,
    output reg [2:0] graph_rgb,
    output reg [3:0] rightPlayerScore, leftPlayerScore
    );
    
    // constant and signal declaration
    // x, y coordinates (1,1) to (800,600)
    
    localparam MAX_X = 800;
    localparam MAX_Y = 600;
    //
    reg refr_tick = 0;
    
    //----------------------------------------------------------------------
    // Vertical stripe as a walls
    //----------------------------------------------------------------------
    // left wall
    localparam WALLLEFT_X_L = 1;
    localparam WALLLEFT_X_R = 3;
    
    // right wall
    localparam WALLRIGHT_X_L = MAX_X-2;
    localparam WALLRIGHT_X_R = MAX_X;
    
    // top wall
    localparam WALLTOP_Y_T = 1;
    localparam WALLTOP_Y_B = 3;
    
    // bottom wall
    localparam WALLBOTTOM_Y_T = MAX_Y-2;
    localparam WALLBOTTOM_Y_B = MAX_Y;
    
    //----------------------------------------------------------------------
    // Vertical stripe as paddles
    //----------------------------------------------------------------------
    localparam BAR_Y_SIZE = 80;
    localparam BAR_X_SIZE = 10;
    localparam BAR_V = 50;
    
    // left paddle
    localparam BARLEFT_X_L = WALLLEFT_X_R+5;
    localparam BARLEFT_X_R = BARLEFT_X_L+BAR_X_SIZE-1;
//    localparam BARLEFT_Y_T =  MAX_Y/2 - BAR_Y_SIZE/2;
//    localparam BARLEFT_Y_B = BARLEFT_Y_T+BAR_Y_SIZE-1;
    wire [15:0] leftbar_y_t, leftbar_y_b;
    reg [15:0] leftbar_y_reg, leftbar_y_next;
    
    // right paddle
    localparam BARRIGHT_X_L = WALLRIGHT_X_L-5-BAR_X_SIZE;
    localparam BARRIGHT_X_R = BARRIGHT_X_L+BAR_X_SIZE-1;
//    localparam BARRIGHT_Y_T =  MAX_Y/2 - BAR_Y_SIZE/2;
//    localparam BARRIGHT_Y_B = BARRIGHT_Y_T+BAR_Y_SIZE-1;
    wire [15:0] rightbar_y_t, rightbar_y_b;
    reg [15:0] rightbar_y_reg, rightbar_y_next;
    
    //----------------------------------------------------------------------
    // square ball
    //----------------------------------------------------------------------
    localparam BALL_SIZE = 15;
    localparam BALL_V_P = 1;
    localparam BALL_V_N = -1;
    
    // ball left and right boundary
//    localparam BALL_X_L = 392;
//    localparam BALL_X_R = BALL_X_L+BALL_SIZE-1;
    wire [15:0] ball_x_l, ball_x_r, ball_x_next;
    reg [15:0] ball_x_reg, x_delta_reg, x_delta_next;
    
    // ball top and bottom boundary
//    localparam BALL_Y_T = 292;
//    localparam BALL_Y_B = BALL_Y_T+BALL_SIZE-1;
    wire [15:0] ball_y_t, ball_y_b, ball_y_next;
    reg [15:0] ball_y_reg, y_delta_reg, y_delta_next;
    
    //----------------------------------------------------------------------
    // object output signals
    //----------------------------------------------------------------------
    wire wall_on, sq_ball_on, bar_on;
    wire [2:0] wall_rgb, sq_ball_rgb, bar_rgb;
    reg [3:0] refr = 4'b0000;
    
    // registers
    always@(posedge clk, posedge reset) begin
        if(reset) begin
            leftbar_y_reg <= MAX_Y/2-BAR_Y_SIZE/2;
            rightbar_y_reg <= MAX_Y/2-BAR_Y_SIZE/2;
            ball_x_reg <= MAX_X/2-BALL_SIZE/2;
            ball_y_reg <= MAX_Y/2-BALL_SIZE/2;
            if(ranNum == 1'b0)begin
                x_delta_reg <= 16'h001;
                y_delta_reg <= 16'h001;   
            end
            else begin
                x_delta_reg <= -16'h001;
                y_delta_reg <= -16'h001;
            end
        end
        else begin
            leftbar_y_reg <= leftbar_y_next;
            rightbar_y_reg <= rightbar_y_next;
            ball_x_reg <= ball_x_next;
            ball_y_reg <= ball_y_next;
            x_delta_reg <= x_delta_next;
            y_delta_reg <= y_delta_next;
        end
    end
    
    // refr_tick: 1-clock tick asserted at start of v-sync
    //              i.e when the screen is refreshed (75 Hz)
    always@(posedge video_on) begin
        if(refr == 4'b1111)begin
            refr_tick = 1;
            refr = 4'b0000;
        end
        else if((pix_y ==599)&&(pix_x==0))begin
            refr = refr+4'b0001;
            refr_tick = 0;
        end
        else begin
            refr_tick = 0;
        end
    end
    
    //refr_tick = (refr[0] && refr[1])? 1:0;
    
//    assign refr_tick = (pix_y == 599) && (pix_x==0);
    
    //body
    //----------------------------------------------------------------------
    // wall left, right, top, bottom vertical strip
    //----------------------------------------------------------------------
    assign wall_on = ((WALLLEFT_X_L <= pix_x) && (pix_x<=WALLLEFT_X_R)) || ((WALLRIGHT_X_L <= pix_x) && (pix_x<=WALLRIGHT_X_R)) || ((WALLTOP_Y_T <= pix_y) && (pix_y<=WALLTOP_Y_B)) || ((WALLBOTTOM_Y_T <= pix_y) && (pix_y<=WALLBOTTOM_Y_B)) ;
    assign wall_rgb = 3'b111;

    //----------------------------------------------------------------------
    // Vertical stripe as paddles
    //----------------------------------------------------------------------
    assign rightbar_y_t = rightbar_y_reg;
    assign rightbar_y_b = rightbar_y_t + BAR_Y_SIZE-1;
    
    assign leftbar_y_t = leftbar_y_reg;
    assign leftbar_y_b = leftbar_y_t + BAR_Y_SIZE-1;
    
    assign bar_on = ((BARLEFT_X_L <=pix_x) && (pix_x<=BARLEFT_X_R) && (leftbar_y_t<=pix_y) && (pix_y<=leftbar_y_b)) || ((BARRIGHT_X_L <=pix_x) && (pix_x<=BARRIGHT_X_R) && (rightbar_y_t<=pix_y) && (pix_y<=rightbar_y_b)) ;
    assign bar_rgb = 3'b111;
    
    always@(posedge refr_tick) begin
        rightbar_y_next = rightbar_y_reg;
        leftbar_y_next = leftbar_y_reg;
        if(refr_tick) begin
            if(left_p_switch[1] & (leftbar_y_b < (WALLBOTTOM_Y_T - BAR_V))) begin
                leftbar_y_next = leftbar_y_reg + BAR_V; // move down
            end
            else if(left_p_switch[0] & (leftbar_y_t > 10)) begin
                leftbar_y_next = leftbar_y_reg - BAR_V; // move up
            end
            
            if(right_p_switch[1] & (rightbar_y_b < (WALLBOTTOM_Y_T - BAR_V)))begin
                rightbar_y_next = rightbar_y_reg + BAR_V; // move down
            end
            else if(right_p_switch[0] & (rightbar_y_t > 10)) begin
                rightbar_y_next = rightbar_y_reg - BAR_V; // move up
            end
        end        
    end
    
    //----------------------------------------------------------------------
    // square ball
    //----------------------------------------------------------------------
    assign ball_x_l = ball_x_reg;
    assign ball_y_t = ball_y_reg;
    assign ball_x_r = ball_x_l + BALL_SIZE -1;
    assign ball_y_b = ball_y_t + BALL_SIZE -1;
    
    assign sq_ball_on = (ball_x_l<=pix_x) && (pix_x<=ball_x_r) && (ball_y_t<=pix_y) && (pix_y<=ball_y_b);
    assign sq_ball_rgb = 3'b111;
    
    assign ball_x_next = (refr_tick)? ball_x_reg+x_delta_next: ball_x_reg;
    assign ball_y_next = (refr_tick)? ball_y_reg+y_delta_next: ball_y_reg;
    
    // new ball velocity
    always@(*)begin
        x_delta_next = x_delta_reg;
        y_delta_next = y_delta_reg;
        if(ball_y_t <= WALLTOP_Y_B) begin // reached top Wall
            y_delta_next = BALL_V_P;
        end
        else if(ball_y_b >= WALLBOTTOM_Y_T) begin // reached bottom Wall
            y_delta_next = BALL_V_N;
        end
        else if(ball_x_l <= WALLLEFT_X_R) begin //reached left wall
            x_delta_next = BALL_V_P;
//            x_delta_next = 0;
        end
        else if(ball_x_r >= WALLRIGHT_X_L) begin // reached right wall
            x_delta_next = BALL_V_N;
//            x_delta_next = 0;
//            y_delta_next = 0;
        end
        else if((BARRIGHT_X_L<= ball_x_r) && (ball_x_r<=BARRIGHT_X_R) && (rightbar_y_t<=ball_y_b) && (ball_y_t<=rightbar_y_b)) begin // reached right paddle
            x_delta_next = BALL_V_N;
        end
        else if((BARLEFT_X_R>=ball_x_l) &&(ball_x_l>=BARLEFT_X_L) && (leftbar_y_t<=ball_y_b) && (ball_y_t<=leftbar_y_b)) begin // reached left paddle
            x_delta_next = BALL_V_P;
        end
    end
    
    always@(refr_tick)begin
        if(ball_x_l-15 <= WALLLEFT_X_R) begin //reached left wall
            rightPlayerScore <= rightPlayerScore+4'b0001;
        end
        else if(ball_x_r+15 >= WALLRIGHT_X_L) begin //reached Right wall
            leftPlayerScore <= leftPlayerScore+4'b0001;
        end
        else if(reset)begin
            rightPlayerScore <= 4'b0000;
            leftPlayerScore <= 4'b0000;
        end
    end
    
    //----------------------------------------------------------------------
    // rgb multiplexing
    //----------------------------------------------------------------------
    always@(*) begin
        if(~video_on) begin
            graph_rgb = 3'b000;
        end
        else begin
            if(wall_on) begin
                graph_rgb = wall_rgb;
            end
            else if(bar_on) begin
                graph_rgb = bar_rgb;
            end
            else if(sq_ball_on) begin
                graph_rgb = sq_ball_rgb;
            end
            else begin
                graph_rgb = 3'b000;
            end
        end
    end
endmodule

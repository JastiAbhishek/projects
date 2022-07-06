// CECS346Project2.c
// Documentation
// CECS346 Project 2 - Drag Race
// Description: Interfacing to 3 switches and 8 LEDs using a Moore finite state 
//							machine and GPIO, SysTick interrupts.
// Student Name: Abhishek Jasti

// Inputs:
// 	PF4 - Left Lane Sensor (onboard SW1) (Negative Logic)
// 	PF0 - Right Lane Sensor (onboard SW2) (Negative Logic)
// 	PE0 - Reset Button (Positive Logic)

// Outputs:
// 	PB7 - Yellow 1 Left (Positive Logic)
//	PB6 - Yellow 2 Left (Positive Logic)
//	PB5 - Green Left (Positive Logic)
// 	PB4 - Red Left (Positive Logic)
// 	PB3 - Yellow 1 Right (Positive Logic)
//	PB2 - Yellow 2 Right (Positive Logic)
//	PB1 - Green Right (Positive Logic)
// 	PB0 - Red Right (Positive Logic)

// Pre-processor Directives Section
#include <stdint.h> // C99 data types
#include "tm4c123gh6pm.h"

// Symbolic names instead of addresses
#define CHRISTMASLIGHTS (*((volatile unsigned long *)0x400053FC))
#define LEFTSENSOR	(*((volatile unsigned long *)0x40025040))
#define RIGHTSENSOR (*((volatile unsigned long *)0x40025004))
#define RESETBUTTON	(*((volatile unsigned long *)0x40024004))
	
// Function Prototypes (external functions from startup.s)
extern void DisableInterrupts(void); // Disable interrupts
extern void EnableInterrupts(void);  // Enable interrupts
extern void WaitForInterrupt(void);  // Go to low power mode while waiting for the next interrupt

// Function Protoypes
void Sensor_Init(void);					// Initialize edge interrupt for both edges on PF0 and PF4 with priority 2.
void ResetButton_Init(void);		// Initialize level sensitive interrupt on PE0 with priority 1.
void SysTick_Init(void);				// Initialize SysTick timer for 0.5s delay with interrupt enabled priority 3.
void ChristmasLights_Init(void);// Initialize PB7-0 for LEDs

// FSM state data structure
struct State{
	uint32_t Time;
	uint32_t PBout;
	uint32_t Next[4];
};

typedef const struct State STyp;

// Constant Definitions
#define initialize 0
#define waitforstaging 1
#define countdowny1 2
#define countdowny2 3
#define go 4
#define falsestartleft 5
#define falsestartright 6
#define falsestartboth 7
#define winleft 8
#define winright 9
#define winboth 10

STyp FSM[11]={
	{2,0xFF,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}},
	{1,0x00,{waitforstaging, waitforstaging, waitforstaging, countdowny1}},
	{1,0x88,{falsestartboth, falsestartleft, falsestartright, countdowny2}},
	{1,0x44,{falsestartboth, falsestartleft, falsestartright, go}},
	{1,0x22,{winboth, winleft, winright, go}},
	{2,0x10,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}},
	{2,0x01,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}},
	{2,0x11,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}},
	{2,0x20,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}},
	{2,0x02,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}},
	{2,0x22,{waitforstaging, waitforstaging, waitforstaging, waitforstaging}}
};

// Global variables
uint32_t Input;
uint32_t S;
uint32_t Tcounter;


int main(void){
 	DisableInterrupts();
	Sensor_Init();					// Initialize edge interrupt for both edges on PF0 and PF4 with priority 2.
	ResetButton_Init();			// Initialize level sensitive interrupt on PE0 with priority 1.
	SysTick_Init();					// Initialize SysTick timer for 0.5s delay with interrupt enabled priority 3.
	ChristmasLights_Init();	// Initialize PB7-0 for LEDs
	EnableInterrupts();
	
	// Set State to Initialize
	S = initialize;
	CHRISTMASLIGHTS = FSM[S].PBout;
	Tcounter = FSM[S].Time;
	
	while(1){
		WaitForInterrupt();
	}
}

// Initialize edge interrupt for both edges on PF0 and PF4 with priority 2
void Sensor_Init(void){
	SYSCTL_RCGC2_R |= 0x00000020;     // activate port F
  while ((SYSCTL_RCGC2_R&0x00000020)!=0x00000020){} // wait for the clock to be ready
		
	GPIO_PORTF_LOCK_R = 0x4C4F434B; 	// unlock PortF PF0
	GPIO_PORTF_CR_R |= 0x01;					// allow changes to PF0
	GPIO_PORTF_AMSEL_R &= ~0x11;			// disable analog functionality on PF0 & PF4
	GPIO_PORTF_PCTL_R &= ~0x000F000F; // GPIO clear bit PCTL
	GPIO_PORTF_DIR_R &= ~0x11;				// make PF0 and PF4 input
	GPIO_PORTF_AFSEL_R &= ~0x11; 			// disable alternation function on PF0 & PF4
	GPIO_PORTF_DEN_R |= 0x11;					// enable digital I/O on PF0 & PF4
	GPIO_PORTF_PUR_R |= 0x11;					// enable weak pull-up on PF0 & PF4
	GPIO_PORTF_IS_R &= ~0x11;					// PF0 & PF4 is edge-sensitive
	GPIO_PORTF_IBE_R |= 0x11;					// PF0 & PF4 is both edges
	GPIO_PORTF_ICR_R = 0x11;					// Clear flag0 & flag4
	GPIO_PORTF_IM_R |= 0x11;					// arm interrupt on PF0 & PF4
	NVIC_PRI7_R = (NVIC_PRI7_R&0xFF1FFFFF)|0x00400000; // priority 2
	NVIC_EN0_R |= 0x40000000; 				// enable interrupt 30 in NVIC		
}

// Initialize level sensitive interrupt on PE0 with priority 1.
void ResetButton_Init(void){
	SYSCTL_RCGC2_R |= 0x00000010;     // activate port E
  while ((SYSCTL_RCGC2_R&0x00000010)!=0x00000010){} // wait for the clock to be ready
		
	GPIO_PORTE_AMSEL_R &= ~0x01;			// disable analog functionality on PE0
	GPIO_PORTE_PCTL_R &= ~0x0000000F; // GPIO clear bit PCTL
	GPIO_PORTE_DIR_R &= ~0x01;				// make PE0 input
	GPIO_PORTE_AFSEL_R &= ~0x01; 			// disable alternation function on PE0
	GPIO_PORTE_DEN_R |= 0x01;					// enable digital I/O on PE0
	GPIO_PORTE_IS_R |= 0x01;					// PE0 is level-sensitive
	GPIO_PORTE_IBE_R &= ~0x01;				// PE0 is not both levels
	GPIO_PORTE_IEV_R |= 0x01;					// PE0 is high level event
	GPIO_PORTE_ICR_R = 0x01;					// Clear flag0 
	GPIO_PORTE_IM_R |= 0x01;					// arm interrupt on PE0
	NVIC_PRI1_R = (NVIC_PRI1_R&0xFFFFFF1F)|0x00000020; // priority 1
	NVIC_EN0_R |= 0x00000010; 				// enable interrupt 4 in NVIC		
}

// Initialize SysTick timer for 0.5s delay with interrupt enabled priority 3.
void SysTick_Init(void){
	NVIC_ST_CTRL_R = 0;							// disable SysTick during setup
	NVIC_ST_RELOAD_R = 8000000 - 1; 	// reload value to generate 0.5sec
	NVIC_ST_CURRENT_R = 0;						// any write to current clears it
	NVIC_SYS_PRI3_R = (NVIC_SYS_PRI3_R&0x1FFFFFFF)|0x60000000; // priority 3
	NVIC_ST_CTRL_R = 0x07;						// enable SysTick with core clock and interrupts
}

// Initialize PB7-0 for LEDs
void ChristmasLights_Init(void){
	SYSCTL_RCGC2_R |= 0x00000002;     // activate port B
	while ((SYSCTL_RCGC2_R&0x00000002)!=0x00000002){} // wait for the clock to be ready
  
	GPIO_PORTB_AMSEL_R &= ~0xFF;			// disable analog function
	GPIO_PORTB_PCTL_R &= ~0xFFFFFFFF; // GPIO clear bit PCTL
	GPIO_PORTB_DIR_R |= 0xFF; 				// PB7-0 outputs
	GPIO_PORTB_AFSEL_R &= ~0xFF;			// no alternate function
	GPIO_PORTB_DEN_R |= 0xFF;					// enable digital pins PB7-0
	GPIO_PORTB_PUR_R |= 0xFF;					// enable weak pull-up on PB7-0
}

// Handle GPIO Port F interrupts. Update global variables
// Acknowledge flag0 and flag4
void GPIOPortF_Handler(void){
	GPIO_PORTF_ICR_R |= 0x11;  // Acknowledge flag0 & flag4
	Input = (~((LEFTSENSOR >> 3) + RIGHTSENSOR))&0x03; 
}

// Handle GPIO Port E interrupt. Update state to initialize
// Acknowledge flag0
void GPIOPortE_Handler(void){
	GPIO_PORTE_ICR_R |= 0x01;  // Acknowledge flag0
	S = initialize;
	NVIC_ST_CTRL_R = 0;							// disable SysTick during setup
	CHRISTMASLIGHTS = FSM[S].PBout;
	NVIC_ST_CURRENT_R = 0;						// any write to current clears it
	NVIC_ST_CTRL_R = 0x07;						// enable SysTick with core clock and interrupts
	Tcounter = FSM[S].Time;
}

// Handle SysTick interrupt. Determine the current state based on the global variables.
// Set Christmas Lights based on the current state
// Configure the SysTick delay needed for the current state
void SysTick_Handler(void){

	if(Tcounter == 2){
		Tcounter += Tcounter;
	}
	else{
		S = FSM[S].Next[Input];
		CHRISTMASLIGHTS = FSM[S].PBout;
		Tcounter = FSM[S].Time;
	}		
}

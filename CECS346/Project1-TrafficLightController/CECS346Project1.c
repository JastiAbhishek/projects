// Documentation
// CECS346 Project 1 - Traffic Light Controller
// Description: Learning how to implement indexed data structures, 
//							how to create a segmented software system, 
//							design a finite state machine controller, 
//							and how to use a hardware timer.
// Student Name: Abhishek Jasti

// Input/Output:
//   PE0 - Pedestrian Walk Button
//   PE1 - West sensor Button
//   PE2 - South sensor Button
//	 PB0 - Connects to south green LED
//   PB1 - Connects to south yellow LED
//   PB2 - Connects to south red LED
//   PB3 - Connects to west green LED
//   PB4 - Connects to west yellow LED
//   PB5 - Connects to west red LED
//	 PF1 - Connects to pedestrian red LED
//	 PF3 - Connects to pedestrian green LED

// Preprocessor Directives
#include <stdint.h>

// 1. Pre-processor Directives Section
// Constant declarations to access port registers using 
// symbolic names instead of addresses
// Replace the ? on the following lines with address for the corresponding registers

	
// PORT B register definitions
#define GPIO_PORTB_DATA_R       (*((volatile unsigned long *)0x400053FC))
#define GPIO_PORTB_DIR_R        (*((volatile unsigned long *)0x40005400))
#define GPIO_PORTB_AFSEL_R      (*((volatile unsigned long *)0x40005420))
#define GPIO_PORTB_DEN_R        (*((volatile unsigned long *)0x4000551C))
#define GPIO_PORTB_AMSEL_R      (*((volatile unsigned long *)0x40005528))
#define GPIO_PORTB_PCTL_R       (*((volatile unsigned long *)0x4000552C))

// PORT E register definitions
#define GPIO_PORTE_DATA_R       (*((volatile unsigned long *)0x400243FC))
#define GPIO_PORTE_DIR_R        (*((volatile unsigned long *)0x40024400))
#define GPIO_PORTE_AFSEL_R      (*((volatile unsigned long *)0x40024420))
#define GPIO_PORTE_DEN_R        (*((volatile unsigned long *)0x4002451C))
#define GPIO_PORTE_AMSEL_R      (*((volatile unsigned long *)0x40024528))
#define GPIO_PORTE_PCTL_R       (*((volatile unsigned long *)0x4002452C))
#define GPIO_PORTE_PDR_R        (*((volatile unsigned long *)0x40024514))	

// PORT F register definitions
#define GPIO_PORTF_DATA_R       (*((volatile unsigned long *)0x400253FC))
#define GPIO_PORTF_DIR_R        (*((volatile unsigned long *)0x40025400))
#define GPIO_PORTF_AFSEL_R      (*((volatile unsigned long *)0x40025420))
#define GPIO_PORTF_DEN_R        (*((volatile unsigned long *)0x4002551C))
#define GPIO_PORTF_AMSEL_R      (*((volatile unsigned long *)0x40025528))
#define GPIO_PORTF_PCTL_R       (*((volatile unsigned long *)0x4002552C))

// SysTick Timer register definitions
#define NVIC_ST_CTRL_R          (*((volatile unsigned long *)0xE000E010))
#define NVIC_ST_RELOAD_R        (*((volatile unsigned long *)0xE000E014))
#define NVIC_ST_CURRENT_R       (*((volatile unsigned long *)0xE000E018))

// system control register RCGC2 definition
#define SYSCTL_RCGC2_R          (*((volatile unsigned long *)0x400FE108))

// define constants and alias
#define P_LIGHTS 		(*((volatile unsigned long *)0x40025028))  // PORTF, bits 1,3
#define T_LIGHTS 		(*((volatile unsigned long *)0x400050FC))  // PORTB, bits 0,1,2,3,4,5
#define SENSORS			(*((volatile unsigned long *)0x4002401C))  // PORTE, bits 0,1,2


// define constants and alias for SysTick Timer
#define NVIC_ST_CTRL_COUNT      0x00010000  // Count flag
#define NVIC_ST_CTRL_CLK_SRC    0x00000004  // Clock Source
#define NVIC_ST_CTRL_INTEN      0x00000002  // Interrupt enable
#define NVIC_ST_CTRL_ENABLE     0x00000001  // Counter mode
#define NVIC_ST_RELOAD_M        0x00FFFFFF  // Counter load value

// Function Prototypes - Each subroutine defined
void PortB_Init(void);
void PortE_Init(void);
void PortF_Init(void);
void SysTick_init(void);
void Wait_quarterSecond(uint8_t n);

//FSM state data structure
struct State{
	uint32_t Time;
  uint32_t PBOut; 
	uint32_t PFOut;  
  uint32_t Next[8];
};

typedef const struct State STyp;

//Constants Definitions
#define GoS 0
#define WaitS 1
#define GoW 2
#define WaitW 3
#define GoP 4
#define WaitPon1 5
#define WaitPoff1 6
#define WaitPon2 7
#define WaitPoff2 8


STyp FSM[9]={
	{8,0x21,0x02,{GoS,WaitS,WaitS,WaitS,GoS,WaitS,WaitS,WaitS}},
	{4,0x22,0x02,{GoP,GoP,GoW,GoP,GoW,GoP,GoW,GoW}},
	{8,0x0C,0x02,{GoW,WaitW,GoW,WaitW,WaitW,WaitW,WaitW,WaitW}},
	{4,0x14,0x02,{GoS,GoP,GoP,GoP,GoS,GoS,GoS,GoP}},
	{8,0x24,0x08,{GoP,GoP,WaitPon1,WaitPon1,WaitPon1,WaitPon1,WaitPon1,WaitPon1}},
	{1,0x24,0x02,{WaitPoff1,WaitPoff1,WaitPoff1,WaitPoff1,WaitPoff1,WaitPoff1,WaitPoff1,WaitPoff1}},
	{1,0x24,0x00,{WaitPon2,WaitPon2,WaitPon2,WaitPon2,WaitPon2,WaitPon2,WaitPon2,WaitPon2}},
	{1,0x24,0x02,{WaitPoff2,WaitPoff2,WaitPoff2,WaitPoff2,WaitPoff2,WaitPoff2,WaitPoff2,WaitPoff2}},
	{1,0x24,0x00,{GoS,GoW,GoW,GoW,GoS,GoS,GoW,GoS}}
};

int main(void) {
	uint32_t S;
	uint32_t Input;
	// Initialize GPIO Ports A, B, F, SysTick Timer
  PortB_Init();
	PortE_Init();
	PortF_Init();
	SysTick_init();
	// Initial state: Red LED on, the other three LEDs off
  S = GoS;

	while(1) {
		T_LIGHTS = FSM[S].PBOut; //Set light to state output
		P_LIGHTS = FSM[S].PFOut; //Set light to state output
		Wait_quarterSecond(FSM[S].Time); //Set delay to state time
		Input = SENSORS; 				//Read Inputs
		S = FSM[S].Next[Input];
	}
}


// Subroutine to initialize port E pins for inputs
// Inputs: None
// Outputs: None
void PortE_Init(void){
	SYSCTL_RCGC2_R |= 0x00000010; //activate E Clock
	while ((SYSCTL_RCGC2_R&0x00000010) != 0x00000010){} //wait for the clock to be ready

	GPIO_PORTE_AMSEL_R &= ~0x07; 			// disable analog function
	GPIO_PORTE_PCTL_R &= ~0x00000FFF; // GPIO clear bit PCTL
	GPIO_PORTE_DIR_R &= ~0x07; 				// PE2-0 output
	GPIO_PORTE_AFSEL_R &= ~0x07; 			// no alternate function
	GPIO_PORTE_DEN_R |= 0x07; 				// enable digital pins PE2-0  
	GPIO_PORTE_PDR_R |= 0x07; 				// enable pull down resistor on PE2-0
}

// Subroutine to initialize port B pins PB5-0 for outputs
// Inputs: None
// Outputs: None
void PortB_Init(void){   
	SYSCTL_RCGC2_R |= 0x00000002; //activate B Clock
	while ((SYSCTL_RCGC2_R&0x00000002) != 0x00000002){} //wait for the clock to be ready

	GPIO_PORTB_AMSEL_R &= ~0x3F; 			// disable analog function
	GPIO_PORTB_PCTL_R &= ~0x00FFFFFF; // GPIO clear bit PCTL
	GPIO_PORTB_DIR_R |= 0x3F; 				// PB5-0 output
	GPIO_PORTB_AFSEL_R &= ~0x3F; 			// no alternate function
	GPIO_PORTB_DEN_R |= 0x3F; 				// enable digital pins PB5-0  
}

// Subroutine to initialize port F pins PF1,PF3 for outputs
// Inputs: None
// Outputs: None
void PortF_Init(void){   
	SYSCTL_RCGC2_R |= 0x00000020; //activate F Clock
	while ((SYSCTL_RCGC2_R&0x00000020) != 0x00000020){} //wait for the clock to be ready

	GPIO_PORTF_AMSEL_R &= ~0x0A; 			// disable analog function
	GPIO_PORTF_PCTL_R &= ~0x0000F0F0; // GPIO clear bit PCTL
	GPIO_PORTF_DIR_R |= 0x0A; 				// PF1,PF3 output
	GPIO_PORTF_AFSEL_R &= ~0x0A; 			// no alternate function
	GPIO_PORTF_DEN_R |= 0x0A; 				// enable digital pins PF1,PF3
}

// Subroutine to initialize SysTick timer
// Initialize the SysTick timer with maximum reload value
// Enable Systick timer with system clock
// Inputs: None
// Outputs: None
void SysTick_init(void){
	NVIC_ST_CTRL_R = 0;										// disable SysTick during setup
	NVIC_ST_RELOAD_R = 4000000 - 1;				// 0.25sec reload value
	NVIC_ST_CURRENT_R = 0;								// any write to current clears it
	// enable SyStick with core clock
	NVIC_ST_CTRL_R = NVIC_ST_CTRL_ENABLE + NVIC_ST_CTRL_CLK_SRC;
}

// Subroutine to wait 0.25 sec
// Use busy waiting approach to generate n*0.25s delay
// n is specified by the parameter of this function
// Inputs: None
// Outputs: None
void Wait_quarterSecond(uint8_t n){
	unsigned long i;
	for(i=0; i<n; i++){
		NVIC_ST_CURRENT_R = 0;					// any value writtern to current clears 
		while ((NVIC_ST_CTRL_R & NVIC_ST_CTRL_COUNT) == 0){} // Wait for count
	}
}

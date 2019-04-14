#define RIGHT 29
#define LEFT 28
#define DOWN 27
#define UP 26
#define START 25
#define SELECT 24
#define B 23
#define A 22

#define BYTEREADY 0xDD
#define COMMANDSIG 0xFF

byte rightMask = 128;
byte leftMask = 64;
byte downMask = 32;
byte upMask = 16;
byte startMask = 8;
byte selectMask = 4;
byte bMask = 2;
byte aMask = 1;

int oldLatch = 0;

byte latch = 53;
int oldlatch = 0;
int nlatch = 0;
int in = 0;
//
void setup() {
//   put your setup code here, to run once:
  pinMode(latch, INPUT);
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(SELECT, OUTPUT);
  pinMode(START, OUTPUT);
  pinMode(UP, OUTPUT);
  pinMode(DOWN, OUTPUT);
  pinMode(LEFT, OUTPUT);
  pinMode(RIGHT, OUTPUT);
  Serial.begin(115200);
//
  digitalWrite(RIGHT, HIGH);
  digitalWrite(LEFT, HIGH);
  digitalWrite(UP, HIGH);
  digitalWrite(DOWN, HIGH);
  digitalWrite(START, HIGH);
  digitalWrite(SELECT, HIGH);
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);

}
////bool go = false;
void loop() {
//  int nLatch = digitalRead(latch);
//  if (nLatch == HIGH && oldLatch == LOW) {

  
    

    Serial.write(COMMANDSIG);
    Serial.write(BYTEREADY);
    
    //while (Serial.available() <= 0); // sleep
    
    //in = Serial.read();
    nlatch = digitalRead(latch);
    if (oldLatch == HIGH && nlatch == LOW){
    in = Serial.read();
    /*switch(in) {
     case 'w' :
      writeButtons(upMask);
      break;
     case 's' :
      writeButtons(downMask);
      break;
     case 'a' : 
      writeButtons(leftMask);
      break;
     case 'd' :
      writeButtons(rightMask);
      break;
     case ' ' :
      writeButtons(aMask);
      break;
     case 'j' :
      writeButtons(bMask);
      break;
     case 'r':
      writeButtons(startMask);
      break;
     default:
      break;
    }*/
    if (in == 0xFF) {
      Serial.read();
    } else {
      writeButtons(in);
    }
  //}
    }
    
    oldLatch = nlatch;
}

/*void loop() {
  // put your main code here, to run repeatedly:
  int nLatch = digitalRead(latch);
  // serial play game
  if (nLatch == HIGH && oldLatch == LOW) {
  
  
    Serial.write(COMMANDSIG);
    Serial.write(BYTEREADY);
    
    //while (Serial.available() <= 0); // sleep
    
    incomingByte = Serial.read();
  
    Serial.println(incomingByte);
    
    if (incomingByte == 0xFF) {
      incomingByte = Serial.read();
      
      if (incomingByte == 0xAA) {
        while(true) {
          //freeze
        }
      }
    }
    else {
      writeButtons(incomingByte);
    } 

  }
  
  oldLatch = nLatch;

  Serial.println("pulse");
}*/

void writeButtons(byte buttons)
{
    // Shift out the button inforçççation from the data byte
    // and make each pin HIGH or LOW accordingly
    buttons = ~buttons;
    digitalWrite(A,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(B,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(SELECT,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(START,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(UP,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(DOWN,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(LEFT,      buttons & 1);
    buttons = buttons >> 1;
    digitalWrite(RIGHT,      buttons & 1);
}


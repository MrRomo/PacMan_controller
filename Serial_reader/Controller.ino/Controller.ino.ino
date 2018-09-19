
int b12 = 12;
int b11 = 11;
int b10 = 10;
int b9 = 9;
int mov = 4, pastmov = 0;
int incomingByte = 0;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(b12, INPUT_PULLUP);
  pinMode(b11, INPUT_PULLUP);
  pinMode(b10, INPUT_PULLUP);
  pinMode(b9, INPUT_PULLUP);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if(incomingByte=='a'){
      Serial.println(5);  
    }    
  }

  if (pastmov != mov) {
    Serial.print(mov);
    pastmov = mov;
  }
  if (!digitalRead(b12)) {
    mov = 0;
  }
  else if (!digitalRead(b11)) {
    mov = 1;
  }
  else if (!digitalRead(b10)) {
    mov = 2;
  }
  else if (!digitalRead(b9)) {
    mov = 3;
  }

}

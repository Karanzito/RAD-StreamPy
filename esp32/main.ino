// Upload this code to your microcontroller
int button1Pin = 0;
int button2Pin = 1;
int button3Pin = 2;
int button4Pin = 3;

int button_1 = 0;
int button_2 = 0;
int button_3 = 0;
int button_4 = 0;

int hold = 250;

void buttonInput() {

  button_1 = digitalRead(button1Pin); // read the button 1 state
  button_2 = digitalRead(button2Pin); // read the button 2 state
  button_3 = digitalRead(button3Pin); // read the button 3 state
  button_4 = digitalRead(button4Pin); // read the button 4 state

  if (button_1 == LOW) {
    Serial.println("BTN_1");
    delay(hold);
  } 
  else if (button_2 == LOW) {
    Serial.println("BTN_2");
    delay(hold);
  }
  else if (button_3 == LOW) {
    Serial.println("BTN_3");
    delay(hold);
  }

  else if (button_4 == LOW) {
    Serial.println("BTN_4");
    delay(hold);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  delay(2000);

  pinMode(button1Pin, INPUT_PULLUP);
  pinMode(button2Pin, INPUT_PULLUP);
  pinMode(button3Pin, INPUT_PULLUP);
  pinMode(button4Pin, INPUT_PULLUP);

  Serial.println("Hello Wolrd");
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonInput();
}
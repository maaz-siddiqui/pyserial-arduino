int analogPin = A3;
int pos = A1;
int neg = A5;

void setup() {
  Serial.begin(115200);
  pinMode(analogPin, INPUT);
  pinMode(pos, OUTPUT);
  pinMode(neg, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  analogWrite(pos, 255);
  analogWrite(neg, 255);
  // put your setup code here, to run once:
}
char val = 'l';
void loop() {
  if(Serial.available()){
    val = Serial.read();
  }
  switch(val){
    case 'l':
      digitalWrite(LED_BUILTIN, LOW);
      break;
    case 'h':
      digitalWrite(LED_BUILTIN, HIGH);
      break;
  }
    
}

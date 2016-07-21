int LEDPIN = 7;
int LEDPIN2 = 8;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPIN, OUTPUT);
  pinMode(LEDPIN2, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEDPIN, HIGH);
  delay(300);
  digitalWrite(LEDPIN, LOW);
  delay(150);
  digitalWrite(LEDPIN, HIGH);
  delay(300);
  digitalWrite(LEDPIN, LOW);
  delay(150);

  digitalWrite(LEDPIN2, HIGH);
  delay(700);
  digitalWrite(LEDPIN2, LOW);
  delay(150);

}

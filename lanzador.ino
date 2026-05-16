/*
Autor: Nicolas Luengas
26/04/2026
Lanzador de señales Serial de ESP32
*/

#define MICPIN 0
#define CAMPIN 1
#define HANPIN 2

typedef struct {
  int pin;
  int estadoActual;
  int estadoAnterior;
} boton;

void inicializar(boton* button, int pin) {
  button->pin = pin;
  pinMode(pin, INPUT_PULLUP);
  button->estadoActual = digitalRead(pin);
  button->estadoAnterior = digitalRead(pin);
}

bool checkear(boton* button) {
  bool send;
  button->estadoActual = digitalRead(button->pin);
  send = (button->estadoActual != button->estadoAnterior) ? true : false;
  button->estadoAnterior = button->estadoActual;
  return send;
}

boton microfono;
boton mano;
boton camara;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  inicializar(&microfono, MICPIN);
  inicializar(&mano, CAMPIN);
  inicializar(&camara, HANPIN);
  Serial.println("init");
}

void loop() {
  if (checkear(&microfono)) Serial.println("microp");
  if (checkear(&camara)) Serial.println("camera");
  if (checkear(&mano)) Serial.println("handup");
  delay(100);
}

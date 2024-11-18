// Al apretar el boton cambia de color la tira LED y muestra un mensaje en el monitor a vel 9600 del estado
// Se incorporó el intervalo de delay y se corrigió color de fase 0 y fase 2


// Pines de las luces 
const int pinG = 11; // Verde
const int pinB = 10; // Azul
const int pinR = 9; // Rojo

// Pin del botón
const int buttonPin = 2;

// Variables de estado
int buttonState = 0;
int lastButtonState = 0;
int phase = 0; // Fase inicial
bool buttonLocked = false; // Variable para bloquear el botón en fase 1

// Variables para el parpadeo en la fase 0
unsigned long previousMillis = 0;
const long interval = 500; // Intervalo de 500 ms para el parpadeo
bool isRedOn = true; // Controla si está encendido Rojo o Blanco

// Variables para la rampa de color en fase 1
unsigned long phase1PreviousMillis = 0;
const long phase1Interval = 500; // Intervalo de 500 ms para cambiar colores en fase 1
int rainbowStep = 0; // Paso actual del arcoíris

// Variables para la duración de la fase 1
const long phase1Duration = 40000; // Duración de la fase 1 en milisegundos (40 segundos)
unsigned long phase1StartMillis = 0; // Momento en que inicia la fase 1

void setup() {
  // Configurar los pines
  pinMode(pinR, OUTPUT);
  pinMode(pinG, OUTPUT);
  pinMode(pinB, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP); // Botón con resistencia pull-up
  
  // Configurar los LEDs apagados al inicio
  turnOffAllLeds();
  
  // Iniciar la comunicación serie a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Leer el estado del botón
  buttonState = digitalRead(buttonPin);

  // Detectar cambio de estado (pulsación)
  if (buttonState == LOW && lastButtonState == HIGH && !buttonLocked) {
    phase = (phase + 1) % 3; // Cambiar de fase
    Serial.print("Fase cambiada a: ");
    Serial.println(phase);

    if (phase == 1) {
      phase1StartMillis = millis(); // Registrar el tiempo de inicio de la fase 1
      buttonLocked = true; // Bloquear el botón en la fase 1
    }

    delay(200); // Deshabilitar rebote del botón
  }

  lastButtonState = buttonState;

  // Ejecutar acciones específicas según la fase actual
  if (phase == 0) {
    // Fase 0: Parpadeo Blanco y Rojo
    if (hasIntervalPassed(previousMillis, interval)) {
      if (isRedOn) {
        // Encender Rojo
        setColor(255, 0, 0);
      } else {
        // Encender Blanco (RGB combinados)
        setColor(255, 255, 255);
      }
      // Cambiar estado de isRedOn para el próximo ciclo
      isRedOn = !isRedOn;
    }
  } else if (phase == 1) {
    // Fase 1: Ciclo de colores tipo arcoíris
    if (millis() - phase1StartMillis <= phase1Duration) {
      if (hasIntervalPassed(phase1PreviousMillis, phase1Interval)) {
        switch (rainbowStep) {
          case 0: setColor(255, 0, 0); break;    // Rojo
          case 1: setColor(255, 127, 0); break;  // Naranja
          case 2: setColor(255, 255, 0); break;  // Amarillo
          case 3: setColor(0, 255, 0); break;    // Verde
          case 4: setColor(0, 0, 255); break;    // Azul
          case 5: setColor(75, 0, 130); break;   // Añil
          case 6: setColor(148, 0, 211); break;  // Violeta
        }
        rainbowStep = (rainbowStep + 1) % 7; // Ciclar entre los 7 colores del arcoíris
      }
    } else {
      // Finalizar la fase 1 y pasar automáticamente a la fase 2
      phase = 2;
      buttonLocked = false; // Desbloquear el botón al final de la fase 1
      Serial.println("Fase cambiada a: 2");
    }
  } else if (phase == 2) {
    // Fase 2: Rojo encendido fijo
    setColor(255, 0, 0);
   // Serial.println("Fase: 2");
  }
}

void setColor(int red, int green, int blue) {
  // Establecer los valores indicados de R, G, B
  analogWrite(pinR, red);
  analogWrite(pinG, green);
  analogWrite(pinB, blue);

  // Mostrar en el monitor serie para depuración
 // Serial.print("Valores RGB: R=");
 // Serial.print(red);
 // Serial.print(" G=");
 // Serial.print(green);
 // Serial.print(" B=");
 // Serial.println(blue);
}

void turnOffAllLeds() {
  digitalWrite(pinR, LOW);
  digitalWrite(pinG, LOW);
  digitalWrite(pinB, LOW);
}

bool hasIntervalPassed(unsigned long &previousMillis, long interval) {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    return true;
  }
  return false;
}

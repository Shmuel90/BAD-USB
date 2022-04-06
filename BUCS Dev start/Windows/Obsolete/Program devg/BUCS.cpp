#include <windows.h>
#include <winuser.h>
#include <iostream>
//WNDPRC wndproc;

LRESULT CALLBACK wndproc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam){
    if(msg == WM_DEVICECHANGE) {
        //Do the thing
        cout << "worked";
    }
}

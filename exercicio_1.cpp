#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double num1, num2;
    
    cout << "Digite o primeiro número: ";
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2;
    
    double soma = num1 + num2;
    double subtracao = num1 - num2;
    double multiplicacao = num1 * num2;
    double divisao = num1 / num2;
    double resto = fmod(num1, num2);
    double potenciacao = pow(num1, num2);
    
    cout << fixed << setprecision(6);
    cout << "Soma: " << soma << endl;
    cout << "Subtração: " << subtracao << endl;
    cout << "Multiplicação: " << multiplicacao << endl;
    cout << "Divisão: " << divisao << endl;
    cout << "Resto da divisão: " << resto << endl;
    cout << "Potenciação: " << potenciacao << endl;
    
    return 0;
}
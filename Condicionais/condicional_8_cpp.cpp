// Exercício 8 - Calculadora Simples com Condicionais (C++)

#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char operador;
    
    cout << "Digite o primeiro número: ";
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2;
    cout << "Digite o operador (+, -, *, /): ";
    cin >> operador;
    
    if (operador == '+') {
        double resultado = num1 + num2;
        cout << "Resultado: " << resultado << endl;
    } else if (operador == '-') {
        double resultado = num1 - num2;
        cout << "Resultado: " << resultado << endl;
    } else if (operador == '*') {
        double resultado = num1 * num2;
        cout << "Resultado: " << resultado << endl;
    } else if (operador == '/') {
        if (num2 != 0) {
            double resultado = num1 / num2;
            cout << "Resultado: " << resultado << endl;
        } else {
            cout << "Erro: Divisão por zero!" << endl;
        }
    } else {
        cout << "Operador inválido!" << endl;
    }
    
    return 0;
}
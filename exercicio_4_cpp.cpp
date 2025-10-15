#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double num1, num2;
    
    cout << "Digite o primeiro número: ";
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2;
    
    bool maior = num1 > num2;
    bool menor = num1 < num2;
    bool igual = num1 == num2;
    bool diferente = num1 != num2;
    bool maior_igual = num1 >= num2;
    bool menor_igual = num1 <= num2;
    
    cout << boolalpha; // Para mostrar true/false em vez de 1/0
    cout << num1 << " > " << num2 << " : " << maior << endl;
    cout << num1 << " < " << num2 << " : " << menor << endl;
    cout << num1 << " == " << num2 << " : " << igual << endl;
    cout << num1 << " != " << num2 << " : " << diferente << endl;
    cout << num1 << " >= " << num2 << " : " << maior_igual << endl;
    cout << num1 << " <= " << num2 << " : " << menor_igual << endl;
    
    return 0;
}
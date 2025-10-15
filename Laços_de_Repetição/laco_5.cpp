#include <iostream>
#include <string>
using namespace std;

int main() {
    string senha_correta = "python123";
    string senha;
    
    while (true) {
        cout << "Digite a senha: ";
        cin >> senha;
        
        if (senha == senha_correta) {
            cout << "Acesso permitido!" << endl;
            break;
        } else {
            cout << "Senha incorreta! Tente novamente." << endl;
        }
    }
    
    return 0;
}
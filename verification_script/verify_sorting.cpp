#include <iostream>
#include <string>

using namespace std;

int main() {
    string f, last_f, t, last_t;
    int day, price;
    //cin, pls at least one row.
    cin>>f;
    cin>>last_f>>last_t>>day>>price;
    while (cin>>f>>t>>day>>price) {
        if (last_f==f && last_t>t) {
            cout<<"Data not sorted"<<endl;
            return 0;
        }
        if (last_f>f) {
            cout<<"Data not sorted"<<endl;
            return 0;
        }
        swap(last_f, f);
        swap(last_t, t);
    }
    return 0;
}


I am not sure how it fixes first issue.
/*
#include <bits/stdc++.h>
using namespace std;


#define forf(i,a,b) for(int i=(a);i<(b);i++)

int solve(int n){
    int table[n+1];
    memset(table,0,sizeof(table));
    table[0]=1;
    forf(i,3,n+1){
        table[i]+=table[i-3];
    }
    forf(i,5,n+1){
        table[i]+=table[i-5];
    }
    forf(i,10,n+1){
        table[i]+=table[i-10];
    }
    return table[n];
}

int main() {
	int test;
	cin >> test;
	while(test--){
	    int n;
	    cin >> n;
	    int val=solve(n);
	    cout << val << "\n";
	}
	return 0;
}
*/
MRSCD = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 
                    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', 
                    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'} 

def encrpt(S): 
    cp = '' 
    for a in S: 
        if a != ' ': 
            cp += MRSCD[a] + ' '
        else: 
            cp += ' '
    return cp 

def dcrpt(S): 
    S += ' '
    dcp = '' 
    ctxt = '' 
    for a in S: 
        if (a != ' '): 
            i = 0
            ctxt += a 
        else: 
            i += 1
            if i == 2 : 
                dcp += ' '
            else: 
                dcp += list(MRSCD.keys())[list(MRSCD.values()).index(ctxt)] 
                citext = '' 
    return dcp 

def main(): 
    msg = "S"
    MsgMrs = encrpt(msg.upper()) 
    print (MsgMrs) 
  
    MrsMsg = dcrpt(MsgMrs)  
    print (MrsMsg) 

if __name__ == '__main__': 
    main()

// Paranthesis checker using stack (){}[]
#include<iostream>
using namespace std;
class stack
{
    public:
        int top = -1, len = 100;
        char s[100],x;
  
        int push(char x);
        int pop();
        void display();
        bool isempty();
};

int stack::push(char x)
{
    if (top == (len-1))
    {
        cout<<"Stack Overflow"<<endl;
    }
    else
    {
        top ++;
        s[top] = x;        
    }
    return 0;
}

void stack::display()
{
    if (top == -1)
    {
        cout<<"Stack is Empty";
    }
    else
    {
        for (int i = 0; i <= top; i++)
        {
            cout<<s[i]<<" ";
        }
        
    }
}

int stack::pop()
{
    if(top == -1)
    {
        cout<<"Stack Underflow";
    }
    else
    {
        top --;
    }
    return 0;
}

bool stack::isempty()
{
    if (top == -1)
    {
        return true;
    }
    else
    {
        return false;
    }
    
}
int main()
{
    stack s;
    char ch[100];
    int i =0;
    cout<<"Enter the expression : ";
    cin>>ch;
    if ((ch[0]== ')') || (ch[0]== ']') || (ch[0]== '}') )
    {
        cout<<"Invalid Expression"<<endl;
        return -1;
    }
    else
    {
        while (ch[i] != '\0')
        {
            switch (ch[i])
            {
            case '(':
                s.push(ch[i]);
                break;
            case '{':
                s.push(ch[i]);
                break;
            case '[':
                s.push(ch[i]);
                break;
            case ')':
                if (s.s[s.top] == '(')
                {
                    s.pop();
                }
                break;
            case ']':
                if (s.s[s.top] == '[')
                {
                    s.pop();
                }
                break;
            case '}':
                if (s.s[s.top] == '{')
                {
                    s.pop();
                }
                break;
            
            }
            i++;
        }

        if (s.isempty())
        {
            cout<<"Proper Paranthesis Given"<<endl;
        }
        else
        {
            cout<<"Improper Paranthesis"<<endl;
        }
        
        
    }

    
    return 0;
}

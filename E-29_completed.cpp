#include <iostream>
using namespace std;
#define Size 3

// global variables declaration
int queue[Size], front = -1, rear = -1;

int enqueue()
{
    int x;
    if (rear == -1)
    {
        cout << "Intitializing Queue \n"
             << endl;
        front = 0;
    }

    if (rear == (Size - 1))
    {
        cout << "Queue Overflow \n"
             << endl;
        return 0;
    }
    else
    {
        cout << "Enter Job value ";
        cin >> x;
        queue[rear] = x;
    }
    rear++;

    return 0;
}

int dequeue()
{
    int no;

    if (front == rear || front > rear)
    {
        cout << "Queue is empty";
    }
    else
    {
        no = queue[front];
        cout << "\n"
             << no << " was removed from queue\n";
        front++;
    }
    return 0;
}

int display()
{
    int temp = front;
    if (front == rear || front > rear)
    {
        cout << "Queue is Empty";
    }
    else
    {
        for (int i = temp; i < rear; i++)
        {
            cout << queue[i] << " ";
        }
    }

    return 0;
}

int main()
{
    int ch;
    cout << "\n---PRACTICAL E - 29---" << endl;
    while (1)
    {
        cout << "\n\t***** MENU *****";
        cout << "\n1. Add a job";
        cout << "\n2. Remove a job";
        cout << "\n3. Display Current jobs";
        cout << "\n4. Exit";
        cout << "\nEnter your choice: ";
        cin >> ch;

        if (ch == 1)
        {
            enqueue();
        }

        else if (ch == 2)
        {
            dequeue();
        }

        else if (ch == 3)
        {
            display();
        }

        else if (ch == 4)
        {
            exit(0);
        }

        else
        {
            cout << "Invalid Input ";
        }
    }
    return 0;
}
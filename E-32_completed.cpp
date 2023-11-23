#include <iostream>
#define n 5
using namespace std;

class queue
{
    int front = -1, rear = -1, input, size = 0, position;
    int queue[n];

public:
    void stats()
    {
        cout << "Front is " << front << endl;
        cout << "Rear is " << rear << endl;
        cout << "Size is " << size << endl;
    }

    void enqueue();
    void dequeue();
    void display();
};

void queue::enqueue()
{
    position = (rear + 1) % n;
    if (front == position)
    {
        cout << "Parlour is full" << endl;
    }

    else
    {
        rear = (rear + 1) % n;
        cout << "Enter Order No : ";
        cin >> input;
        queue[rear] = input;
        if (front == -1)
        {
            front = rear;
        }
        size++;
    }
}

void queue::dequeue()
{
    if (size == 0)
    {
        cout << "Parlour is empty";
    }

    else
    {
        cout << "Order No. " << queue[front] << " is processed. " << endl;
        front = (front + 1) % n;
        size--;
    }
}

void queue::display()
{
    if (size == 0)
    {
        cout << "Parlour is empty" << endl;
    }

    else
    {
        for (int i = front; i != rear; i = ((i + 1) % n))
        {
            cout << queue[i] << " ";
        }
        cout << queue[rear] << endl;
    }
}

int main()
{
    int ch;
    queue obj;
    while (1)
    {
        cout << "\n\t\t\t***** MENU *****\n"
             << endl;
        cout << "1. Take Order, 2. Serve Order, 3. Current Orders, 4. Close Parlour" << endl;
        cin >> ch;
        cout << endl;

        if (ch == 1)
        {
            obj.enqueue();
        }

        if (ch == 2)
        {
            obj.dequeue();
        }

        if (ch == 3)
        {
            obj.display();
        }

        if (ch == 4)
        {
            cout << "Parlour is closed\nThank You Visit Again.";
            exit(1);
        }
    }
    return 0;
}
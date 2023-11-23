#include <iostream>
#define n 5
using namespace std;

class queue
{
    int front = -1, rear = -1, input, size = 0;
    int queue[n];

public:
    void stats()
    {
        cout << "Front is " << front << endl;
        cout << "Rear is " << rear << endl;
        cout << "Size is " << size << endl;
    }

    void enqueuefront();
    void enqueuerear();
    void dequeuefront();
    void dequeuerear();
    void display();
};

void queue::enqueuefront()
{
    if (front == (n - 1) || front ==0)
    {
        cout << "Queue Overflow" << endl;
    }

    else
    {
        cout << "Enter element : ";
        cin >> input;
        if (front==-1)
        {
            front = 0;
            rear = 0;
            queue[rear]=input;
        }

        else if(front!=0)
        {
            --front;
            queue[front]=input;
        }
        
        size++;
    }

}

void queue::enqueuerear()
{
    if (rear == (n - 1))
    {
        cout << "Queue Overflow" << endl;
    }

    else
    {
        ++rear;
        cout << "Enter element : ";
        cin >> input;
        queue[rear] = input;
        if (front == -1)
        {
            front = rear;
        }
        size++;
    }
}

void queue::dequeuefront()
{
    if (size == 0)
    {
        cout << "Queue is empty";
    }

    else
    {
        cout << queue[front] << " will be deleted" << endl;
        ++front;
        size--;
    }
}

void queue::dequeuerear()
{
    if (size == 0)
    {
        cout << "Queue is empty";
    }

    else
    {
        cout << queue[rear] << " will be deleted" << endl;
        if (front==rear)
        {
            front=rear=-1;
        }
        else
        {
            --rear;
        }
        size--;
    }

}

void queue::display()
{
    if (size == 0)
    {
        cout << "Queue is empty" << endl;
    }

    for (int i = front; i <= rear; i++)
    {
        cout << queue[i] << " ";
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
        cout << "1. Current Positions, 2. Enqueue Front, 3. Enqueue Rear, 4. Dequeue Front, 5. Dequeue Rear, 6. Display, 7. Exit" << endl;
        cin >> ch;
        cout << endl;

        if (ch == 1)
        {
            obj.stats();
        }

        else if (ch == 2)
        {
            obj.enqueuefront();
        }

        else if (ch == 3)
        {
            obj.enqueuerear();
        }

        else if (ch == 4)
        {
            obj.dequeuefront();
        }

        else if (ch == 5)
        {
            obj.dequeuerear();
        }

        else if (ch == 6)
        {
            obj.display();
        }

        else if (ch == 7)
        {
            exit(1);
        }
        
        else
        {
            cout<<"Invalid Input";
        }
    }
    return 0;
}

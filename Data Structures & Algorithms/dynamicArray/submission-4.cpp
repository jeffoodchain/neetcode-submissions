#define MAX_ARRAY_NUM

class DynamicArray {
public:
    int *arr; // just given a point so we don't have to worry about the size.
    int curr_length;
    int max_capacity;

    DynamicArray(int capacity) {
        curr_length = 0;
        max_capacity = capacity;
        // initialize the array to all 0
        for (int i = 0; i < max_capacity; i++) {
            arr[i] = 0;
        }
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (curr_length == max_capacity) resize();
        set(curr_length++, n);
    }

    int popback() {
        int popped = get(--curr_length);
        return popped;
    }

    void resize() {
        int original_capacity = max_capacity;
        max_capacity *= 2;
        int * newArr = new int[max_capacity];
        // copy the original arr element into newArr
        for (int i = 0; i < original_capacity; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    int getSize() {
        return curr_length;
    }

    int getCapacity() {
        return max_capacity;
    }
};

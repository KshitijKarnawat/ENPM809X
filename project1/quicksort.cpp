#include <iostream>
#include <vector>

int partition(std::vector<int> *arr, const int &low, const int &high) {
    int pivot = (*arr)[high];  // taking the last element as pivot
    int i = (low - 1);       // Index of smaller element

    for (int j = low; j < high; j++) {
        // If current element is smaller than or
        // equal to pivot
        if ((*arr)[j] <= pivot) {
            i++;  // increment index of smaller element
            std::swap((*arr)[i], (*arr)[j]);
        }
    }

    std::swap((*arr)[i + 1], (*arr)[high]);
    return (i + 1);
}


void quick_sort(std::vector<int> *arr, const int &low, const int &high) {
    if (low < high) {
        int p = partition(arr, low, high);

        quick_sort(arr, low, p - 1);
        quick_sort(arr, p + 1, high);
    }
}


std::vector<int> quick_sort(std::vector<int> arr, const int &low, const int &high) {
    if (low < high) {
        int p = partition(&arr, low, high);

        quick_sort(&arr, low, p - 1);
        quick_sort(&arr, p + 1, high);
    }
    return arr;
}


void show(const std::vector<int> &arr, const int &size) {
    for (int i = 0; i < size; i++) std::cout << arr[i] << " ";
    std::cout << "\n";
}


int main(){
    std::vector<int> input{1,5,676,23,987,340,13,49,3};
    int begin{0};
    int end{input.size()-1};
    quick_sort(&input, begin, end);
    show(input, input.size());
}

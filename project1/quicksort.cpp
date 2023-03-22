#include <iostream>
#include <vector>

void print_quicksort(std::vector<int> input){
    for(int i = 0; i < input.size(); i++)
        std::cout << input.at(i) << ", ";
    std::cout<<std::endl;
}


int partiton(std::vector<int> input, int begin, int end){
    int temp;
    int x{input.at(end)};
    int i{begin-1};
    for(int j = begin; j < end; j++){
        if(input.at(j) <= x){
            i++;
            
            temp = input.at(i);
            input.at(i) = input.at(j);
            input.at(j) = temp;
        }
    }
    
    temp = input.at(i+1);
    input.at(i+1) = input.at(end);
    input.at(end) = temp;
    
    return i+1;    

}


void quicksort(std::vector<int> input, int begin, int end){
    int part;
    if(begin<end){
        std::cout<<"in quicksort";
        part = partiton(input,begin,end);
        quicksort(input,begin,part-1);
        quicksort(input,part+1,end);
    }
    // print_quicksort(input);
       
}


int main(){
    std::vector<int> input{1,5,676,23,987,340,13,49,3};
    int begin{0};
    int end{input.size()-1};
    quicksort(input, begin, end);
    // print_quicksort(input);
}

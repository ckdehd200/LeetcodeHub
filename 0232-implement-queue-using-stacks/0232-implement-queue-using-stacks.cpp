class MyQueue {
    vector<int> save_stack={};
    vector<int> pop_stack={};
public:
    MyQueue() {
    }
    
    void push(int x) {
        save_stack.push_back(x);
    }
    
    int pop() {
        if(pop_stack.size()==0){
            while(save_stack.size()>0){
                int move = save_stack.back();
                pop_stack.push_back(move);
                save_stack.pop_back();
            }
        }
        int ans = pop_stack.back();
        pop_stack.pop_back();
        return ans;
    }
    
    int peek() {
        if(pop_stack.size()==0){
            while(save_stack.size()>0){
                int move = save_stack.back();
                pop_stack.push_back(move);
                save_stack.pop_back();
            }
        }
        return pop_stack.back();
    }
    
    bool empty() {
        return pop_stack.size()==0 && save_stack.size()==0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
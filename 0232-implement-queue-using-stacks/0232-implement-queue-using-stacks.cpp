class MyQueue {
    stack<int> save_stack={};
    stack<int> pop_stack={};
public:
    MyQueue() {
    }
    
    void push(int x) {
        save_stack.push(x);
    }
    
    int pop() {
        if(pop_stack.size()==0){
            while(save_stack.size()>0){
                int move = save_stack.top();
                pop_stack.push(move);
                save_stack.pop();
            }
        }
        int ans = pop_stack.top();
        pop_stack.pop();
        return ans;
    }
    
    int peek() {
        if(pop_stack.size()==0){
            while(save_stack.size()>0){
                int move = save_stack.top();
                pop_stack.push(move);
                save_stack.pop();
            }
        }
        return pop_stack.top();
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
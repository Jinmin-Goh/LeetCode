// Problem No.: 705
// Solver:      Jinmin Goh
// Date:        20200803
// URL: https://leetcode.com/problems/design-hashset/

#include<set>
#include<iterator>

using namespace std;

class MyHashSet {
public:
    set<int> hashSet;
    MyHashSet() {
        //set<int> hashSet;
    }
    
    void add(int key) {
        if(hashSet.find(key) == hashSet.end()) {
            hashSet.insert(hashSet.begin(), key);
        }
    }
    
    void remove(int key) {
        if(hashSet.find(key) != hashSet.end()) {
            hashSet.erase(hashSet.find(key));
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        if(hashSet.find(key) == hashSet.end()) {
            return false;
        }
        else {
            return true;
        }
    }
};
            
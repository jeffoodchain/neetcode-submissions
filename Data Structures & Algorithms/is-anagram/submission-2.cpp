#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        // use a hashmap to follow the chars num
        unordered_map<char, int> s_char_record;
        unordered_map<char, int> t_char_record;
        
        for (auto c : s) {
            s_char_record[c] += 1;
        }

        for (auto c : t) {
            t_char_record[c] += 1;
        }

        // compare two map
        if (s_char_record == t_char_record) {
            return true;
        }
        return false;
    }
};

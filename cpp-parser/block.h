#ifndef BLOCKCHAIN_PARSER_BLOCK_H
#define BLOCKCHAIN_PARSER_BLOCK_H

#include <string>
#include <vector>
#include "transaction.h"

using namespace std;
class Block {

public:
    string time;
    string prev_hash;
    vector<Transaction> txs;

    Block(string t, string phash, vector<Transaction> transactions) : time(t), prev_hash(phash), txs(transactions)
    {
    }

    ~Block() = default;
};

#endif //BLOCKCHAIN_PARSER_BLOCK_H

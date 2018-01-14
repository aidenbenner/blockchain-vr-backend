#ifndef BLOCKCHAIN_PARSER_BLOCK_H
#define BLOCKCHAIN_PARSER_BLOCK_H

#include <string>
#include <vector>
#include "transaction.h"

using namespace std;
class Block {

public:
    string time;
    int height;
    string hash;
    string prev_hash;
    vector<Transaction> txs;

    Block(int height, string hash, string t, string phash, vector<Transaction> transactions) : height(height), hash(hash), time(t), prev_hash(phash), txs(transactions)
    {
    }

    ~Block() = default;
};

#endif //BLOCKCHAIN_PARSER_BLOCK_H

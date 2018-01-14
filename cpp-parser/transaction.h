#ifndef BLOCKCHAIN_PARSER_TRANSACTION_H
#define BLOCKCHAIN_PARSER_TRANSACTION_H

#include <utility>
#include <vector>

using namespace std;

struct AdrVal {
    string address;
    double val;
};

class Transaction
{
public:
    vector<AdrVal> fromAddr;
    vector<AdrVal> toAddr;
    Transaction(vector<AdrVal> f, vector<AdrVal> t) : fromAddr(f), toAddr(t) { }
    ~Transaction() = default;
};

#endif //BLOCKCHAIN_PARSER_TRANSACTION_H

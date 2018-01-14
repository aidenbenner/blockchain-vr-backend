#include "json.hpp"
#include <iostream>
#include <fstream>
#include <experimental/filesystem>
#include "transaction.h"
#include "block.h"


using json = nlohmann::json;
namespace fs = std::experimental::filesystem;

class JSON_reader {
public:
    JSON_reader(std::string folder_path) {
        auto it = fs::recursive_directory_iterator(fs::path(folder_path.c_str()));
        for (auto curr = fs::begin(it); curr != fs::end(it); curr++) {
            std::ifstream i(fs::canonical(*curr).string());
            json j;
            i >> j;
            add_block(j);
        }
    }

    Block get_block(std::string hash) {
        auto search = blocks.find(hash);
        if (search == blocks.end()) {
            throw invalid_argument("Hash key unrecognized.");
        }
        return search->second;
    }

    std::unordered_map<string, Block>& map() {
        return blocks;
    }

private:

    void add_block(const json& j) {
        auto t = j.at("time").get<std::string>();
        auto p = j.at("prev").get<std::string>();
        auto h = j.at("hash").get<std::string>();
        std::vector<Transaction> txs;
        for (auto& tx : j["tx"]) {
            txs.push_back(json_to_transaction(tx));
        }
        blocks.insert({h, Block(h, p, txs)});
    }

    Transaction json_to_transaction(const json& j) {
        std::vector<AdrVal> froms;
        for (auto& pair: j[0]) {
            froms.push_back(json_to_adrval(pair));
        }
        std::vector<AdrVal> tos;
        for (auto& pair: j[1]) {
            tos.push_back(json_to_adrval(pair));
        }
        return Transaction(froms, tos);
    }

    AdrVal json_to_adrval(const json& j) {
        AdrVal av;
        av.address = j[0];
        av.val = j[1];
        return av;
    }

private:
    std::unordered_map<std::string, Block> blocks;
};

int main() {
 }


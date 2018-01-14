import urllib.request
import json
import datetime
import time 
import os.path


block_url = 'https://blockchain.info/rawblock/'
start_hash = '0000000000000000002fff5695a8ba65fbced03b312c0bf6d5ac1da373fbcc0c'
rate_limit = 2
block_folder = './blocks/'


def getResponse(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def getJsonResponse(url):
    return json.loads(getResponse(url))

def downloadRawBlock(hash):
    return getResponse(block_url + hash)

def converUnixTime(time):
    return datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')

class Block:
    def __init__(self, hash, prev, height, time, tx):
        self.hash = hash
        self.prev = prev
        self.height = height
        self.time = converUnixTime(time)
        self.tx= tx

class Transaction:
    def __init__(self, startAddrs, endAddrs, time):
        self.startAddrs = startAddrs
        self.endAddrs = endAddrs
        self.time = converUnixTime(time)

def parseTransaction(tx):
    inputs = tx['inputs']
    outputs= tx['out']

    time = tx['time']
    startAddrs = []
    endAddrs = []
    for i in inputs:
        if 'prev_out' in i:
            prev_out = i['prev_out']
            addr = prev_out['addr']
            val = prev_out['value'] / (10 ** 8)
            startAddrs.append([addr,val])

    for o in outputs:
        if not 'addr' in o:
            # segwit transaction ignore for now
            continue
        addr = o['addr']
        val = o['value'] / (10 ** 8)
        endAddrs.append([addr,val])

    return [startAddrs, endAddrs, converUnixTime(time)]

def getRawBlock(hash):
    return getJsonResponse(block_url + hash)

def parseBlock(hash):
    # check if we've already downloaded this hash
    fname = fnameFromHash(hash)
    # write if not found
    if not os.path.exists(fname):
        f = open(fname, "w+")
        raw = downloadRawBlock(hash)
        f.write(raw)
        f.close()
    else:
        f = open(fname, "r")
        raw = f.read()
        f.close()
    blk  = json.loads(raw)
    transactions = blk['tx']
    tout = []
    for t in transactions:
        tout.append(parseTransaction(t))

    return Block(hash, blk['prev_block'], blk['height'], blk['time'], tout)

def fnameFromHash(hash):
    return block_folder + hash

def downloadNBlock(n):
    curr_hash = start_hash
    for x in range(n):
        print(curr_hash)
        blk = parseBlock(curr_hash)
        cfname = './clean/' + curr_hash
        f = open(cfname, 'w+')
        cleanjson = json.dumps(blk.__dict__, indent=4, separators=(',', ': '))
        f.write(cleanjson)
        f.close()

        curr_hash = blk.prev
        time.sleep(0)

downloadNBlock(500)




import urllib.request
import json
import datetime

block_url = 'https://blockchain.info/rawblock/'
start_hash = '0000000000000000002fff5695a8ba65fbced03b312c0bf6d5ac1da373fbcc0c'
rate_limit = 2

def getResponse(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def getJsonResponse(url):
    return json.loads(getResponse(url))

def converUnixTime(time):
    return datetime.datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S')


class Block:
    __init__(self, time, transactions):


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

    return [startAddrs, endAddrs]

def getRawBlock(hash):
    return getJsonResponse(block_url + start_hash)

def parseBlock(hash):
    blk  = getJsonResponse(block_url + start_hash)
    transactions = blk['tx']
    tout = []
    for t in transactions:
        tout.append(parseTransaction(t))
    return tout


curr_hash = start_hash
for x in range(10):
    blk = parseBlock(curr_hash)
    next_hash = blk['prev_block']
    time.sleep(rate_limit)


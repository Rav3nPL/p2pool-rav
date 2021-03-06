import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex') #pchmessagestart
P2P_PORT = 52112
ADDRESS_VERSION = 23 #pubkey_address
RPC_PORT = 52111
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'aliencoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 40*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 30 # s
SYMBOL = 'ALN'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'aliencoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/aliencoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.aliencoin'), 'aliencoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://cryptexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://cryptexplorer.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://cryptexplorer.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8

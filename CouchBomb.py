from couchbase.bucket import Bucket
from couchbase.views.parms import Query

STOCK_COUNT = 65348
RECEIPT_ITEM_COUNT = 1163469
BATCH_SIZE = 50000 #default size

BATCH_COUNT = RECEIPT_ITEM_COUNT / BATCH_SIZE
bucket = Bucket('couchbase://ec2-52-64-116-219.ap-southeast-2.compute.amazonaws.com/ReceiptItemSampe')
q = Query
q.limit = BATCH_SIZE

stock_view = bucket.query('id','idList', query = q)

key_list = []

for row in stock_view:
	key_list.append(row.key)
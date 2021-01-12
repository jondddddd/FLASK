import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]

order_management_db = myclient["order_management"]



def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code},{"_id":0})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({},{"_id":0}):
        product_list.append(p)

    return product_list

def get_branch(code):
    branches_coll = products_db["branches"]
    branch = branches_coll.find_one({"code":code})
    return branch

def get_branches():
    branch_list = []
    branches_coll = products_db["branches"]
    for y in branches_coll.find({}):
        branch_list.append(y)

    return branch_list

def get_past_order(username):
    orders_coll = order_management_db["orders"]
    past_orders = orders_coll.find_one({"username":username})
    return past_orders
def get_past_order():

    past_orders_list = []

    orders_coll = order_management_db["orders"]

    for o in orders_coll.find({}):
        past_orders_list.append(o)

    return past_orders_list
def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user
def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)

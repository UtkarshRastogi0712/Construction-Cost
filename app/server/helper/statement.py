def get_statement_details(item_list):
    expenditure=0
    count=0
    for i in item_list:
        expenditure+=(i["price"]*i["quantity"])
        count+=1
    return {"expenditure" : expenditure, "count" : count}
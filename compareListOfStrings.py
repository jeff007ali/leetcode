def findDiff(d1, d2, path=""):
    for k in d1:
        if (k not in d2):
            print (path, ":")
            print (k + " as key not in d2", "\n")
        else:
            if type(d1[k]) is dict:
                if path == "":
                    path = k
                else:
                    path = path + "->" + k
                findDiff(d1[k],d2[k], path)
            # elif type(d1[k]) is list:

            else:
                if d1[k] != d2[k]:
                    print (path, ":")
                    print (" - ", k," : ", d1[k])
                    print (" + ", k," : ", d2[k])




old_list = ["Tap on the ride you would like to cancel", '{"text": "", "type": "TEXT", "data": {"quick_replies": [{"actionable_text": "Calculate again", "is_default": 0, "type": "TEXT_ONLY", "payload": {"link": "", "message": "Calculate [product_name] premium again{task}", "gogo_message": ""}}, {"actionable_text": "Talk to Edelweiss Tokio", "is_default": 0, "type": "TEXT_ONLY", "payload": {"link": "", "message": "Talk to Edelweiss Tokio", "gogo_message": ""}}, {"actionable_text": "Show all products", "is_default": 0, "type": "TEXT_ONLY", "payload": {"link": "", "message": "Show all products{task}", "gogo_message": ""}}]}, "isNew": false}', "Your upcoming Rides" , "xyz"]
new_list = ["Tap on the ride you would like to cancel", '{"text": "", "type": "TEXT", "data": {"quick_replies": [{"actionable_text": "Calculate not again", "is_default": 0, "type": "TEXT_ONLY", "payload": {"link": "", "message": "Calculate [product_name] premium again{task}", "gogo_message": ""}}, {"actionable_text": "Talk to Edelweiss Tokio", "is_default": 0, "type": "TEXT_ONLY", "payload": {"link": "", "message": "Talk to Edelweiss Tokio", "gogo_message": ""}}, {"actionable_text": "Show all articles", "is_default": 0, "type": "TEXT_ONLY", "payload": {"link": "", "message": "Show all articles{task}", "gogo_message": ""}}]}, "isNew": false}', "Your upcoming Ride", "abc"]

d1= {'a':{'b':{'cs':10},'d':{'cs':[20]}}}
d2= {'a':{'b':{'cs':30} ,'d':{'cs':[20,30]}},'newa':{'q':{'cs':50}}}

updated_old_list = list(set(old_list) - set(new_list))
updated_new_list = list(set(new_list) - set(old_list))

print("updated items : {}".format(updated_old_list),"\n", "\n")
print("Added items : {}".format(updated_new_list),"\n", "\n")

# for i in range(len(old_list)):

print ("comparing d1 to d2:")
print (findDiff(d1,d2))
print ("comparing d2 to d1:")
print (findDiff(d2,d1))
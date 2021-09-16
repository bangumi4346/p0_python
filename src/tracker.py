

itemTotal = 0
itemDict = {
    "itemName": [],
    "itemCount": [],
    "itemPrice": []
}


# Table management portion
class tracker:
    # add new item

    def newItem(name:str, count:int, price:float):
        itemDict["itemName"].append(name)
        itemDict["itemPrice"].append(price)
        itemDict["itemCount"].append(count)
        
        global itemTotal 
        itemTotal+=1
        print("Action newItem: " + name + ", itemToal=" + str(itemTotal))
        pass

    # change item count
    def updateCount(name:str, count:int):
        index = itemDict["itemName"].index(name)
        itemDict["itemCount"][index] = count
        print("Action: updateCount - " + name + " to " + str(count))
        pass

    # change item prince
    def updatePrice(name:str, price:float):
        index = itemDict["itemName"].index(name)
        itemDict["itemPrice"][index] = price
        print("Action: updatePrice - " + name + " to " + str(price))
        pass

    # delete item
    def deleteItem(name:str):
        index = itemDict["itemName"].index(name)
        itemDict["itemName"].remove(index)
        itemDict["itemCount"].remove(index)
        itemDict["itemPrice"].remove(index)
        pass

    # print table
    def printTable(*args):
        if itemTotal != 0:
            print("name \tcount \tprice")
            for i in range(0, itemTotal):
                print(itemDict["itemName"][i] + "\t" + str(itemDict["itemCount"][i]) + "\t" + str(itemDict["itemPrice"][i]))
            print("\n")
        else:
            print("THE TABLE IS EMPTY")
        pass

    # load from file
    def loadFile(path:str):
        pass

    # reset current table
    def resetTable(*args):
        itemDict.clear()
        global itemTotal
        itemTotal = 0
        pass




    # testbench
    '''
    newItem("apple", 1.15, 15)
    printTable()

    newItem("pears", 1.2, 8)
    printTable()

    updateCount("apple", 10)
    printTable()

    updatePrice("pears", 1.25)
    printTable()

    resetTable()
    printTable()
    '''
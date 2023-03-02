from kiwoommanager import KiwoomManager

if __name__ == "__main__":
    km = KiwoomManager()
    #km.put_method("005930")
    #print(km.get_method())

    km.put_tr("005930")
    print(km.get_tr())
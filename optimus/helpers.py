import gc

def queryset_iterator(queryset, chunksize=1000):
    '''
    Iterate over a Django Queryset ordered by the primary key

    This method loads a maximum of chunksize (default: 1000) rows in it's
    memory at the same time while django normally would load all rows in it's
    memory. Using the iterator() method only causes it to not preload all the
    classes.
    '''
    queryhelper = queryset[:]
    numresults = queryhelper.count()
    
    count = queryhelper.count()
    if count > chunksize:
        numPages = count/chunksize+1
        indexes = xrange(1, numPages+1)
    else:
        indexes = xrange(1, 2)
    
    for p in indexes:
        rows = queryhelper[(p-1)*chunksize:(p)*chunksize]
        for row in rows:
            yield row
        del pages
        #added garbage collecting to reduce the memory use with trash and speed up the tool
        gc.collect()
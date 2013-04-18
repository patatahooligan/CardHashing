CARD_NUM = 500000

class X17 (object):
    def __init__(self, max_index=CARD_NUM):
        self.max_index = max_index

    def __call__(self, key, size=None):
        if size is None:
            size = self.max_index

        _hash = len(key)
        while len(key)>1:
            _hash = ( ( ( ( _hash * 17 ) + ( ord(key[0]) - ord(' ') ) ) * 17 ) + ( ord(key[1]) - ord(' ') ) ) % size
            key = key[2:]

        if len(key) == 1:
            _hash = (( _hash * 17 ) + ( ord(key[0]) - ord(' ') )) % size;

        return _hash


class Purchase(object):
    """ A single purchase
    """

    def __init__(self, day, card_id, products):
        """ Day is stored as a number, products is an array of (product_id, quantity) tuples.
	"""

        self.day = day
        self.card_id = card_id
        self.products = products

    @property
    def key(self):
        """
        """

        return self.card_id

    def __str__(self):
        """
        """

        ret = str(day) + " " + card_id
        #for p in self.products:


class FileManager(object):
    """Handles all the file input and converts the data from string to a
    usable format.
    """

    def __init__(self):
        """
	"""

        pass

    def get_purchase_history(self, purchase_file):
        """ From given file, extracts purchase history and converts it to a
        list.
        """

        f = open(purchase_file)
        data = f.read()

        # Seperate purchases into different entries
        data = data.split("\n")[:-1]

        ret = []
        for entry in data:
            [day, card_id, products] = entry.split(" ")

            # Transform the products into tuples of id,quantity
            products = products.split(';')
            products = [p.split(',') for p in products[:-1]]
            products = [(p,int(q)) for p,q in products]
            ret.append(Purchase(day, card_id, products))

        return ret


class HashTable(object):
    """
    """

    def __init__(self, size, function=X17, step=1):
        """ Create an empty list of given size to be used as a hash table.
	"""

        self.table = [None]*size
        self.func = function()
        self.no_of_elements = 0

    def insert(self, obj, key=None):
        """
        """

        pos = self.func(key)
        while self.table[pos] is not None and self.table[pos]!="deleted":
            pos = (pos + self.step) % self.size

        self.table[pos] = obj
        self.no_of_elements += 1

    def lookup(self, key):
        """Lookup the key in the table and return corresponding item. Returns
        None if item is not found
        """

        pos = self.func(key)
        init_pos = pos
        while self.table[pos] is not None:
            if self.table[pos] != "deleted":
                obj = self.table[pos]
                if obj.key == key:
                    return obj

            pos = (pos + self.step) % self.size
            if pos == init_pos:
                break

        return None

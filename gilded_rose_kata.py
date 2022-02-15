

class GildedRose(object):

    def __init__(self, stock):
        self.stock = stock

    def update_quality(self):
        for item in self.stock:
            item.update_quality()

    def add_item(self, item):
        self.stock.append(item)


class Updateable:
    def update_quality(self):
        pass


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal_item(Item, Updateable):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def set_quality(self, increment):
        if self.quality + increment > 50:
            self.quality = 50

        elif self.quality + increment >= 0:
            self.quality = self.quality + increment

        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.set_quality(-1)

        else:
            self.set_quality(-2)


class Conjured_item(Item):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def set_quality(self, increment):
        if self.quality + increment > 50:
            self.quality = 50

        elif self.quality + increment >= 0:
            self.quality = self.quality + increment

        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.set_quality(-2)

        else:
            self.set_quality(-4)


class Aged_brie(Item):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def set_quality(self, increment):
        if self.quality + increment > 50:
            self.quality = 50

        elif self.quality + increment >= 0:
            self.quality = self.quality + increment

        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.set_quality(1)

        else:
            self.set_quality(2)


class Sulfuras(Item):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def set_quality(self, increment):
        if self.quality + increment > 50:
            self.quality = 50

        elif self.quality + increment >= 0:
            self.quality = self.quality + increment

        else:
            self.quality = 0

    def update_quality(self):
        if self.quality != 80:
            self.set_quality(-80)
            print("We will be doomed")


class Backstage_pass(Item):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def set_quality(self, increment):
        if self.quality + increment > 50:
            self.quality = 50

        elif self.quality + increment >= 0:
            self.quality = self.quality + increment

        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in <= 0:
            self.set_quality(-50)

        elif self.sell_in < 5:
            self.set_quality(3)

        elif self.sell_in < 10:
            self.set_quality(2)

        else:
            self.set_quality(1)

### TEST ###


if __name__ == '__main__':
    print()
    print("=== WELCOME TO OLIVANDER'S ===")
    print()

    item = Aged_brie("Aged Brie", 2, 0)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        item.set_sell_in()
        print(item)

    itemInterfaz = Updateable()
    itemInterfaz.update_quality()

    ##############################

    item = Normal_item("Elixir of the Mongoose", 5, 7)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        item.set_sell_in()
        print(item)

    itemInterfaz = Updateable()
    itemInterfaz.update_quality()

    ##############################

    item = Conjured_item("Wand", 10, 20)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        item.set_sell_in()
        print(item)

    itemInterfaz = Updateable()
    itemInterfaz.update_quality()

    ##############################

    item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        item.set_sell_in()
        print(item)

    itemInterfaz = Updateable()
    itemInterfaz.update_quality()

    ##############################

    item = Backstage_pass("Backstage Pass CFK8", 10, 10)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 15):
        item.update_quality()
        item.set_sell_in()
        print(item)

    itemInterfaz = Updateable()
    itemInterfaz.update_quality()

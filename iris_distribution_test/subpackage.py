# only for test
import iris_distribution_test

def showver():
    print 'self: ', __name__, ' : ',__file__
    print 'parent: ', iris_distribution_test.__name__, ' : ',iris_distribution_test.__file__

if __name__ == '__main__':
    showver()

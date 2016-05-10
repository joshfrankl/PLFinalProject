class course(object):
    def f(self):
        data = {
            'coursename': 'Elements of Programming Languages',
            '$coursename': lambda x: data.update({'coursename': x}),
            'number': 'CS329E',
            '$number': lambda x: data.update({'number': x}),
            'grade': 'None assigned',
            '$grade': lambda x: data.update({'grade': x})
        }
        def cf(self,d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)

class gradeFinder(course):
# This is not designed to actually find grades for corresponding courses.
# Written just to show that we can use closures.
    def f(self):
        data = {
            'number': 'PHY362K',
            '$number': lambda x: data.update({'number': x})
        }
        def cf(self,d):
            if d in data:
                return data[d]
            else:
                return super(gradeFinder, self).run(d)
        return cf
    run = f(1)

def createCourse(name, number, grade):
    newCourse = course()
    c1.run('$coursename')(name)
    c1.run('$number')(number)
    c1.run('$grade')(grade)

    print c1.run('coursename')
    print c1.run('number')
    print c1.run('grade')

c1 = course()
print c1.run('coursename')
print c1.run('number')
print c1.run('grade')
print c1.run('average')
c1.run('$coursename')('Quantum Physics II')
c1.run('$number')('PHY362K')
c1.run('$grade')('A')
print "\n"
print c1.run('coursename')
print c1.run('number')
print c1.run('grade')

g1 = gradeFinder()
print "\n"
print g1.run('number')
print g1.run('coursename')
print g1.run('grade')

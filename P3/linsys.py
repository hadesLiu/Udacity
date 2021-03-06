# -*- coding:utf-8 -*-
# author: hiro

from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        n = self[row].normal_vector
        k = self[row].constant_term
        new_normal_vector = n.times_scalar(coefficient)
        new_constant_term = k * coefficient
        self[row] = Plane(normal_vector=new_normal_vector, constant_term=new_constant_term)


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        n1 = self[row_to_add].normal_vector
        k1 = self[row_to_add].constant_term
        n2 = self[row_to_be_added_to].normal_vector
        k2 = self[row_to_be_added_to].constant_term

        new_normal_vector = n1.times_scalar(coefficient).plus(n2)
        new_constant_term = (k1 * coefficient) + k2

        self[row_to_be_added_to] = Plane(normal_vector=new_normal_vector, constant_term=new_constant_term)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def compute_triangular_form(self):
        system = deepcopy(self)

        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                constant = MyDecimal(system[i].normal_vector[j])
                if constant.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coefficient_below(i, j)
                j += 1
                break

        return system

    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        num_equtation = len(self)

        for k in range(row+1, num_equtation):
            coefficient = MyDecimal(self[k].normal_vector[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True

        return False

    def clear_coefficient_below(self, row, col):
        num_equtation = len(self)
        beta = MyDecimal(self[row].normal_vector[col])

        for k in range(row+1, num_equtation):
            n = self[k].normal_vector
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)

    def compute_rref(self):
        tf = self.compute_triangular_form()

        num_equatation = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()   # 主变量索引，即每行首项变量的索引列表

        for i in range(num_equatation)[::-1]:

            j = pivot_indices[i]
            if j < 0:
                continue

            tf.scale_row_to_make_coefficient_equal_one(i, j)
            tf.clear_coefficient_above(i, j)

        return tf


    def scale_row_to_make_coefficient_equal_one(self, row, col):
        n = self[row].normal_vector
        print n[col]
        beta = Decimal('1.0')/n[col]
        self.multiply_coefficient_and_row(beta, row)


    def clear_coefficient_above(self, row, col):
        for k in range(row)[::-1]:
            n = self[k].normal_vector
            alpha = -(n[col])
            self.add_multiple_times_row_to_row(alpha, row, k)


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']), constant_term='-1') and
                r[1] == p2):
    print 'test case 1 failed'

# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# r = s.compute_rref()
# if not (r[0] == p1 and
#                 r[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
# s = LinearSystem([p1, p2, p3, p4])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']), constant_term='0') and
#                 r[1] == p2 and
#                 r[2] == Plane(normal_vector=Vector(['0', '0', '-2']), constant_term='2') and
#                 r[3] == Plane()):
#     print 'test case 3 failed'
#
# p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
# s = LinearSystem([p1, p2, p3])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']), constant_term=Decimal('23') / Decimal('9')) and
#                 r[1] == Plane(normal_vector=Vector(['0', '1', '0']),
#                               constant_term=Decimal('7') / Decimal('9')) and
#                 r[2] == Plane(normal_vector=Vector(['0', '0', '1']),
#                               constant_term=Decimal('2') / Decimal('9'))):
#     print 'test case 4 failed'


# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#                 t[1] == p2):
#     print 'test case 1 failed'
#
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#                 t[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
# s = LinearSystem([p1, p2, p3, p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#                 t[1] == p2 and
#                 t[2] == Plane(normal_vector=Vector(['0', '0', '-2']), constant_term='2') and
#                 t[3] == Plane()):
#     print 'test case 3 failed'
#
# p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
# s = LinearSystem([p1, p2, p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2') and
#                 t[1] == Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1') and
#                 t[2] == Plane(normal_vector=Vector(['0', '0', '-9']), constant_term='-2')):
#     print 'test case 4 failed'


# p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
#
# s = LinearSystem([p0, p1, p2, p3])
# s.swap_rows(0, 1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 1 failed'
#
# s.swap_rows(1, 3)
# if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
#     print 'test case 2 failed'
#
# s.swap_rows(3, 1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 3 failed'
#
# s.multiply_coefficient_and_row(1, 0)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 4 failed'
#
# s.multiply_coefficient_and_row(-1, 2)
# if not (s[0] == p1 and
#                 s[1] == p0 and
#                 s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 5 failed'
#
# s.multiply_coefficient_and_row(10, 1)
# if not (s[0] == p1 and
#                 s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
#                 s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 6 failed'
#
# s.add_multiple_times_row_to_row(0, 0, 1)
# if not (s[0] == p1 and
#                 s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
#                 s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 7 failed'
#
# s.add_multiple_times_row_to_row(1, 0, 1)
# if not (s[0] == p1 and
#                 s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
#                 s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 8 failed'
#
# s.add_multiple_times_row_to_row(-1, 1, 0)
# if not (s[0] == Plane(normal_vector=Vector(['-10', '-10', '-10']), constant_term='-10') and
#                 s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
#                 s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 9 failed'


# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])
#
# print s.indices_of_first_nonzero_terms_in_each_row()
# print "--------"
# print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
# print "--------"
# print len(s)
# print s
# print "--------"
#
# s[0] = p1
# print s
#
# print MyDecimal('1e-9').is_near_zero()
# print MyDecimal('1e-11').is_near_zero()
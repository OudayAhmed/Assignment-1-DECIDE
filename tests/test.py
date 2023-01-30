import test_cmv
import test_fuv

test = test_cmv.TestCMV()

test.test_cmv_1_positive()
test.test_cmv_1_negative()
test.test_cmv_1_negative_radius1()

test.test_cmv_13_positive()
test.test_cmv_13_negative_fail_condition_1()
test.test_cmv_13_negative_fail_condition_2()
test.test_cmv_13_negative_radius2()
test.test_cmv_13_negative_NUMPOINTS()

test.test_cmv_14_positive()
test.test_cmv_14_negative_fail_condition_1()
test.test_cmv_14_negative_fail_condition_2()
test.test_cmv_14_negative_area2()
test.test_cmv_14_negative_NUMPOINTS()

test1 = test_fuv.TestFUV()
test1.test_fuv_positive_condition_1()
test1.test_fuv_positive_condition_2()
test1.test_fuv_negative()
test1.test_fuv_random()
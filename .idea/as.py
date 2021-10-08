import HMS

def test_measure_pulse():
    a = HMS.measure_pulse(40,50,60)
    assert (a != "negative")

def test_abnormal():
    a = HMS.abnormal(60,70,90,100)
    assert(a == none)

import main.py

stub = stubout.StubOutForTesting()
stub.Set(measure_pulse, (r1, r2, r3))

def test_measure_pulse():
    return






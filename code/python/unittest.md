# unittest

```python
#!/usr/bin/python3
import unittest

def find(num: int):
    if num != 0:
    	return True
    else:
    	return False

class TestZf(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, find(9))

    def test_2(self):
        self.assertEqual(False, find(0))

if __name__ == "__main__":
    # 0不输出1默认2详细
    unittest.main(verbosity=2)
```


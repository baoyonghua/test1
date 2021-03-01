import os,sys
base = os.path.abspath(__file__)
sys.path.append(base)
import pytest

# if __name__ == '__main__':
pytest.main(["-s", "-v"])
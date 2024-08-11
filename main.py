import unittest

def valid(s:list[str])-> bool:
    return validParenthesis('',s)
openCloseMap ={'(':')','{':'}','[':']'}
def validParenthesis(before:str, string: list[str]) -> bool:
    if openCloseMap.get(string[0]):
        return validParenthesis(before+string[0], string[1:]) if len(string)>1 else False
    elif before =='':
        return False
    elif openCloseMap[before[-1]]==string[0]:
        if len(string)>1: return validParenthesis(before[:-1], string[1:])
        elif len(before)>1: return False
        else: return True
    else:
        return False



class TestValidParenthesisChecker(unittest.TestCase):
    def test_parenthesis(self):
        for testStr, expectation in {
                '(': False,
                '()': True,
                '([)': False,
                ')': False,
                '())': False,
                '([{}])()[]{}': True,
                '({[(())]})()': True,
                '({[(())]})())': False,
                '(((()': False,
                '(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()': False,
        }.items():
            self.assertEqual(valid(list(testStr)), expectation)

if __name__=='__main__':
    unittest.main()

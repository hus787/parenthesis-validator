import unittest

openCloseMap ={'(':')','{':'}','[':']'}

def AreParenthesisValid(s:str)-> bool:
    return areParenthesisValid('',list(s))

def areParenthesisValid(unclosedParenthesis:str, string: list[str]) -> bool:
    if openCloseMap.get(string[0]):
        # if first one is opening parenthesis and remaining parenthesis are more
        # than one than recurse otherwise not valid
        return areParenthesisValid(unclosedParenthesis+string[0], string[1:]) if len(string)>len(unclosedParenthesis) else False
    elif unclosedParenthesis =='':
        # if no unclosed parenthesis and first parenthesis not opening than not valid
        return False
    elif openCloseMap[unclosedParenthesis[-1]]==string[0]:
        # if matching closing parenthesis and
        #  more than one parenthesis remaining than recurse
        if len(string)>=len(string[1:]): return areParenthesisValid(unclosedParenthesis[:-1], string[1:])
        #  if no more than one parenthesis remaining and there are still unclosed
        #  parenthese than not valid
        elif len(unclosedParenthesis)>1: return False
        #  valid parenthesis
        else: return True
    else:
        # not a valid closing parenthesis therefore not valid
        return False

class TestAreParenthesisValid(unittest.TestCase):
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
                'sdfasdf': False,
                '(asdf)': False
        }.items():
            self.assertEqual(AreParenthesisValid(testStr), expectation)

if __name__=='__main__':
    unittest.main()

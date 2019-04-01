class Solution:
    def IntoPost(self, list_in):
        list_post = []
        list_symbol = []
        length = len(list_in)
        num = 0
        flag = False
        for i in range(length):
            tmp = list_in[i]
            if tmp.isdigit():
                flag = True
                num = num * 10 + int(tmp)
            if i == length-1 or tmp in '+-*/()':
                if flag:
                    list_post.append(num)
                    num = 0
                    flag = False
            if tmp in '+-*/()':
                if tmp == '*/(' or len(list_symbol) == 0:
                    list_symbol.append(tmp)
                elif tmp == ')':
                    symbol = list_symbol.pop()
                    while symbol != '(':
                        list_post.append(symbol)
                        symbol = list_symbol.pop()
                elif tmp in '+-' and list_symbol[len(list_symbol) - 1] in '*/':
                    if list_symbol.count('(') == 0:
                        while list_symbol:
                            list_post.append(list_symbol.pop())
                    else:
                        symbol = list_symbol.pop()
                        while symbol != '(':
                            list_post.append(symbol)
                            symbol = list_symbol.pop()
                        list_symbol.append('(')
                    list_symbol.append(tmp)
                else:
                    list_symbol.append(tmp)
        while list_symbol:
            list_post.append(list_symbol.pop())
        return list_post


    def calcultor(self, list_post):
        list_out = []
        for i in range(len(list_post)):
            tmp = list_post[i]
            if type(tmp) is str:
                A = list_out.pop()
                B = list_out.pop()
                if tmp == '+':
                    list_out.append(B+A)
                elif tmp == '-':
                    list_out.append(B-A)
                elif tmp == '*':
                    list_out.append(B*A)
                elif tmp == '/':
                    list_out.append(B/A)
            else:
                list_out.append(tmp)
        result = int(list_out[0])
        return result



if __name__ == '__main__':
    list_in = input()
    a = Solution()
    print(a.IntoPost(list_in))  # 输出后缀表达式
    print(a.calcultor(a.IntoPost(list_in)))  # 输出最后结果

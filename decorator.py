def div(a,b):
    return (a/b)
def smart_div(func):
    def swap(a,b):
        if a<b:
            a,b=b,a
        return (func(a,b))

    return (swap)
div1=smart_div(div)
res=div1(2,4)
print(res)
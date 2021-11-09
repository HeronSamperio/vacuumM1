import subprocess

print("Cantidad de aspiradoras: ")
mode=int(input())

if mode == 1:
    import aspiradora1
    exec(open("aspiradora1.py").read())
    
if mode == 2:
    import aspiradora
    
    try:
        exec(open("aspiradora.py").read())
    except AttributeError:
        exec(open("aspiradora.py").read())
    except IndexError:
        exec(open("aspiradora.py").read())
    finally:
        print("fin")
        
if mode == 3:
    import aspiradora3
    
    try:
        exec(open("aspiradora3.py").read())
    except AttributeError:
        exec(open("aspiradora3.py").read())
    except IndexError:
        exec(open("aspiradora.py").read())
    finally:
        print("fin")
    
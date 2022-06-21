

class mystring:
    whitespace = ' \t\n\r\v\f'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_letters = ascii_lowercase + ascii_uppercase
    digits = '0123456789'
    alnum = ascii_letters + digits
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    all_ascii = digits + ascii_letters + punctuation + whitespace

    identifier_invalid = digits + punctuation

    lower_upper = {k: v for k, v in zip(ascii_lowercase, ascii_uppercase)}
    upper_lower = {v: k for k, v in lower_upper.items()}

    def __init__(self, s: str):
        self.s = s
    
    def __str__(self) -> str:
        return self.s

    def __repr__(self) -> str:
        return self.s

    def __add__(self, __o: object) -> "mystring":
        if not isinstance(__o, mystring): raise TypeError(f"+ is not supported between instances of 'mystring' and '{type(__o)}")
        return mystring(self.s + __o.s)
    
    def capitalize(self) -> "mystring":
        """
        Capitalizes the first letter and the rest are lowercased
        """
        new = mystring(self.s[0]).upper() + mystring(self.s[1:]).lower()
        return new
        
    def count(self, sub: str) -> int:
        """
        Returns the number of occurences of the substring `sub`
        """
        if not sub: return len(self.s) + 1
        ct = 0
        for i in range(len(self.s)):
            if self.s[i] == sub[0]:
                found = True
                for j in range(len(sub)):
                    if self.s[i+j] != sub[j]:
                        found = False
                        break
                if found: ct += 1
        return ct

    def endswith(self, sub: "str|tuple[str]") -> bool:
        """
        Returns True if the string ends with subtring `sub` or any of the subtrings in tuple `sub`
        """
        if sub == "": return True
        if isinstance(sub, tuple):
            if len(sub) == 0: return False
        
        if isinstance(sub, str):
            if sub in self.s and self.s[-1] == sub[-1]: return True
        elif isinstance(sub, tuple):
            for _sub in sub:
                if not isinstance(_sub, str):
                    raise TypeError(f"tuple for endswith must only contain str, not {type(_sub)}")

                if _sub in self.s and self.s[-1] == _sub[-1]: return True
        else:
            raise TypeError("sub must be str or tuple of str")
        return False

    def startswith(self, sub: "str|tuple[str]") -> bool:
        """
        Returns True if the string starts with subtring `sub` or any of the subtrings in tuple `sub`
        """
        if sub == "": return True
        if isinstance(sub, tuple):
            if len(sub) == 0: return False
        
        if isinstance(sub, str):
            if sub in self.s and self.s[0] == sub[0]: return True
        elif isinstance(sub, tuple):
            for _sub in sub:
                if not isinstance(_sub, str):
                    raise TypeError(f"tuple for startwith must only contain str, not {type(_sub)}")

                if _sub in self.s and self.s[0] == _sub[0]: return True
        else:
            raise TypeError("sub must be str or tuple of str")
        return False

    def find(self, sub: str, start: int = 0, stop: int = -1) -> int:
        """
        Returns the starting index of the substring `sub`in the range [`start`:`stop`] if found, else -1
        """
        if stop == -1: stop = len(self.s)
        if sub in self.s[start:stop]:
            return self.index(self.s, sub, start, stop)
        return -1

    def index(self, sub: str, start: int = 0, stop: int = -1) -> int:
        """
        Same as `find`, except this raises `ValueError` if not found!
        """
        if stop == -1: stop = len(self.s)
        if sub in self.s[start:stop]:
            for i in range(start, len(self.s)):
                if self.s[i] == sub[0]:
                    found = True
                    for j in range(len(sub)):
                        if self.s[i+j] != sub[j]:
                            found = False
                            break       
                    if found: return i
                    
        raise ValueError(f"'{sub}' was not found in '{self.s}' in range [{start}:{stop}]")

    def isalnum(self) -> bool:
        """
        Returns True if all characters in the string are alphanumeric and if the string is non-empty, False otherwise
        """
        # for i in self.s:
        #     if i not in self.alnum:
        #         return False
        # return True
        return all([i in self.alnum for i in self.s]) if self.s else False

    def isaplha(self) -> bool:
        """
        Returns True if all characters in the string are alphabets and if the string is non-empty, False otherwise
        """
        return all([i in self.ascii_letters for i in self.s]) if self.s else False

    def isascii(self) -> bool:
        """
        Returns True if all characters in the string are ascii and if the string is non-empty, False otherwise
        """
        return all([i in self.all_ascii for i in self.s]) if self.s else False

    def isdecimal(self) -> bool:
        """
        Returns True if all characters in the string are decimal and if the string is non-empty, False otherwise
        """
        return all([i in self.digits for i in self.s]) if self.s else False
    
    # TODO: Doubt, are they both same???
    def isdigit(self) -> bool:
        """
        Returns True if all characters in the string are digits and if the string is non-empty, False otherwise
        """
        return self.isdecimal()

    def isidentifier(self) -> bool:
        """
        Returns True if the string is a valid python identifier
        Note: for keywords, call `keyword.iskeyword()`
        """
        if not self.s: return False
        if " " in self.s: return False
        if self.s[0] in self.identifier_invalid: return False
        for i in self.punctuation:
            if i in self.s: return False
            
        return True

    def islower(self) -> bool:
        """
        Returns True if all characters in the string are lowercase and if the string is non-empty, False otherwise
        """
        return all([i in self.ascii_lowercase for i in self.s]) if self.s else False
    
    # TODO: Doubt, are they all same???
    def isnumeric(self) -> bool:
        """
        Returns True if all characters in the string are numeric and if the string is non-empty, False otherwise
        """
        return self.isdecimal()
    
    def isprintable(self) -> bool:
        """
        Returns True if all characters in the string are printable and if the string is non-empty, False otherwise
        """
        return self.isascii()

    def isspace(self) -> bool:
        """
        Returns True if all characters in the string are whitespace and if the string is non-empty, False otherwise
        """
        return all([i in self.whitespace for i in self.s]) if self.s else False

    def istitle(self) -> bool:
        """
        Returns True if each word is capitialized, False otherwise.
        """
        words = self.split()
        for i in words:
            if i.s != i.capitalize().s: return False
        return True
    
    def isupper(self) -> bool:
        """
        Returns True if all characters in the string are uppercased and if the string is non-empty, False otherwise
        """
        return all([i in self.ascii_uppercase for i in self.s]) if self.s else False

    def join(self, seq: list) -> "mystring":
        """
        """
        new = ""
        for i in seq:
            if i == seq[-1]:
                new += str(i)
            else:
                new += str(i) + self.s
        return mystring(new)

    def lower(self) -> "mystring":
        new = ""
        for i in self.s:
            if i in self.upper_lower.keys():
                new += self.upper_lower[i]
            else:
                new += i
        return mystring(new)

    def removeprefix(self, pref: str) -> "mystring":
        """
        """
        if self.startswith(pref):
            return mystring(self.s[len(pref):])
        return self

    def removesuffix(self, suff) -> "mystring":
        """
        """
        if self.endswith(suff):
            return mystring(self.s[:-len(suff)])
        return self

    def replace(self, old: str, new: str, num_occur: int=-1) -> "mystring":
        """
        """
        starts = []
        ct = self.count(old)
        if ct == 0: return self.s

        if num_occur == -1: num_occur = ct
        if num_occur > ct: num_occur = ct
            
        for i in range(num_occur):
            if i == 0: starts.append(self.index(old))
            else: starts.append(self.index(old, start=starts[-1]+1))
                
        stops = [j + len(old) for j in starts]
            
        temp = ""
        for i in range(len(starts)):
            if i == 0:
                if len(starts) == 1:
                    temp += self.s[:starts[i]] + new + self.s[stops[i]:]
                else:
                    temp += self.s[:starts[i]] + new
                        
            elif i == len(starts) - 1:
                temp += self.s[stops[i-1]:starts[i]] + new + self.s[stops[i]:]
            else:
                temp += self.s[stops[i-1]:starts[i]] + new
                    
        return mystring(temp)

    def split(self, sep=None, maxsplit: int=-1) -> "list[mystring]":
        """
        """
        if sep == "": raise ValueError("Empty Seperator!")
        if sep is None: sep = " "
        ls = []
        
        starts = []
        ct = self.count(sep)
        if ct == 0: return [self.s]
        if maxsplit == -1: maxsplit = ct
        if maxsplit > ct: maxsplit = ct
            
        for i in range(maxsplit):
            if i == 0: starts.append(self.index(sep))
            else: starts.append(self.index(sep, start=starts[-1]+1))
                
        stops = [j + len(sep) for j in starts]
            
        for i in range(len(starts)):
            if i == 0:
                if len(starts) == 1:
                    ls.append(self.s[:starts[i]])
                    ls.append(self.s[stops[i]:])
                else:
                    ls.append(self.s[:starts[i]])
                        
            elif i == len(starts) - 1:
                ls.append(self.s[stops[i-1]:starts[i]])
                ls.append(self.s[stops[i]:])
            else:
                ls.append(self.s[stops[i-1]:starts[i]])

        for i in ls:
            ls[ls.index(i)] = mystring(i)

        return ls

    def strip(self, chars: str=None) -> "mystring":
        """
        """
        if chars == None: chars = " "
        new = self
        while new.startswith(tuple(chars)):
            for i in chars:
                new = new.removeprefix(i)
        while new.endswith(tuple(chars)):
            for i in chars:
                new = new.removesuffix(i)
        return new

    def lstrip(self, chars: str=None) -> "mystring":
        if chars == None: chars = " "
        
        new = self
        while new.startswith(tuple(chars)):
            for i in chars:
                new = new.removeprefix(i)  
        return new
        
    def rstrip(self, chars: str=None) -> "mystring":
        if chars == None: chars = " "
        
        new = self
        while new.endswith(tuple(chars)):
            for i in chars:
                new = new.removesuffix(i)
        return new

    def title(self) -> "mystring":
        if " " not in self.s:
            return self.capitalize()
            
        words = self.split()
        new_words = []
        for i in words:
            new_words.append(i.capitalize())
            
        return mystring(" ").join(new_words)

    def upper(self) -> "mystring":
        new = ""
        for i in self.s:
            if i in self.lower_upper.keys():
                new += self.lower_upper[i]
            else:
                new += i
        return mystring(new)

a = mystring("hello every on Ehere!")
print(a.title().istitle())
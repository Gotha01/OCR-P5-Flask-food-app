def display(number, symbol, txt, empty_line = False,
            symbolbis = "", where="center"):
            #Message display function with frame in the terminal
    result = ""
    symbol_line = number * symbol
    d_line = "\n" + symbolbis + (number - 2) * " " + symbolbis
    
    if isinstance(txt, list):
        if isinstance(empty_line, int):
            texts = []
            for element in txt:
                if (len(element) % 2) != 0:
                    element = element + " "
                if where == 'center':
                    space = int((number - (len(symbolbis) * 2 + len(element))) / 2) * " "
                    linetxt = symbolbis + space + element + space + symbolbis
                    texts.append(linetxt)
                elif where == 'left':
                    space = int((number - (len(symbolbis) * 2 + len(element))) / 2) * " "
                    linetxt = symbolbis + element + space * 2 + symbolbis
                    texts.append(linetxt)
                elif where == 'right':
                    space = int((number - (len(symbolbis) * 2 + len(element))) / 2) * " "
                    linetxt = symbolbis + space * 2 + element + symbolbis
                    texts.append(linetxt)
            result = symbol_line + empty_line * d_line + "\n" + \
                "\n".join(texts) + empty_line * d_line + "\n" + symbol_line
        else:
            for element in txt:
                if (len(element) % 2) != 0:
                    element = element + " "
                linetxt = "\n" + element
                space = int((number - (len(symbolbis) * 2 + len(element))) / 2) * " "
            if where == 'center':
                result = symbol_line + "\n" + \
                    symbolbis + space + linetxt + space + symbolbis + \
                    "\n" + symbol_line
            elif where == 'left':
                result = symbol_line + "\n" + \
                    symbolbis + linetxt + space * 2 + symbolbis + \
                    "\n" + symbol_line
            elif where == 'right':
                result = symbol_line + "\n" + \
                    symbolbis + space * 2 + linetxt + symbolbis + \
                    "\n" + symbol_line


    elif isinstance(txt, str):
        space = int((number - (len(symbolbis) * 2 + len(txt))) / 2) * " "
        if isinstance(empty_line, int):
            if (len(txt) % 2) != 0:
                    txt = txt + " "
            if where == 'center':
                result = symbol_line + empty_line * d_line + "\n" + \
                    symbolbis + space + txt + space + symbolbis + \
                    empty_line * d_line + "\n" + symbol_line
            elif where == 'left':
                result = symbol_line + empty_line * d_line + "\n" + \
                    symbolbis + txt + space * 2 + symbolbis + \
                    empty_line * d_line + "\n" + symbol_line
            elif where == 'right':
                result = symbol_line + empty_line * d_line + "\n" + \
                    symbolbis + space * 2 + txt + symbolbis + \
                    empty_line * d_line + "\n" + symbol_line
        else:
            if where == 'center':
                result = symbol_line + "\n" + \
                    symbolbis + space + txt + space + symbolbis + \
                    "\n" + symbol_line
            elif where == 'left':
                result = symbol_line + "\n" + \
                    symbolbis + txt + space * 2 + symbolbis + \
                    "\n" + symbol_line
            elif where == 'right':
                result = symbol_line + "\n" + \
                    symbolbis + space *2 + txt + symbolbis + \
                    "\n" + symbol_line
    return result